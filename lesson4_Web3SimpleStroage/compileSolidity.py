from solcx import compile_standard, install_solc

with open("SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

install_solc("0.8.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode"]}
            }
        },
    },
    # solc_version="0.8.0"
)

print(compiled_sol)