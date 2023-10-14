string=input()
matching=input()
m=0
n=len(matching)
sum1=0
final=0

for i in range(len(string)-len(matching)+1):
    # print(i)
    # print(f"m1={m}")
    # print(f"n1={n}")
    if string[m:n]==matching:
        # print(string[m:n])
        final=sum1+1
        sum1=final
    m=m+1
    # print(f"m={m}")
    n=n+1
    # print(f"n={n}")
print(final)
