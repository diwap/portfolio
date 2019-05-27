import random

word = "Dinosaurs"


splitted_string = [i.lower() for i in word]

half_len = round(len(splitted_string)/2)
i = 0

new_string = ["*" for i in word]

while i <= half_len:
    index_no = splitted_string.index(random.choice(splitted_string))
    # OR
    # index_no = random.randrange(len(splitted_string) -1)

    new_string[index_no] = splitted_string[index_no]
    i += 1

my_word = "Guess this word: {0}".format(
    "".join(new_string)
)

print(my_word)