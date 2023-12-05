# Linters output (before refactoring)

## flake8:
```bash
./hw1/utils.py:1:1: F401 'numpy as np' imported but unused
./hw1/main.py:5:19: F541 f-string is missing placeholders
./hw1/main.py:6:5: F841 local variable 'x' is assigned to but never used
```

## pylint:
```bash
************* Module hw1.utils
hw1/utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)
hw1/utils.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
hw1/utils.py:6:4: C0103: Variable name "df" doesn't conform to snake_case naming style (invalid-name)
hw1/utils.py:10:0: C0103: Argument name "df" doesn't conform to snake_case naming style (invalid-name)
hw1/utils.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
hw1/utils.py:1:0: W0611: Unused numpy imported as np (unused-import)
************* Module hw1.main
hw1/main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
hw1/main.py:1:0: E0401: Unable to import 'utils' (import-error)
hw1/main.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
hw1/main.py:5:4: C0103: Variable name "df" doesn't conform to snake_case naming style (invalid-name)
hw1/main.py:5:18: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
hw1/main.py:6:4: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
hw1/main.py:6:4: W0612: Unused variable 'x' (unused-variable)
```

# Linters output (after refactoring)

## flake8:
```bash
```

## pylint:
```bash
************* Module hw1.main
hw1/main.py:3:0: E0401: Unable to import 'utils' (import-error)

------------------------------------------------------------------
Your code has been rated at 6.15/10 (previous run: -1.33/10, +7.48)
```

false-positive error in pylint