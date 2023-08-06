# WhirlCalc

Whirlcalc is an advanced python module with some different functions related to Maths and other computations

## Currently Whirlcalc is on version 2b0 (v2 beta)

# NOTE: This file will not be updated on pre-releases, this file gives v1.0.0 readme.

Binary to Decimal:
```
>>> import whirlcalc
>>> print(whirlcalc.binary2decimal(1010))
>>> 10
```

Decimal to Binary:
```
>>> import whirlcalc
>>> print(whirlcalc.decimal2binary('110001001'))
>>> 393
```

Factorial:
```
>>> import whirlcalc
>>> print(whirlcalc.factorial(5))
>>> 120
```

Evaluate:
```
>>> import whirlcalc
>>> print(whirlcalc.evaluate("2*3+100-190+factorial(3)-pi"))
>>> -81.1415926535898
```

valid functions:
```
whirlcalc.make_penguin()
whirlcalc.factorial(int)
whirlcalc.arithmetic_mean(list)
whirlcalc.decimal2binary(int)
whirlcalc.binary2decimal(int)
whirlcalc.hexadecimal2decimal(str)
whirlcalc.decimal2hexadecimal(int)
whirlcalc.octal2decimal(int)
whirlcalc.decimal2octal(int)
whirlcalc.evaluate(str)
```
NOTE: evaluate() only supports factorial() and pi.

Can I use it?
> Yeah! Of course! you can use it.. (Only if you are a cute penguin!)

and if you are not a penguin.. then.. try this:
```
>>> import whirlcalc
>>> whirlcalc.make_penguin()
```


CHANGELOG:
```
v2.0.0:
> added classes
  > decimal
  > binary
  > octal
  > hexadecimal

v1.0.0:
> added decimal2binary()
> added binary2decimal()
> added hexadecimal2decimal()
> added decimal2hexadecimal()
> added octal2decimal()
> added decimal2octal()
> improved make_penguin()
```