import string
import random
import os

alphabet = list(string.ascii_uppercase)
print(alphabet)

with open("summary.txt", "w") as summary_file:
    for letter in alphabet:
        filename = f"{letter}.txt"
        with open(filename, "w") as file:
            n = random.randint(1, 100)
            file.write(f"{n}")
            summary_file.write(f"{filename}:{n}\n")
