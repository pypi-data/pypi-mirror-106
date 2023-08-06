from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED
from simple_salesforce import Salesforce
import requests
from datetime import datetime
import os
import time
import random
import string
import pandas as pd


class CassandraManager:
    """
    Cassandra Cluster center
    :param key_space: session keyspace to set for the Cluster
    """
    def __init__(self, username, password, pem_file_path, key_space='delpha_actions'):
        ssl_context = SSLContext(PROTOCOL_TLSv1_2)
        ssl_context.load_verify_locations(pem_file_path)
        ssl_context.verify_mode = CERT_REQUIRED
        ssl_context.check_hostname = True

        cassandra_username = os.environ.get('CASSANDRA_USERNAME', username)
        cassandra_password = os.environ.get('CASSANDRA_PWD', password)
        cassandra_dc1 = os.environ.get('CASSANDRA_DC1', 'DATACENTER_EU_WEST_1')
        cassandra_node1 = os.environ.get('CASSANDRA_NODE1', '52.215.22.60')
        cassandra_node2 = os.environ.get('CASSANDRA_NODE2', '34.254.52.140')
        cassandra_node3 = os.environ.get('CASSANDRA_NODE3', '34.251.123.6')

        self._cluster = Cluster(
            [
                cassandra_node1, cassandra_node2, cassandra_node3
            ],
            load_balancing_policy=DCAwareRoundRobinPolicy(local_dc=cassandra_dc1),
            port=9042,
            auth_provider=PlainTextAuthProvider(
                username=cassandra_username,
                password=cassandra_password
            ),
            ssl_context=ssl_context
        )
        self._keyspace = key_space
        self._session = self._cluster.connect(key_space)
        self._session.row_factory = dict_factory
        print('Connected to cluster %s' % self._cluster.metadata.cluster_name)
        for host in self._cluster.metadata.all_hosts():
            print('Datacenter: %s; Host: %s; Rack: %s' % (host.datacenter, host.address, host.rack))

    def __del__(self):
        self._cluster.shutdown()

    def disconnect(self):
        print("Cluster is disconnected !")
        self._cluster.shutdown()

    @property
    def cluster(self):
        return self._cluster

    @property
    def session(self):
        return self._session

    @property
    def keyspace(self):
        return self._keyspace
    
    def set_keyspace(self, key_space):
        self._keyspace = key_space
        self._session.set_keyspace(key_space)

    def execute(self, query_string, *args, **kwargs):
        """
        Execute a cql command, as a blocking call that will not return until the statement is finished executing.
        :param query_string: query executed
        """
        return self._session.execute(query_string, *args, **kwargs)

    def execute_async(self, query_string, *args, **kwargs):
        """
        Execute a cql command asynchronously (program continues and getting a future_response)
        :param query_string: query executed
        """
        return self._session.execute_async(query_string, *args, **kwargs)

    
