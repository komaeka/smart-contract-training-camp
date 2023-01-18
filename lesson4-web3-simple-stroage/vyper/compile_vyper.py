from vyper import compiler
import json

with open("SimpleStorage.vy", "r") as file:
    simple_storage_source = file.read()

compiled_vy = compiler.compile_code(contract_source=simple_storage_source,output_formats=["abi","bytecode"])

with open("compiledVyper.json", "w") as file:
    json.dump(compiled_vy, file)