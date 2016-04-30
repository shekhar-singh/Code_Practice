import string

x = raw_input()

algo = string.maketrans(
                "defghijklmnopqrstuvwxyzabc", "abcdefghijklmnopqrstuvwxyz")

print x.translate(algo)
