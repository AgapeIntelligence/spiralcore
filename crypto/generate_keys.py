#!/usr/bin/env python3
from cryptography.hazmat.primitives.asymmetric import ed25519
import base64
priv = ed25519.Ed25519PrivateKey.generate()
pub = priv.public_key()
print("Demo private key →", base64.b64encode(priv.private_bytes_raw()).decode())
print("Demo public key  →", base64.b64encode(pub.public_bytes_raw()).decode())
