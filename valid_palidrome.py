def isvalid(s):
    stack=[]

    for i in len(s):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            stack.append(s[i])

        else: 
            if len(stack)==0:
                return False
        
            if s[i]==')' and stack[-1]!='(':
                return False
            elif s[i]=='}' and stack[-1]!='{':
                return False
            elif s[i]==']' and stack[-1]!='[':
                return False
                
        

s="()"
print(isvalid(s))