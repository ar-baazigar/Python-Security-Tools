import socket

# 1. Get user input
target = input("[+] Enter Target IP (e.g., 127.0.0.1): ")
start_p = int(input("[+] Start Port: "))
end_p = int(input("[+] End Port: "))
print(f"\n[*] Scanning {target}...")

#Open a file for writing ('w' means write mode)
with open("scan_results.txt", "w") as f:
    f.write(f"--- SCAN REPORT FOR {target} ---\n")
    
    for port in range(1, 150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[!] Found Open Port: {port}")
            # 2. Write the finding to the file
            f.write(f"Port {port} is OPEN\n")
        
        s.close()

print("\n[*] Results saved to scan_results.txt")