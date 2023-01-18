import json
from web3 import Web3
import os

with open("compiledVyper.json", "r") as file:
    compiled_vy = json.loads(file.read())

# get abi
abi = compiled_vy["abi"]

# get bytecode
bytecode = compiled_vy["bytecode"]

# Ganache
w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
chain_id = 1337
my_address = "0xD7F441fa244AC8b61854106C43EfE7AeC9fcEa86"
private_key = os.environ.get("GANACHE_KEY1")

# Goerli
# infura_key = os.environ.get("WEB3_INFURA_PROJECT_ID")
# infura_url = "https://goerli.infura.io/v3/" + infura_key
# w3 = Web3(Web3.HTTPProvider(infura_url))
# chain_id = 5
# my_address = "0x96d3Ad47B88aF44F0Dc2C07e42e6B8b8ce4313bf"
# private_key = os.environ.get("GOERLI_KEY1")

# get the latestest transaction
nonce = w3.eth.getTransactionCount(my_address)

# create contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# 1.build a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
        "gasPrice": w3.eth.gas_price
    }
)

# 2.sign a transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 3.send a transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# 4.wait block confirmation
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)