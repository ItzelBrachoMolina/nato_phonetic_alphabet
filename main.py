import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

data_dict=dict(zip(data.letter,data.code))
print(data_dict)

your_answer=input("write your name: ")

your_answer_list=[n.upper() for n in your_answer]

print(your_answer_list)



n = {data_dict[k] for k in your_answer_list if k in data_dict}

print(n)
