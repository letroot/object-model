"""Bypassing the class syntax"""

# so we've seen that classes are types too (user-defined types)
# so can we say that classes are objects (instances) of class type?

# can we create our own types?
# Yes, that's exactly what a class means
class Chronic:
    colour = "green"

leaf = Chronic()
print(type(leaf))
# guess...

# But can we do it another way?
# TODO
# print(type(ChronicClass))
# we just made a class without using the class keyword

# leafb = ChronicClass()
# print(type(leafb))
# print its colour
