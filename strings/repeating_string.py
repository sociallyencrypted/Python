#Made by Mehul Arora on 12 Jan 2021
#Checks for a repeating sequence in a string
#For eg. "abcabcabc" returns "abc"
def repStr(string1):
    tmp=string1*2
    tmp=tmp[1:-1]
    index=tmp.find(string1)
    return string1[0:index]

if __name__ == "__main__":
    print(repStr(input("Please input sequence: ")))
