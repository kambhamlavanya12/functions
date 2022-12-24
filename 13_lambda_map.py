#lambda that returns squares
# list1 = [1, 2, 3, 4, 5]
# print(list1 * 2)

# a = [1, 2, 3, 4, 5]
# r=[item * 3 for item in a]
# print(r)

list1=[int(x) for x in input().split()]
list2 = list(map(lambda x: x**2, list1))
print(list2)