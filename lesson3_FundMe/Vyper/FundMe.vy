# SPDX-License-Identifier: MIT
# @version ^0.3.0

import interfaces.AggregatorV3Interface as AggregatorV3Interface

addressToAmountFunded: public(HashMap[address, uint256])
owner: public(address)
funders: public(DynArray[address,10])

@external
def __init__():
    self.owner = msg.sender

# @payable
# @external
# def fund():
#     minimumUSD: uint256 = 1 * 10**8
#     assert self.getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!"
#     self.addressToAmountFunded[msg.sender] += msg.value
#     self.funders.append(msg.sender)

@view
@external
def getPrice() -> uint256:
    priceFeed: AggregatorV3Interface = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e)
    a: uint80 = 0
    price: int256 = 0
    b: uint256 = 0
    c: uint256 = 0
    d: uint80 = 0
    (a, price, b, c, d) = priceFeed.latestRoundData()
    return convert(price,uint256)

# @view
# @external
# def getConversionRate(ethAmount: uint256) -> uint256:
#     ethPrice: uint256 = self.getPrice()
#     ethAmountInUsd: uint256 = (ethPrice * ethAmount) / 1000000000000000000
#     return ethAmountInUsd

# @payable
# @external
# def withdraw():
#     assert msg.sender == self.owner, "You are not owner!"
#     send(msg.sender,self.balance)
#     # fundersLength: uint8 = convert(len(self.funders), uint8)
#     for funderIndex in range(10):
#         if funderIndex < len(self.funders):
#             funder: address = self.funders[funderIndex]
#             self.addressToAmountFunded[funder] = 0
#         else:
#             break
#     self.funders = []