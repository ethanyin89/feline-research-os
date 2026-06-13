import re
with open("scratch/sheet_edit.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for "feline " and print 100 characters before and after
for caption in ["feline diabetes & obesity", "feline FCV", "feline HCM", "feline CKD", "feline IBD", "feline FIP", "feline cancer"]:
    idx = html.find(caption)
    if idx != -1:
        print(f"Caption: {caption}")
        print(f"Before: {html[idx-150:idx]!r}")
        print(f"After: {html[idx:idx+150]!r}")
        print("="*40)
