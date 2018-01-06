#Two ways to implement Anagram check in Python

#Easier way

def anagram_check(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    return sorted(str1) == sorted(str2)


#Using hash table

def anagram_check2(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    #Edge case
    if len(str1) != len(str2):
        return False

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for letter in count:
        if count[letter] == 0:
            return True
    return False
