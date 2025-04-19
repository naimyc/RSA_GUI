from utils import *

def generate(key_size = 1024):
    # P und Q Primzahlen => Ergeben durch * N -> p != q
    
    bit_length = key_size // 2  # => 512 Bit pro Primzahl
    p, q = generate_large_prime(bit_length), generate_large_prime(bit_length)
    while p == q: generate_large_prime(bit_length)
    
    N = p * q
    PHI_N = (p - 1) * (q - 1)
    
    e = randint(2, PHI_N -1)
    d = 2
    
    if gcd(e, PHI_N) != 1:
        while True:
            e = randint(3, PHI_N - 1)
            if gcd(e, PHI_N) == 1:
                break
    d = modinv(e, PHI_N)
    
    return [(e, N), (d, N)]

def encrypt(message, public_key):
    e, N = public_key
    cypher_block = [(ord(m) ** e) % N for m in message]
    return cypher_block

def decrypt(cypher_text, private_key):
    d, N = private_key
    message = ""
    for c in cypher_text:
        message += chr((c ** d) % N)
        
    return message

def sign(message, private_key):
    d, N = private_key
    
    hashed_message = hash(message, N)
    signature = (hashed_message ** d) % N
    return signature

def verify(message, signature, public_key):
    e, N = public_key
    message_hash = sum(bytearray(message, 'utf-8'))
    decrypted_hash = (signature ** e) % N
    return decrypted_hash == message_hash
    
public_key, private_key = generate()
cypher_text = encrypt("Hello", public_key)

message = decrypt(cypher_text, private_key)
sig = sign(message, private_key)
print(sig)
isValid = verify(message, sig, public_key)
print(isValid)
    