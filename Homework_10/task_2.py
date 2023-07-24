import textwrap

with open("firstfile.txt", "w") as firstfile:
    content_dirty = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    content = "\n".join(textwrap.wrap(content_dirty, 70))
    firstfile.write(content)

with open("firstfile.txt", "r") as firstfile, open("secondfile.txt", "w") as secondfile:
    content_upper = firstfile.read().upper()
    secondfile.write(content_upper)



