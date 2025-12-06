#!/usr/bin/env python3
import time, base64
print("RED BUTTON PRESSED — simulated revocation")
print(base64.b64encode(f"REVOCATION {time.time()}".encode()).decode())
