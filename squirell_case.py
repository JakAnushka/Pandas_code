import pandas
squirrel_data=pandas.read_csv("Squirrel_data.csv")
all_color=squirrel_data["Primary Fur Color"]
count_gray=0
count_black=0
count_red=0
for c in all_color:
    if c=="Gray":
        count_gray+=1
    elif c=="Black":
        count_black+=1
    elif c=="Cinnamon":
        count_red+=1

print(f"the gray color is {count_gray}")
print(f"the gray color is {count_black}")
print(f"the gray color is {count_red}")
color_squirrel={
    "fur color":["gray","red","black"],
    "Count":[count_gray,count_red,count_black]
}
new_data=pandas.DataFrame(color_squirrel)
new_data.to_csv("squirrel_count.csv")
# ANOTHER method to calculate the gray or color is
# len(data[data["primary fur color"]=="gray"])