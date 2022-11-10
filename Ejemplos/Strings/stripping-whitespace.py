demo = "     This is a demo string     "

print("This string has extra whitespace at both beginning and end: **" + demo + "**")
print("This string has extra whitespace at the end only: **" + demo.lstrip() + "**")
print("This string has extra whitespace at the beginning only: **" + demo.rstrip() + "**")
print("This string does not have any extra whitespace: **" + demo.strip() + "**")