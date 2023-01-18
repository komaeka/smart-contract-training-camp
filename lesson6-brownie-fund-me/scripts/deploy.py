from brownie import FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks

def deploy_fund_me():
    account = get_account()
    deploy_mocks()
    price_feed_address = MockV3Aggregator[-1].address
    FundMe.deploy(price_feed_address, {"from": account})

def main():
    deploy_fund_me()