import urllib.request
import re

url = "https://docs.google.com/spreadsheets/d/1Y-MSR39kW5F5J4OedcctdeHk0jhe1mbyvsK43Fcc7lk/edit"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    
    # Let's search for sheet metadata in the bootstrap data
    # GSheets HTML often has a script tag with bootstrapData containing "sheetId"
    # Let's print out all occurrences of "sheetId" or similar, or sheet names.
    print("HTML length:", len(html))
    
    # Save a snippet containing sheet data
    # Often sheets are list of dicts: {"properties":{"sheetId":0,"title":"Sheet1"...}}
    # Let's look for "sheetId"
    matches = re.findall(r'"sheetId":\s*(\d+),\s*"title":\s*"([^"]+)"', html)
    if not matches:
        matches = re.findall(r'sheetId:\s*(\d+),\s*title:\s*["\']([^"\']+)["\']', html)
    
    if not matches:
        # Let's look for "gid"
        matches = re.findall(r'"gid":\s*(\d+),\s*"name":\s*"([^"]+)"', html)
        
    print("Found matches:", len(matches))
    for m in matches:
        print(m)
        
    # If no matches, let's write first 200k chars to a file for manual check
    with open("scratch/sheet_edit.html", "w", encoding="utf-8") as f:
        f.write(html[:500000])
except Exception as e:
    print("Error:", e)
