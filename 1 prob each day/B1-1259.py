while True:
    word = input()
    if word != '0':
        if word == word[::-1]:
            print('yes')
        else:
            print('No')
    else:
        break
    