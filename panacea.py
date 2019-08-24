import os, sys
import subprocess, shlex
import socket

from subprocess import PIPE, CalledProcessError, check_call, Popen
import json
from pprint import pprint
import requests
import logging
from urllib.parse import urljoin

class PanaceaNode(object):
    def __init__(self, ip, port=1317, acc_addr=None):

        assert(is_ip(ip))
        self.__ip = ip

        assert(type(port) == int)
        self.__port = port

        assert(type(acc_addr) == str or acc_addr == None)
        self.__addr = acc_addr

        self.raw_status = None
        self.channels = None
        self.id = None
        self.listen_addr = None
        self.moniker = None
        self.chain_id = self.network = None
        self.rpc_addressb = None
        self.tx_index = None
        self.protocol_version = None
        self.version = None

    def get_ip_addr(self):
        return self.__ip

    def get_acc_addr(self):
        return self.__addr

    def get_response(self, api_url, data=None):

        base_url = "http://{}:{}".format(self.__ip, self.__port)
        url = urljoin(base_url, api_url)

        try:
            response = requests.get(url, data=data)
            data = json.loads(response.content)
            return data

        except requests.exceptions.ConnectionError as e:
            logging.error(e)
            return None

    def set_node_params(self, status_dict):
        self.raw_status = status_dict
        self.channels = status_dict['channels']
        self.__addr = self.id = status_dict['id']
        self.listen_addr = status_dict['listen_addr']
        self.moniker = status_dict['moniker']
        self.chain_id = self.network = status_dict['network']
        self.rpc_addressb = status_dict['other']['rpc_address']
        self.tx_index = status_dict['other']['tx_index']
        self.protocol_version = status_dict['protocol_version']
        self.version = status_dict['version']
        return status_dict

    def renew_status(self):
        result_output = self.get_response(api_url='/node_info')

        if result_output is None or result_output.get('error', False):
            print(result_output)
            return

        ## Save node status information
        self.set_node_params(result_output)

    def get_info(self):
        self.renew_status()
        return self.raw_status

    def is_sync(self):
        api_url = "/syncing"
        result_output = self.get_response(api_url)

        if type(result_output) == bool:
            return result_output
        elif result_output is None or result_output.get('error', False):
            print(result_output)
            return

        raise NotImplementedError

    def get_block_latest(self):
        api_url = '/blocks/latest'
        result_output = self.get_response(api_url)

        if result_output is None or result_output.get('error', False):
            print(result_output)
            return

        block = PanaceaBlock.from_res_dict(result_output)
        return block

    def get_block(self, height):
        api_url = '/blocks/{}'.format(height)
        result_output = self.get_response(api_url)

        if result_output is None or result_output.get('error', False):
            print(result_output)
            return

        block = PanaceaBlock.from_res_dict(result_output)
        return block

    def get_validatorset_latest(self):
        pass  ## TODO: get latest validator set

    def get_validatorset(self, height):
        pass  ## TODO: get valdator set of given height

    def get_txs(self, hash=None):
        pass  ## TODO: get transaction with hash

    def search_txs(self, tag, page=None, limit=None):
        pass ## TODO: search tranjaction with tag info

    def send_transaction(self):
        pass ## TODO make transaction

class PanaceaBlock(object):
    @classmethod
    def from_res_dict(cls, res_dict):
        pprint(res_dict)

        ## Height
        block_height = res_dict['block']['header']['height']

        ## Chain id
        chain_id = res_dict['block']['header']['chain_id']

        ## Block hash
        block_hash = res_dict['block_meta']['block_id']['hash']

        block = PanaceaBlock(block_height, chain_id=chain_id, block_hash=block_hash)

        ## Set all transactions
        txs = res_dict['block']['data']['txs']
        if txs is None:
            txs = []
        block.txs = txs
        block.__num_txs = int(res_dict['block']['header']['num_txs'])
        assert  block.__num_txs == len(txs)

        ## Generated time
        block.__time = res_dict['block']['header']['time']


        ## Other information
        block.__app_hash = res_dict['block']['header']['app_hash']
        block.__consensus_hash = res_dict['block']['header']['consensus_hash']
        block.__data_hash = res_dict['block']['header']['data_hash']
        block.__evidence_hash = res_dict['block']['header']['evidence_hash']
        block.__last_block = PanaceaBlock(
            height=str(int(block_height) - 1),
            chain_id=chain_id,
            block_hash=res_dict['block']['header']['last_block_id']['hash'],
        )
        block.__last_commit = res_dict['block']['last_commit']



        return block

    def __init__(self, height, chain_id=None, block_hash=None, chain_hash=None):
        self.height = height
        self.hash = block_hash
        self.chain_id = chain_id
        self.chain_hash = chain_hash

        if block_hash is None:
            pass # TODO: add block hash query to node

    def __hash__(self):
        return f"chainId:{self.chain_id}, height:{self.height}, block_hash:{self.hash}"

    def __str__(self):
        return f"<Panacea Block Object : {self.__hash__()}>"

    def get_timestamp(self):
        return self.__time


class PanaceaTransaction(object):
    pass #TODO


class PananceaValiator(object):
    pass #TODO


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

    ## Get 2nd block
    second_block = node.get_block(2)
    print(second_block)

    print(second_block.get_timestamp())
