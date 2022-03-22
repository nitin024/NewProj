from pathlib import Path

for path in Path("X:\\Felix\\Prod\\Assembler").glob("_IXA01*"):
    print(path)

for path in Path("X:\\Felix\\Prod\\Bms").glob("_IXA01*"):
    print(path)    
