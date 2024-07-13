print("Введите n:")
n = int(input())

i=sum=0
for i in range(n):
    i+=1
    num = i**3
    sum += num

print(sum)
# 5. По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.