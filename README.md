# panacea-python
Python library to use panancea (panacea git repository: https://github.com/medibloc/panacea-core)


## Requirment 
  - Supported OS : Ubuntu 18.04
  - Go 1.12++
  - Python 3.7++
  - Panacea-core : [here](https://medibloc.gitbook.io/panacea-core/)
  - Panacea Light Demon Client : [here](https://medibloc.gitbook.io/panacea-core/guide/clients)
  
## Installation
### Check-up before setup
  - Panacea LCD check 
```sh
# To chek panacead status
$ panaceacli status

# To check LCD status
$ curl http//127.0.0.1:1317/node_info
# or,
$ curl http//{IP_address of LCD}:{port}/node_info
```
### Installation
  - move to your project dir
```sh
$ cd {your project dir}
```
  - clone this repo
```sh
$ git clone https://github.com/Paul-Kim/panacea-python.git
$ cd panacea-python
$ pip install -r requirment.txt
$ cd ..  # back to your project directory
```

```python
import panacea
```

### How to use
Please see the official docs [here](https://panacea-python.readthedocs.io/en/latest/)
