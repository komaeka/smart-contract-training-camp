from vyper import compiler

with open("SimpleStorage.vy", "r") as file:
    simple_storage_file = file.read()

compiled_vy = compiler.compile_code(contract_source=simple_storage_file,output_formats=["abi","bytecode"])
print(compiled_vy)