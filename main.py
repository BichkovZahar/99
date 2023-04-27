#теорія
'''
def blak_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)
blak_hole(2341 , "Earth" , 'rusnya')
'''
'''
def blak_hole_named(**kwargs):
    print(type(kwargs))
    for argument , value in kwargs.items():
        print(argument ,'=' , value)
blak_hole_named(name = 'Gleb' , planet = 'Earth' , number = 5)
'''
def blak_hole_named(*args , **kwargs):
    if not args: #для перевірки
        return 0
    for argument in args:
        print(argument)
    for key , value in kwargs.items():
        print(key ,'=' , value)
blak_hole_named( 2341, "Earth", 'rusnya' ,
                name = 'Gleb' , planet = 'Earth' , number = 5)
