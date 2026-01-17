def count_words(text: str) -> dict:
    words = text.split()
    word_count = {}
    
    for word in words:
        word = word.lower().strip('') 
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count
print(count_words("salom salom dunyo dunyo salom"))