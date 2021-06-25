#To Check whether an input alphabet is vowel or not using Functions
def checkVowel(a):
    if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
        return "is vowel"
    else:
        return "is not vowel"

ch=input("Enter an alphabet : ")
print(ch," ",checkVowel(ch))