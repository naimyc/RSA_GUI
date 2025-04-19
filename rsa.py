import time
from RSA_Algo import *

start = time.time()
public_key, private_key = generate()
gen_time = time.time()
cypher_text = encrypt("Hello", public_key)
encrypt_time = time.time()

message = decrypt(cypher_text, private_key)
decrypt_time = time.time()

sig = sign(message, private_key)
sign_time = time.time()

isValid = verify(message, sig, public_key)
end_time = time.time()

print("Zeit für Schlüsselerzeugung:", round(gen_time - start, 2), "Sekunden")
print("Zeit für Verschlüsselung:", round(encrypt_time - gen_time, 2), "Sekunden")
print("Zeit für Entschlüsselung:", round(decrypt_time - encrypt_time, 2), "Sekunden")
print("Zeit für Signieren:", round(sign_time - decrypt_time, 2), "Sekunden")
print("Zeit für Verifikation:", round(end_time - sign_time, 2), "Sekunden")
print("Gesamtlaufzeit:", round(end_time - start, 2), "Sekunden")