
def ReverseString(s):
    return s[::-1]

print('Reversed string is',ReverseString('hello'))


def is_alinfrome(s):
    s = s.replace(" ", "").lower()
    return s== s[::-1]

print('Is "madam" a palindrome?', is_alinfrome(' madam')) 


def vowelCount(s):
    vowels='aeiouAEIOU'
    vCount=0
    cCount=0
    for char in s:
        if char in vowels:
            vCount+=1
        else:
            cCount+=1
            
    return vCount, cCount
print('Vowel and consonant count in "Hello World":', vowelCount('Hello World'))