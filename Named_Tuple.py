from collections import namedtuple

Color_names=namedtuple("field_names",["red","orange","blue"])

print(type(Color_names))
color_nums=Color_names(55,78,95)
print(color_nums[0],color_nums[2])
print(color_nums.blue)

different=Color_names(32,43,70)
print(different.blue)