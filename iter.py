numbers = [1, 2, 3, 4]
it = iter(numbers)   # create iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
# next(it) would raise StopIteration


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:   # automatically uses iterator
    print(fruit)


class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num <= 5:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

numbers = MyNumbers()
for n in numbers:
    print(n)



def countdown():
    n = 5
    while n > 0:
        yield n
        n -= 1

for num in countdown():
    print(num)
    

colors = ["red", "green", "blue"]
it = iter(colors)

print(next(it, "End"))  # red
print(next(it, "End"))  # green
print(next(it, "End"))  # blue
print(next(it, "End"))  # End (no error)