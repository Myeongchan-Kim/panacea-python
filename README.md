# panacea-python
Python library to use panancea (panacea git repository: https://github.com/medibloc/panacea-core)


## Requirment 
  - Go 1.12++
  - Panacea-core : [here](https://medibloc.gitbook.io/panacea-core/).
  - Panacea Light Demon Client : [here](https://medibloc.gitbook.io/panacea-core/guide/clients).
  
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
```

```python
import panacea
```
