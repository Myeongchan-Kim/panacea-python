import os, sys
import subprocess, shlex
import socket

from subprocess import PIPE, CalledProcessError, check_call, Popen
import json
from pprint import pprint
import requests
import logging

class PanaceaNode(object):
    def __init__(self, ip, port=1317, acc_addr=None):

        assert(is_ip(ip))
        self.__ip = ip

        assert(type(port) == int)
        self.__port = port

        assert(type(acc_addr) == str or acc_addr == None)
        self.__addr = acc_addr

    def get_ip_addr(self):
        return self.__ip

    def get_acc_addr(self):
        return self.__addr

    def make_response(self, url, data=None):
        try:
            response = requests.get(url, data=data)
            data = json.loads(response.content)
            return data
        except requests.exceptions.ConnectionError as e:
            logging.error(e.message)
            return None

    def set_node_params(self, status_dict):
        self.raw_status = status_dict
        self.channels = status_dict['channels']
        self.id = status_dict['id']
        self.listen_addr = status_dict['listen_addr']
        self.moniker = status_dict['moniker']
        self.chain_id = self.network = status_dict['network']
        self.rpc_addressb = status_dict['other']['rpc_address']
        self.tx_index = status_dict['other']['tx_index']
        self.protocol_version = status_dict['protocol_version']
        self.version = status_dict['version']
        return status_dict

    def renew_status(self):
        url = "http://{}:{}/node_info".format(self.__ip, self.__port)
        result_output = self.make_response(url)
        if result_output is None:
            return None

        ## Save node
        self.set_node_params(result_output)

    def get_info(self):
        self.renew_status()
        return self.raw_status


class PanaceaAccount(object):
    pass #TODO


class AOLWriter(PanaceaAccount):
    pass #TODO


class AOLOwner(PanaceaAccount):
    pass #TODO


def getNodeFromLocalhost(self):
    pass #TODO

def is_ip(text):
    if text == 'localhost':
        text = '127.0.0.1'

    try:
        socket.inet_aton(text)
        return True
    except socket.error:
        return False

if __name__ == "__main__":

    node = PanaceaNode('localhost')
    pprint(node.get_info())
