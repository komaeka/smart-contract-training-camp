from brownie import network, accounts, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 100000000000

def get_account():
    current_network = network.show_active()
    if current_network == "localchain":
        account = accounts[0]
    else:
        raise Exception("Please give correct network")
    return account

def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})