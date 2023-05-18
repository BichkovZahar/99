#інтератор
lst = [1 , 2 , 3 , 4 , 5 , 6]
print(iter(lst))

class MyIterator:
    def __init__(self , data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
my_list = [1 , 2 , 3 , 4 , 5 , 6]
my_iter = MyIterator(my_list)
for num in my_iter:
    print(num)


