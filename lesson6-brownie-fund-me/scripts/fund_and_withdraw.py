from brownie import FundMe
from scripts.helpful_scripts import get_account

ENTRANCE_FEE = 1000000000000000

def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrance_fee = ENTRANCE_FEE
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)

def main():
    fund()
    withdraw()
