def binary_strings(n, r):
    strings = set()
    if n < r or r < 0 or n == 0:
        return {}
    if n == 1:
       return {f'{r}'}
    for string in list(binary_strings(n-1,r)):
        strings.add(string + "0")
    for string in list(binary_strings(n - 1, r-1)):
        strings.add(string + "1")
    return list(strings)

def dyck_words(n):
    strings = set()
    if n == 0:
        return []
    if n == 1:
        return ["10"]
    for word in dyck_words(n-1):
        for i in range(len(word)):
            new_word = f"{word[:i]}1{word[i:]}"
            for k in range(len(word)-i):
                index = i + k+1
                new_word2 = f"{new_word[:index]}0{new_word[index:]}"
                strings.add(new_word2)
    return list(strings)

def Nariyana_sequence(n,r):
    n = n+1
    r = r+1
    strings = set()
    if n < r or r < 0 or n == 0:
        return {}
    possible_words = dyck_words(n)
    for word in possible_words:
        k = 0
        for index in range(len(word)-1):
            if word[index] == "1" and word[index+1] == "0":
                k+=1
        if k == r:
            strings.add(word)
    return list(strings)

def fibbonaci_sequence(n):
    strings = set()
    if n == 0:
        return ["0"]
    if n == 1:
        return ["1"]

    for word in fibbonaci_sequence(n-1):
        strings.add("0" + word)
    for word in fibbonaci_sequence(n - 2):
        strings.add("1" + word)
    return list(strings)

