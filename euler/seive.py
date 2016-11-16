from math import sqrt

def eratosthenes(n):
    a=dict.fromkeys(range(2,n+1), True)

    for i in range(2,int(sqrt(n))):
        if a[i]:
            for j in [i**2+k*i for k in range(int((n-i**2)/i+1))]:
                a[j]=False
    return [k for k,v in a.items() if v]

if __name__=='__main__':
  print(eratosthenes(1000000))
