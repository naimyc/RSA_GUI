from utils import *

async def generate(key_size = 1024):
    # Generiert ein RSA Schlüsselpaar.
    # Args:
        # key_size (int): Die Die Bitlänge des Modulus N (Standard: 1024 Bit)
    
    # Returns:
        #  tupel [(e, N), (d, N)] mit Public Key und Private Key
    
    bit_length = key_size // 2  # Hälfte für jede Primzahl
    p, q = await generate_large_prime(bit_length), await generate_large_prime(bit_length)
    while p == q: await generate_large_prime(bit_length) # sicherstellen, dass p != q
    
    N = p * q           # Modulus
    PHI_N = (p - 1) * (q - 1) # Eulerschen Phi-Funktion
    e = randint(2, PHI_N -1)
    d = 2
    
    # Verschlüsselungsexponent e bestimmen mit 1 < e < PHI_N und ggT(e, PHI_N) = 1
    while gcd(e, PHI_N) != 1:
        e = randint(2, PHI_N - 1)
            
    # Private und Entschlüsselungsexponent d berechnen
    d = modinv(e, PHI_N)
    
    return [(e, N), (d, N)]

async def encrypt(message, public_key):
    # Verschlüsselt eine Nachricht mit dem öffentlichen Schlüssel
    
    # Args:
       # message (str): Die Klartextnachricht
       # public_key (tuple): (e, N)
    
    # Returns 
       # list[int]: Verschlüsselte Blöcke
       
    e, N = public_key
    cypher_block = [pow(ord(m), e, N) for m in message]
    return cypher_block

async def decrypt(cypher_text, private_key):
    # Entschlüsselt verschlüsselte Blöcke mit dem privaten Schlüssel
    
    # Args:
       # cypher_text (list[int]): Verschlüsselte Blöcke
       # private_key (tuple): (d, N)
    
    # Returns 
       # str: Entschlüsselte Klartextnachricht
       
    d, N = private_key
    message = ""
    for c in cypher_text:
        message += chr(pow(c, d, N))
        
    return message

async def sign(message, private_key):
    # Erstellt eine digitale Signatur der Nachricht.

    # Args:
    #     message (str): Die Nachricht
    #     private_key (tuple): (d, N)

    # Returns:
    #     int: Digitale Signatur
    
    d, N = private_key
    
    hashed_message = hash(message, N)
    signature = pow(hashed_message, d, N)
    return signature

async def verify(message, signature, public_key):
    # Überprüft eine digitale Signatur.
    
    # Args:
    #     message (str): Die ursprüngliche Nachricht
    #     signature (int): Die digitale Signatur
    #     public_key (tuple): (e, N)
    
    # Returns:
    #     bool: True, wenn die Signatur gültig ist, sonst False
    
    e, N = public_key
    
    message_hash = hash(message, N)
    decrypted_hash = pow(signature, e, N) 
    return decrypted_hash == message_hash
    