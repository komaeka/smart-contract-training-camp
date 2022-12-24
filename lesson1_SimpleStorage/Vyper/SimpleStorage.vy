# SPDX-License-Identifier: MIT
# @version ^0.3.0

nameToAge: HashMap[String[20],uint256]

@external
def store(_name: String[20], _age: uint256):
    self.nameToAge[_name] = _age

@view
@external
def retrieve(_name: String[20]) -> uint256:
    return self.nameToAge[_name]