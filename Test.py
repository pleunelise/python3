def palindrome(string):
    if string == string[::-1]:
        return string
        print(True)

    else:
        print(False)
print(palindrome('hallo'))
