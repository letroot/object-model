"""Inspect types"""
import string

objects = [42, "typo", 51.0, [1, 2, 3], (1, 2, 3), string]

# Everything in python is an object with a type and an id
for obj in objects:
    print(obj, '|', type(obj), '|', id(obj))
    print('-' * 30)


# modules are objects
# functions are objects
# classes are objects (more on this)
