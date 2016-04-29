import string

x = raw_input()

algo = string.maketrans(
		"abcdefghijklmnopqrstuvwxyz", "defghijklmnopqrstuvwxyzabc"
    )

print x.translate(algo)
