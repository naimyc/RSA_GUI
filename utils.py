from random import randint

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Kein modulares Inverses")
    return x % m

def MillerRabin(p):
    d = p - 1
    r = 0
    
    while d % 2 == 0:
        d //= 2
        r += 1
        
    a = randint(2, p-1)
    x = (a ** d) % p
    
    if x == 1 or x == p -1:
        return True
    
    while r > 1:
        x = (x ** 2) % p
        if x == 1:
            return False
        if x == p - 1:
            return True
        
        r -= 1
    return False

def generate_large_prime(bits):
    while True:
        candidate = randint(bits // 2, bits)
        if MillerRabin(candidate):
            return candidate
        
def hash(msg, n):
    return sum(bytearray(msg, 'utf-8')) % n