# 람다함수에 관한 내용.

plus_two = lambda x : x+2
print(plus_two(4))

a = [1,2,3]
print(list(map(plus_two,a)))
print(list(map(lambda x : x+2,a)))

