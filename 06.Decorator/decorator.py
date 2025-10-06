# decorator


# Multiple Decorator Calls
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello Sally"


@changecase
def otherfunction():
    return "I am speed!"


print(myfunction())
print(otherfunction())


# Arguments in the Decorated Function
def changecase(func):
    def myinner(x):
        return func(x).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))


# *args and **kwargs
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))


# Decorator With Arguments
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a

        return myinner

    return changecase


@changecase(1)
def myfunction():
    return "Hello Linus"


print(myfunction())


# Multiple Decorators
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"

    return myinner


@changecase
@addgreeting
def myfunction():
    return "Tobias"


print(myfunction())


# Preserving Function Metadata
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)


def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)


# Import functools.wraps to preserve the original function name and docstring.

import functools


def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Have a great day!"


print(myfunction.__name__)
