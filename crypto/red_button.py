#!/usr/bin/env python3
from cryptography.hazmat.primitives.asymmetric import ed25519
import base64, time, sys

priv = ed25519.Ed25519PrivateKey.from_private_bytes(base64.b64decode(input("Your private key (base64): ")))
msg = f"REVOCATION {time.time()}".encode()
sig = base64.b64encode(priv.sign(msg)).decode()

print("\nRED BUTTON PRESSED")
print("Broadcast this signature everywhere:")
print(sig)
open("participants/revocation.sig","w").write(sig)
sys.exit(0)
