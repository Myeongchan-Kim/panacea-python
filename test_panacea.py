from panacea import *

if __name__ == "__main__":

    node = PanaceaNode('localhost')

    pprint(node.get_info())

    pprint(node.is_sync())

    latest_block = node.get_block_latest()
    print(latest_block)
