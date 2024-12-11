# like we have many build in module like 
# sys, math, random, date time, os, platfrom

# platfrom 

import platform

platform_Name = platform.system()
print(platform_Name) # -> Windows

python_version = platform.python_version()
print(python_version) # -> 3.12.6

processor_Name = platform.processor()
print(processor_Name) # -> Intel64 Family 6 Model 151 Stepping 2, GenuineIntel


# Built-in Function :-

# We have a lot of build in functions in python. 
# In the following example, we used 
# build-in function dir().

import math
import random
print(dir(random))
