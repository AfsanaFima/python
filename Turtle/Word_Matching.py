def m_words(words) :
    ctr = 0
    list = []
    for word in words :
        if len(word) > 1 and word[0] == word[-1] :
            ctr += 1
            list.append(word)

    print("list of words with first and last caracter same :",list)
    return ctr

count = m_words(['fgg','sdf','rtr','4454'])
print("Number of words with first and last character same :",count)
