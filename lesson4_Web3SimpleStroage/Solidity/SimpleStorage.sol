// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {
    mapping(string => uint256) nameToAge;

    function store(string memory _name, uint256 _age) public {
        nameToAge[_name] = _age;
    }

    function retrieve(string memory _name) public view returns (uint256) {
        return nameToAge[_name];
    }
}
