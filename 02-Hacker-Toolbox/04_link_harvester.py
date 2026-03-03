import requests
from bs4 import BeautifulSoup # This library parses HTML

url = input("[+] Enter website to crawl (include http://): ")

print(f"[*] Harvester initiated on {url}...")

# 1. Get the raw HTML from the site
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 2. Find all 'a' tags (these are the links in HTML)
links = soup.find_all('a')

print(f"[!] Found {len(links)} links:\n")

# 3. Loop through them and print the 'href' (the actual URL)
for link in links:
    href = link.get('href')
    if href:
        print(f"-> {href}")