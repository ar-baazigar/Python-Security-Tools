hacker_greeting.py :-
1 Variables: Like alias and server_number. These are "buckets" in the computer's memory that hold information.
2. The input() Function: How to let a user talk to your program.
3. F-Strings: That f"..." trick. It’s the most modern way to "inject" variables into a sentence.

port_scanner_v1.py
1. Python Syntax & Logic
Variables: Storing text (strings) and whole numbers (integers).
Type Casting: Using int() to turn user text into numbers so the computer can do math or loops.
F-Strings: Formatting output professionally (e.g., f"Port {port} is OPEN").
2. Networking Foundations
The Socket Library: The "bridge" between Python and the network.
IP Addresses: Specifically 127.0.0.1 (the "Home" address) for safe testing.
Ports: Understanding them as "digital doors" (like 80 for Web and 135 for Windows RPC).
3. Automation & File Handling
For Loops: Repeating a task (like scanning) 1,000 times with just two lines of code.
File Modes: Using "w" to write a fresh report and "a" to add to an existing one.

learning_notes.md :-
1. String Methods
len(): A built-in function to count characters in a string (e.g., "hacker" is 6).
.isdigit(): A method used to check if a specific character is a number.
2. Advanced Logic
any(): This function is a "Hacker's Shortcut." It checks a whole list of characters and returns True if even one of them matches your criteria (like being a digit).
Logical and: Used when both conditions must be met for a result (e.g., Length must be 12+ AND have a number).
Logical not: Used to check if something is missing (e.g., if not has_number).
3. Conditional Flow (if, elif, else)
if: The first check.
elif: Short for "else if"—it allows you to check multiple specific categories (Weak, Medium, Strong) in order.
else: The "Catch-all" for anything that didn't match the previous checks.
4. and: Returns True only if EVERY check passes.
or: Returns True if AT LEAST ONE check passes.
5. The in keyword: Used to see if a character belongs to a specific group (like our symbols string).

03_crypto_fetcher.py:-
1. The requests Library
Purpose: Allows Python to send HTTP requests (GET, POST) just like a web browser.
response.json(): Converts the "string" of data from a website into a Python Dictionary so we can easily pick out specific info (like the price of Bitcoin).

2. HTTP Status Codes
200 OK: Request successful.
403 Forbidden: Access denied by the server.
404 Not Found: The page or API endpoint doesn't exist.

3. Data Structures: Dictionaries
We used data['bitcoin']['usd']. This is how Python navigates "Key-Value" pairs—it's like looking up a word in a real dictionary to find its definition.