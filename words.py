def extension(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        else:
            lower += 1

    if upper > lower:
        return s.upper()
    else:
        return s.lower()


s = input()
print(extension(s))