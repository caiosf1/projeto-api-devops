import secrets

print(f"SECRET_KEY={secrets.token_hex(32)}")
print(f"JWT_SECRET_KEY={secrets.token_hex(32)}")
print(f"POSTGRES_PASSWORD={secrets.token_hex(16)}")
