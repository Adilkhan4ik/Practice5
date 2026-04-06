def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) would raise StopIteration


def square_numbers(n):
    for i in range(1, n+1):
        yield i * i

for sq in square_numbers(5):
    print(sq)  # 1 4 9 16 25



def infinite_count():
    n = 1
    while True:
        yield n
        n += 1

count = infinite_count()
print(next(count))  # 1
print(next(count))  # 2
print(next(count))  # 3


squares = (x*x for x in range(1, 6))
for sq in squares:
    print(sq)  # 1 4 9 16 25



def read_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# for line in read_file("bigfile.txt"):
#     print(line)