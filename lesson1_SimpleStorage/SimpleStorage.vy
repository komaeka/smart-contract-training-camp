nameToAge: HashMap[String[20],uint256]

@external
def store(_name: String[20], _age: uint256):
    self.nameToAge[_name] = _age

@external
@view
def retrieve(_name: String[20]) -> uint256:
    return self.nameToAge[_name]