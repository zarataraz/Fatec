n = int(input("numerinho :"))
mult = 0

for i in range (2,n):
    if (n % i == 0):
        print("multiplo de", i)
        mult+=1

if (mult==0):
    print("é primo")
else:
    print(("não é primo"))
