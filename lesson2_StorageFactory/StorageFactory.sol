// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./SimpleStorage.sol";

contract StorageFactory is SimpleStorage {
    SimpleStorage[] simpleStorageArray;

    function createSimpleStorageContract() public {
        simpleStorageArray.push(new SimpleStorage());
    }

    function sfStore(uint256 simpleStorageIndex, uint256 simpleStorageNumber)
        public
    {
        simpleStorageArray[simpleStorageIndex].store(simpleStorageNumber);
    }

    function sfGet(uint256 simpleStorageIndex) public view returns (uint256) {
        return simpleStorageArray[simpleStorageIndex].retrieve();
    }
}