class SalesforceManager:
    """
    Salesforce Manager
    :param instance_name: Salesforce Instance name
    :param client_id: Consumer ID for authorized app
    :param client_secret: Consumer Secret for authorized app
    :param username: usernam to login to Instance of Salesforce
    :param password: password to login to Instance of Salesforce
    :param security_token: User's security token
    """
    def __init__(self, instance_name, client_id, client_secret, username, password, security_token):
        print("Connecting to Salesforce...")
        params = {
            "grant_type": "password",
            "client_id": client_id, # Consumer Key
            "client_secret": client_secret, # Consumer Secret
            "username": username,
            "password": password+security_token
        }
        r = requests.post(f"https://{instance_name}.my.salesforce.com/services/oauth2/token", params=params)
        self.access_token = r.json().get("access_token")
        self.instance_url = r.json().get("instance_url")
        self.headers = {
            'Content-type': 'application/json',
            'Accept-Encoding': 'gzip',
            'Authorization': 'Bearer %s' % self.access_token
        }
        print(r.json())
        self.api_url = self.instance_url+'/services/data/v51.0/'
        self.describe_columns = ["name", "label", "type", "custom", "referenceTo", ]
        print("Credentials acquired !")

    def help(self):
        sf_url = self.api_url
        r = requests.request('get', self.api_url, headers=self.headers)
        if r.status_code < 300:
            return r.json()
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
            
    def execute(self, api_route, method="get", params={}, data={}):
        """
        Generalized execute system for Salesforce API
        :param api_route: api route to use
        :param params: Object to send to the API as additive data
        """
        sf_url = self.api_url + f'{api_route}'
        
        if method == 'get':
            r = requests.request('get', sf_url, headers=self.headers, params=params)
        else:
            r = requests.request(method, sf_url, headers=self.headers, json=data, params=parameters, timeout=10)
        if r.status_code < 300:
            return r.json()
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
        
    def query(self, query, to_pandas=True):
        """
        Simple query system for Salesforce
        :param query: String SOQL query to run
        """
        parameters = {
            'q': query
        }
        sf_url = self.api_url + 'query/'
        r = requests.request('get', sf_url, headers=self.headers, params=parameters)
        results = []
        if r.status_code < 300:
            curr_results = r.json()
            results = curr_results
            while curr_results.get("nextRecordsUrl"):
                next_r = self._query_next(curr_results.get("nextRecordsUrl").split('/')[-1:][0])
                curr_results = next_r
                results["records"] = [*results["records"], *curr_results["records"]]
            if to_pandas:
                return pd.DataFrame(results["records"]), results["totalSize"]
            else:
                return results["records"], results["totalSize"]
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
            
    def _query_next(self, next_url):
        sf_url = self.api_url + 'query/' + next_url
        r = requests.request('get', sf_url, headers=self.headers)
        if r.status_code < 300:
            curr_results = r.json()
            return curr_results
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
        return 
            
    def describe_object(self, sf_object, to_pandas=True):
        """
        Describe a Salesforce object
        :param sf_object: String Saleforce object name to describe
        :param to_pandas: Boolean to set pandas dataframe result or not
        """
        sf_url = self.api_url + f'sobjects/{sf_object}/describe'
        r = requests.request('get', sf_url, headers=self.headers)
        if r.status_code < 300:
            if to_pandas:
                return pd.DataFrame(r.json()["fields"])[self.describe_columns]
            else:
                return r.json()["fields"]
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
         
    def search(self, search_q, to_pandas=True):
        """
        Simple search system for Salesforce
        :param search_q: search item to look for
        """
        parameters = {
            'q': "FIND {"+search_q+"}"
        }
        
        sf_url = self.api_url + 'search/'
        r = requests.request('get', sf_url, headers=self.headers, params=parameters)
        if r.status_code < 300:
            if to_pandas:
                return pd.DataFrame(r.json()["searchRecords"])
            else:
                return r.json()
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))     

    def get_record(self, record_id, record_type, to_pandas=True):
        """
        Get a Salesforce record from Salesforce
        :param record_id: String Saleforce object Id to get
        :param record_type: String Saleforce object name to get
        """
        sf_url = self.api_url + f'sobjects/{record_type}/{record_id}'
        r = requests.request('get', sf_url, headers=self.headers)
        if r.status_code < 300:
            if to_pandas:
                return pd.DataFrame(r.json())[self.describe_columns]
            else:
                return r.json()
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
            
    def insert(self, object_name, data={}, parameters={}, to_pandas=True):
        """
        Simple Insert system of Salesforce
        :param object_name: String object to insert data into
        :param data: Dict data to insert json
        :param parameters: Dict Parameters of request 
        """
        sf_url = self.api_url + 'sobjects/' + object_name + "/"
        r = requests.request('post', sf_url, headers=self.headers, json=data, params=parameters, timeout=10)
        if r.status_code < 300:
            return r.json()
        else:
            raise Exception('API error when calling %s : %s' % (r.url, r.content))
            