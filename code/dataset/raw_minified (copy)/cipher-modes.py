from cryptography.hazmat.primitives.ciphers.modes import CBC,ECB
A=ECB(iv)
B=AES.new(key,blockalgo.MODE_CTR,iv)
A=CBC(iv)