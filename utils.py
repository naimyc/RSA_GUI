from random import randint

def gcd(a, b):
    # Berechnet den größten gemeinsamen Teiler (ggT) von a und b
    
    while b:
        a, b = b, a % b
    return a

# Erw. Euklidischer Algorithmus
def egcd(a, b):
    # Liefert dem ggT und die Koeffizienten x und y, sodass a*x + b*y = ggT(a, b)
    # Wird verwendet zur Berechnung des modularen Inversen
    
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    #  Berechnet das modulare Inverse von a modulo m, also a^-1 mod m.
    #  Gesucht ist x, sodass: (a * x) mod m = 1
    #  Wird verwendet zur Berechnung des privaten RSA-Schlüssels d.
    
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Kein modulares Inverses")
    return x % m

def MillerRabin(p):
    # Miller-Rabin Primalitätstest (probabilistisch).
    # → Testet, ob p wahrscheinlich eine Primzahl ist.
    # → Wird verwendet zur schnellen Generierung großer Primzahlen in der Kryptografie.
    
    # Hintergrund:
    # Jeder Primzahl p > 2 lässt sich als p - 1 = 2^r * d mit ungeradem d schreiben.
    # Der Test prüft für zufälliges a, ob a^d mod p entweder 1 oder -1 ist.
    # Falls nicht, wird mehrfach quadriert, um -1 zu erreichen. Sonst ist p zusammengesetzt.
   
    d = p - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
        
    a = randint(2, p-1)
    x = pow(a, d, p)
    
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
    # Generiert eine große Primzahl
    # Versucht Zufallszahlen im Bereich [bits // 2, bits], bis der Miller-Rabin-Test sie akzeptiert.
    # Wird bei RSA zur Erzeugung der Primzahlen p und q verwendet.
    
    while True:
        candidate = randint(2**(bits - 1), 2**bits - 1)  # Zufallszahl im Bereich [2^(bits-1), 2^bits - 1]
        if MillerRabin(candidate):
            return candidate
        
def hash(msg, n):
    # Sehr einfache Hashfunktion für kleine Beispiele.
    # Handelt Nachricht in Bytearray um und summiert alle Bytewerte.
    # Modulo n reduziert, damit der Wert im RSA-Bereich liegt.
    
    return sum(bytearray(msg, 'utf-8')) % n