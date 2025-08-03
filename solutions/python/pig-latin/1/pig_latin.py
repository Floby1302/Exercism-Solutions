def translate(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word.startswith(('xr', 'yt')) or word[0] in vowels:
            result.append(word + "ay")
            continue
        if "qu" in word:
            qu_index = word.find("qu")
            if qu_index != -1 and all(char not in vowels for char in word[:qu_index]):
                result.append(word[qu_index + 2:] + word[:qu_index + 2] + "ay")
                continue
        for i in range(1, len(word)):
            if word[i] == 'y' and all(char not in vowels for char in word[:i]):
                result.append(word[i:] + word[:i] + "ay")
                break
        else:
            for i, char in enumerate(word):
                if char in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
            else:
                result.append(word + "ay")

    return ' '.join(result)