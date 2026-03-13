#comparetriplets
a = list(map(int, input().split()))
b = list(map(int, input().split()))

alice = 0
bob = 0

for i in range(3):
    if a[i] > b[i]:
        alice += 1

    elif a[i] < b[i]:
        bob += 1

print(alice, bob)

#zip function
a = list(map(int, input().split()))
b = list(map(int, input().split()))

alice = sum(1 for x,y in zip(a,b) if x<y)
bob = sum(1 for x,y in zip(a,b) if x>y)
print(alice,bob)

number = int(input().strip())
data=list(map(int,input().split()))
addition=sum(data)
print(addition)

def averybigsum(a):
    return sum(a)
number=int(input())
data=list(map(int,input().split()))
print(averybigsum(data))

