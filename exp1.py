a=["aaf","acd","bab","racecar"]
palindrome=""
for i in range (len(a)):
    n=a[i]
    if n==n[::-1]:
        palindrome=n
        break
print("First palindrome: ",palindrome)

