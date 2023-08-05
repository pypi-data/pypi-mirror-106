import numpy as np

def say_hello(name=None):
    if name is None:
        return "Hello, world!"
    else:
        return f"Hello, {name}!"