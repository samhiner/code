class cipher:
    def caesar(self,string,shift):
        print('only use lowercase')
        newStr = ''
        for x in string:
            charCode = ord(x)
            if not x.isalpha():
                newChar = x
            elif charCode + shift > 122:
                over = charCode + shift - 122
                newChar = chr(97 + (over - 1))
            else:
                newChar = chr(charCode + shift)
            newStr += newChar
        return newStr

    def vigenere(self,string,key):
        print('only use lowercase')
        newStr = ''
        k = 0
        for x in range(0,len(string)):
            currKey = k % len(key)
            charCode = ord(string[x])
            if not string[x].isalpha():
                newChar = string[x]
                k -= 1
            elif charCode + currKey > 122:
                newChar = chr(charCode + currKey - 25)
            else:
                newChar = chr(charCode + currKey)
            newStr += newChar
            k += 1
        return newStr

myCipher = cipher()
print(myCipher.caesar('hello world', 1))
print(myCipher.vigenere('hello world', 'abc'))
