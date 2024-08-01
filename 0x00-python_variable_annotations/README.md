
---

# 0x00. Python - Variable Annotations

## Project Overview

This project focuses on mastering type annotations in Python, a key aspect of writing robust and maintainable code. It introduces concepts such as basic annotations, complex types, and function annotations, with an emphasis on using type hints to improve code clarity and validation.

## Curriculum

### Short Specializations

- **Average Completion**: 101.41%

## Learning Objectives

By the end of this project, you should be able to:

- Explain type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand duck typing and its role in Python.
- Validate your code with MyPy for type checking.

## Resources

- **Python 3 Typing Documentation**: Official Python documentation on type hints and annotations.
- **MyPy Cheat Sheet**: A quick reference for MyPy usage and type annotations.

## Requirements

- **Allowed Editors**: vi, vim, emacs
- **Environment**: All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- **File Endings**: All files should end with a new line.
- **Shebang**: The first line of all files should be `#!/usr/bin/env python3`.
- **Code Style**: Adhere to PyCodeStyle version 2.5.
- **Executable Files**: All files must be executable.
- **Documentation**: Every module, class, and function must have proper documentation.

## Tasks

### 0. Basic Annotations - `add`

**Objective**: Write a type-annotated function `add` that takes two floats and returns their sum as a float.

**File**: `0-add.py`

```python
def add(a: float, b: float) -> float:
    return a + b
```

### 1. Basic Annotations - `concat`

**Objective**: Write a type-annotated function `concat` that takes two strings and returns their concatenation.

**File**: `1-concat.py`

```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

### 2. Basic Annotations - `floor`

**Objective**: Write a type-annotated function `floor` that takes a float and returns its floor value as an integer.

**File**: `2-floor.py`

```python
import math

def floor(n: float) -> int:
    return math.floor(n)
```

### 3. Basic Annotations - `to_str`

**Objective**: Write a type-annotated function `to_str` that takes a float and returns its string representation.

**File**: `3-to_str.py`

```python
def to_str(n: float) -> str:
    return str(n)
```

### 4. Define Variables

**Objective**: Define and annotate the following variables with specified values: `a` (int), `pi` (float), `i_understand_annotations` (bool), `school` (str).

**File**: `4-define_variables.py`

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### 5. Complex Types - List of Floats

**Objective**: Write a type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

**File**: `5-sum_list.py`

```python
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

### 6. Complex Types - Mixed List

**Objective**: Write a type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

**File**: `6-sum_mixed_list.py`

```python
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
```

### 7. Complex Types - String and Int/Float to Tuple

**Objective**: Write a type-annotated function `to_kv` that takes a string and an int or float and returns a tuple. The first element is the string and the second is the square of the int/float, annotated as a float.

**File**: `7-to_kv.py`

```python
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v * v))
```

### 8. Complex Types - Functions

**Objective**: Write a type-annotated function `make_multiplier` that takes a float and returns a function that multiplies a float by the given multiplier.

**File**: `8-make_multiplier.py`

```python
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
```

### 9. Let's Duck Type an Iterable Object

**Objective**: Annotate the `element_length` function to specify that it takes an iterable of sequences and returns a list of tuples containing a sequence and its length.

**File**: `9-element_length.py`

```python
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

## Contributing

Feel free to fork the repository and submit pull requests. Ensure your code adheres to the style guidelines and includes comprehensive documentation.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

