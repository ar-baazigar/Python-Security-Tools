# --- PASSWORD STRENGTH ANALYZER v3.0 ---

symbols = "!@#$%^&*"
password = input("[?] Enter password to test: ")

# 1. THE CHECKS
length_ok = len(password) >= 12
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in symbols for char in password)

# 2. THE RATING SYSTEM
if length_ok and has_digit and has_symbol:
    print("[+] Status: ELITE SECURITY")
elif (length_ok or has_digit) and has_symbol:
    print("[!] Status: STRONG")
elif length_ok:
    print("[!] Status: MEDIUM (Needs numbers/symbols)")
else:
    print("[!] Status: WEAK")