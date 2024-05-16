#Prcatice

def sumofdigits(n):
    assert n>=0 and int(n)==n, "N should be positive and integer"
    if n == 0:
        return n
    else:
        return n + sumofdigits(n-1)
    
print(sumofdigits(10))

def sumofnumbers(n):
    assert n>=0 and int(n)==n, "N should be positive and integer"
    if n == 0:
        return n
    else:
        return n%10 + sumofnumbers(n//10)

print(sumofnumbers(119))

def power(base,pow):
    assert int(pow)==pow ; "Pow should be integer"
    if pow == 0:
        return 1
    elif pow < 0:
        return 1/base*power(base,pow+1)
    else:
        return base*power(base,pow-1)

print(power(2,-2))


def gcd(a,b):
    assert int(a)==a and int(b)==b, "A and B should be integers"
    if a<0:
        a = a*-1
    if b<0:
        b = b*-1
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,-18))

def bintodec(n):
    if n//2==0:
        return n
    else:
        return (bintodec(n//2))*10 + (n%2)
    
print(bintodec(10))
