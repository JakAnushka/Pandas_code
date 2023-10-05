
import pandas
data_read=pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data_read)
data_dict = {row.letter: row.code for (index, row) in data_read.iterrows()}
print(data_dict)
going_on=True
while going_on:
    user_input=input("enter your name?").upper()
    try:
        list_name = [data_dict[letter] for letter in user_input]
        print(list_name)
    except KeyError:
        print("please enter alphabets only.")
    else:
        going_on=False
# data_dict={row.letter: row.code for (index,row) in data_read.iterrows()}
# print(data_dict)
# list_name=[data_dict[letter] for letter in user_input]
# print(list_name)

# for (index,row) in data_read.iterrows():
#     dic[row.letter]=row.code
#     for i in user_input:
#         if row.letter==i:
#             l_name.append(row.code)
# print(l_name)
