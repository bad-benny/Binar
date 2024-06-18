# Introduction
Binar a program you can use to convert analog signals into digital signals.
# Name Orgin
Originated from the name ben then got changed to Binar.
# Use 
Can be used with the raspberry pi for analog conversion.
# How to
To use it pip install the repo into your python environment then import the class and there you have it.
``` python
from binar import Binar

a = int(input("Enter a number: \n"))
binar_a = Binar(a)
print(f"Analog signal: {a}, Digital signal: {binar_a.result}")
```