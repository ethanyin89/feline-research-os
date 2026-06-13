import re
with open("scratch/sheet_edit.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for occurrences of "FIP", "CKD", "Obesity", "FCV", "Cancer"
for keyword in ["FIP", "CKD", "Obesity", "FCV", "Cancer", "HCM", "IBD", "Sheet1"]:
    indices = [m.start() for m in re.finditer(keyword, html, re.IGNORECASE)]
    print(f"Keyword '{keyword}' found at indices: {indices[:5]}")
    if indices:
        # print 100 chars around the first occurrence
        idx = indices[0]
        start = max(0, idx - 50)
        end = min(len(html), idx + 100)
        print(f"  Snippet: {html[start:end]!r}")
