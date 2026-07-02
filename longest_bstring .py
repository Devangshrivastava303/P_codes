def long_sub(s):
    seen=[]
    for i in range(len(s)):
        if s[i] not in seen:
            seen.append(s[i])
    return len(seen)
s="pwwkew"
print(long_sub(s))