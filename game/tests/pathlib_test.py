from pathlib import Path

DATA = Path(__file__).parent.parent.parent / "data"

print(str(DATA))

for path in DATA.rglob("*.png"):

    print(str(path.relative_to(DATA)))

for i in range(50):
    print('-', end = '')

for path in DATA.rglob("*.png"):
    print(str(path.relative_to(DATA)))