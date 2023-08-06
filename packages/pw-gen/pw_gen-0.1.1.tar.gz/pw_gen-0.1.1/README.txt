A library for generating secure randomised passwords.


Usage (Simple password):
------------------------
from pw_gen import Simple

var = Simple(20)

print(var.generate())

print(var.result())

Usage (Complex password):
-------------------------
from pw_gen import Complex

var = Complex(20, 'both', include_numbers=True, include_special_chars=False)

print(var.generate())

print(var.result())

Usage (Memorable password):
---------------------------
from pw_gen import Memorable

var = Memorable(True)

print(var.generate())

print(var.result())
