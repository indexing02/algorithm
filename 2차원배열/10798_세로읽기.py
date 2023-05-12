
word_list = []
word_length = []

for i in range(5):
    word = input()
    word_list.append(word)
    word_length.append(len(word))

for i in range(max(word_length)):
    for j in range(5):
        if i < word_length[j]:
            print(word_list[j][i], end="")
