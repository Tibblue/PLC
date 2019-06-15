

def count_digits(inteiros):
    c = 0
    for i in range(len(inteiros)):
        number = inteiros[i]
        while(number > 0):
            c+=1
            number = int(number / 10)
    return c


# x = count_digits([1,5,14,28,1000])
# print(x)

from unidecode import unidecode
import re

def is_palindrome(string):
    string = unidecode(string)
    string = string.lower()
    string = re.sub(r'!|,| |\.|\(|\)|:|_|-','',string)


    inv = len(string)-1
    for i in range(len(string)):
        if(string[i] != string[inv]):
            return False
        inv -= 1
    return True


x = is_palindrome("Olé! Maracujá, caju, caramelo")
print(x)