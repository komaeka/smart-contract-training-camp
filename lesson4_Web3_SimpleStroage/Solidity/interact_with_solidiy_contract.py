import json
from web3 import Web3
import os

with open("./compiledSolidity.json", "r") as file:
    compiled_sol = json.loads(file.read())

abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Ganache
w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))
chain_id = 1337
my_address = "0xD7F441fa244AC8b61854106C43EfE7AeC9fcEa86"
private_key = os.environ.get("GANACHE_KEY1")
contract_address = "0x4F7ABE0Ca67dAE8b56799e8B658e3c181F6EEf28"

# Goerli
# infura_key = os.environ.get("WEB3_INFURA_PROJECT_ID")
# infura_url = "https://goerli.infura.io/v3/" + infura_key
# w3 = Web3(Web3.HTTPProvider(infura_url))
# chain_id = 5
# my_address = "0x96d3Ad47B88aF44F0Dc2C07e42e6B8b8ce4313bf"
# private_key = os.environ.get("GOERLI_KEY1")
# contract_address = "0xd00d8bAa8c437Fb5d522C7cfF5C42559ae4596b8"

nonce = w3.eth.getTransactionCount(my_address)

contract = w3.eth.contract(address=contract_address, abi=abi)

# 与合约交互可以使用call或者transaction 
# call：仅能获取区块链中的信息，不能改变状态，相当于Remix中的蓝色按钮
# transaction ：可以改变区块链中的状态，相当于Remix中的橙色按钮

def store(name, age):
    greeting_transaction = contract.functions.store(name, age).buildTransaction(
        {
            "chainId": chain_id,
            "from": my_address,
            "nonce": nonce,
            "gasPrice": w3.eth.gas_price
        }
    )

    signed_greeting_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=private_key
    )

    tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)

    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

store("Alice", 16)
print(contract.functions.retrieve("Alice").call())
