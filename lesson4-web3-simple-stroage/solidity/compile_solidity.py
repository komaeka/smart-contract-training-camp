import solcx
import json

with open("SimpleStorage.sol", "r") as file:
    simple_storage_source = file.read()

solcx.install_solc("0.8.0")

compiled_sol = solcx.compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_source}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "evm.bytecode"]}
            }
        }
    }
)

with open("compiledSolidity.json", "w") as file:
    json.dump(compiled_sol, file)