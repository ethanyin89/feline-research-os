import re

with open("scratch/sheet_edit.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for "feline HCM" or other sheet names and look for numbers nearby
# GID is typically an integer like 0, 396361602, 639162275, 799421167
# Let's search for the sheet titles in the script tags.
script_tags = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(script_tags)} script tags")

for idx, script in enumerate(script_tags):
    for name in ["feline FCV", "feline HCM", "feline CKD", "feline IBD", "feline FIP", "feline cancer"]:
        if name in script:
            print(f"Script tag {idx} contains '{name}'")
            # print 400 chars around the name in the script
            pos = script.find(name)
            start = max(0, pos - 200)
            end = min(len(script), pos + 400)
            print(script[start:end])
            print("="*60)
