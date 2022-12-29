from brownie import accounts, network, SimpleStorage

def get_account():
    current_network = network.show_active()
    if current_network == "development":
        account = accounts[0]
    elif current_network == "goerli":
        account = accounts.load("GOERLI_ACCOUNT1")
    else:
        raise Exception("Please give correct network")
    return account

def deploy_simple_storage():
    account = get_account()

    simple_storage = SimpleStorage.deploy({"from": account})

    transaction = simple_storage.store("Alice", 16, {"from": account})
    transaction.wait(1)

    AliceAge = simple_storage.retrieve("Alice")
    print(AliceAge)

def main():
    deploy_simple_storage()