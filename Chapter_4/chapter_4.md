# Functions and Modules
## Introduction
- For Code reuse and modularity, we use functions and modules.
- Break large chunks of code into smaller ones.


> Standard Library - os()
>> Module() - os()
>>> Functions() - getcwd()

- Keywords - `def` and `return`.
    - `def` - names the function and details and arguments
    - `return` - optional. Is used to pass back a value to the code that invoked this.

- Functions can accept argument data.
    - specify list of arguments within () after function name.
    - e.g.: `test_func(x,y)`

- Functions contain the code and documentation.
    - Code is always indented one level below `def`
    - Comments can be added as single using `#` or a docstrings using triple quotes.
    - When a function is a part of a Python Class, it is called a Method.

- Function Annotation are used to document the type of your function's argument and return type.

```python
def test_func(optional_arguments:str) -> set:
    """Documentation String"""
    #Your Function's Code Goes Here.
    return optional_value
```

