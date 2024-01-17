n=int(input())
prime=[]
sophie_germain_prime=[]
for i in range (2,2*n+2):
    for p in prime:
        if (i % p == 0):
            break;
    else:
        prime.append(i)
for m in range (2,n+1):
    k = 2*m+1
    if m in prime:
        if k in prime:
            sophie_germain_prime.append(m)
print(sophie_germain_prime)
