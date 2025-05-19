"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(x: float, y: float) -> float:
    "Multiplication function $f(x, y) = x * y$"
    return x * y

def id(x: float) -> float:
    "Identity function $f(x) = x$"
    return x

def add(x: float, y: float) -> float:
    "Addition function $f(x, y) = x + y$"
    return x + y

def neg(x: float) -> float:
    "Negation function $f(x) = -x$"
    return -x

def lt(x: float, y: float) -> float:
    "Less than function $f(x) =$ 1.0 if x is less than y else 0.0"
    return 1.0 if x < y else 0.0

def eq(x: float, y: float) -> float:
    "Is equal function $f(x) =$ 1.0 if x is equal to y else 0.0"
    return 1.0 if x == y else 0.0

def max(x: float, y: float) -> float:
    "Maximum function $f(x) =$ x if x is greater than y else y"
    return x if x > y else y

def is_close(x: float, y: float) -> float:
    "Return 1.0 if x is within 1e-2 of y else 0.0"
    return 1.0 if abs(x - y) < 1e-2 else 0.0

def sigmoid(x: float) -> float:
    "Sigmoid function $f(x) =  \frac{1.0}{(1.0 + e^{-x})})}$"
    return 1.0 / (1.0 + math.exp(-x))

def relu(x: float) -> float:
    "ReLU function $f(x) =$ x if x is greater than 0, else 0"
    return x if x > 0 else 0.0

def log(x: float) -> float:
    "Implements a function that computes the logarithm of x."
    return math.log(x)

def exp(x: float) -> float:
    "Implements a function that computes the exponential function $e^x$."
    return math.exp(x)

def inv(x: float) -> float:
    "Implements a function that computes the inverse $1 / x$ of x."
    return 1.0 / x

def log_back(x: float, d: float) -> float:
    r"If $f = log$ as above, compute $d \times f'(x)$"
    return d * (1.0 / x)

def inv_back(x: float, d: float) -> float:
    r"If $f(x) = 1.0 / x$ compute $d \times f'(x)$"
    return -d * (1.0 / x**2)

def relu_back(x: float, d: float) -> float:
    r"If $f = relu$ compute $d \times f'(x)$"
    return d if x > 0 else 0.0

# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(fn: Callable[[float], float], xs: list[float]) -> list[float]:
    "Apply the function fn to each element of the input list xs."
    return [fn(x) for x in xs]

def zipWith(fn: Callable[[float, float], float], xs: list[float], ys: list[float]) -> list[float]:
    "Zip together two lists and apply the function fn to each paired element."
    return [fn(x, y) for x, y in zip(xs, ys)]

def reduce(fn: Callable[[float, float], float], xs: list[float], start: float) -> float:
    "Reduce the input list xs by applying the function fn to elements."
    result = start
    for x in xs:
        result = fn(result, x)
    return result

def negList(xs: list[float]) -> list[float]:
    "Use :func:`map` and :func:`neg` to negate each element in `xs`"
    return map(neg, xs)

def addLists(xs: list[float], ys: list[float]) -> list[float]:
    "Add the elements of `xs` and `ys` using :func:`zipWith` and :func:`add`"
    return zipWith(add, xs, ys)

def sum(xs: list[float]) -> float:
    "Sum the elements in `xs` using :func:`reduce` and :func:`add`."
    return reduce(add, xs, 0)

def prod(xs: list[float]) -> float:
    "Product the elements in `xs` using :func:`reduce` and :func:`mul`."
    return reduce(mul, xs, 1)

# TODO: Implement for Task 0.3.
