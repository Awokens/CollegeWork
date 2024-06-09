def indexMapWords(path):
    
    dictionary = {}

    with open(path, 'r') as file:
        lines = file.readlines()
    for linePos, line in enumerate(lines, start=1):
        words = line.strip().split()
        for word in words:
            if word not in dictionary:
                dictionary[word] = []
            dictionary[word].append(linePos)
    
    with open('CS202/Module4/Part2/Dictionary/index.txt', 'w') as file:
        mappedWords = sorted(dictionary.keys())
        
        for word in mappedWords:
            lineIndex = ', '.join(str(num) for num in dictionary[word])
            file.write(f'{word}: {lineIndex}\n')

if __name__ == "__main__":
    indexMapWords('CS202/Module4/Part2/Dictionary/file.txt')