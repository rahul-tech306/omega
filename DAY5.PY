def word_frequency(text):
    
    words = text.split()
    
    fre = {}
    for word in words:
        if word in fre:
            fre[word] += 1
        else:
            fre[word] = 1
    
    for word, count in fre.items():
        print(f"{word}: {count}")

text = "this is a test this is only a test"
word_frequency(text)