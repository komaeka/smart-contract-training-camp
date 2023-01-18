# SPDX-License-Identifier: MIT
# @version ^0.3.0

from . import SimpleStorage

simpleStorageArray: DynArray[SimpleStorage,10]

@external
def createSimpleStorageContract(addr: address):
   self.simpleStorageArray.append(SimpleStorage(addr))

@external
def sfStore(simpleStorageIndex: uint256,simpleStorageNumber: uint256):
   self.simpleStorageArray[simpleStorageIndex].store(simpleStorageNumber)

@view
@external
def sfGet(simpleStorageIndex: uint256) -> uint256:
   return self.simpleStorageArray[simpleStorageIndex].retrieve()