# -*- coding: utf-8 -*-
import s2


print(dir(s2))
# ['EMAIL', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
for key in dir(s2):
    if key.isupper():
        s = getattr(s2, key)

print(s)


