import re
import json

with open("scratch/sheet_edit.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for bootstrapData or other JSON arrays in script tags
# GSheets bootstrap JSON typically contains "sheetId": ... and "title": ...
# Or similar keys. Let's search for "sheetId" or "gid" inside the whole html
# using broad regex.

# Print anything that has "sheetId" and the sheet title
# E.g. {"sheetId": 0, "title": "feline diabetes & obesity"}
# Or similar combinations.

matches = re.finditer(r'["\'](sheetId|gid|id)["\']\s*:\s*(\d+|"[^"]+")', html)
for m in matches:
    # Print the surrounding 200 chars to find context
    start = max(0, m.start() - 100)
    end = min(len(html), m.end() + 100)
    snippet = html[start:end]
    if "feline" in snippet.lower():
        print("MATCH:", snippet)
        print("="*40)
