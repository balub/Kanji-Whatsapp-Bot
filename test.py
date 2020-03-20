data = input("enter data ")



def process(data):
    default = 20
    split_sentence = data.split()
    level = split_sentence[0]
    num_questions = len(split_sentence)
    if num_questions is 2:
        return level, default
    else:
        return level, split_sentence[2]


level, num_questions = process(data)

print(level)
print(num_questions)
