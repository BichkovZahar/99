#теорія Декоратори
def my_decorator_func(func): #крок №3
    def wrapper():    #4
        print("+" * len('Hello!'))
        func()
        print("+" * len('Hello!'))
    return wrapper
@my_decorator_func #крок №2
def say_hello():
    print('Hello!') #крок №1
say_hello()

#########################################################

#задержка времени
import time
def delay_decorator(func):   #3
    def wrapper(*args , **kwargs):   #4
        time.sleep(3)
        return func(*args , **kwargs)
    return wrapper


@delay_decorator   #2
def sleepy():
    print('Я сплю')   #1
sleepy()

#########################################################
def cache_dekorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n] , cache
    return wrapper

@cache_dekorator
def fibonacci(n): #числа фібоначі
    if n in (0 , 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(10))
