from brownie import accounts, SimpleStorage

def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve("Alice")
    expected = 0
    # Assert
    assert expected == starting_value

def test_updating_storage():
    # Arrage
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    simple_storage.store("Alice", 16, {"from": account})
    expected = 16
    # Assert
    assert expected == simple_storage.retrieve("Alice")