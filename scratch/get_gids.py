import re
with open("scratch/sheet_edit.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for "goog-inline-block docs-sheet-tab-caption" and display the full parent structure
# The parent divs usually have some IDs or attributes
pattern = r'<div class="[^"]*docs-sheet-tab-caption"[^>]*>([^<]+)</div>'
for match in re.finditer(pattern, html):
    caption = match.group(1)
    idx = match.start()
    # print 500 characters before the caption to see if GID is there
    start = max(0, idx - 400)
    end = min(len(html), idx + 200)
    print("--------------------------------------------------")
    print(f"Caption: {caption}")
    print(f"Context:\n{html[start:end]}")
