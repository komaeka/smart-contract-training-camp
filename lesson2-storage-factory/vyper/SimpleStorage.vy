# SPDX-License-Identifier: MIT
# @version ^0.3.0

favoriteNumber: uint256

@external
def store(_favoriteNumber: uint256):
    self.favoriteNumber = _favoriteNumber

@view
@external
def retrieve() -> uint256:
    return self.favoriteNumber