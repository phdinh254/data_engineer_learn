number = 2
text = " là số người yêu cũ"

print (str(number) + text)
print (f"{number}{text}")

number = 2
text = "{} là số người yêu cũ"

print (text.format(number))

my_name = "Trầ Phú Dinh"
my_age = 21
text = "Tôi tên là {} năm nay tôi {} tuổi"

print(text.format(my_name, my_age))

text = "Tôi tên là {1} năm nay tôi {0} tuổi"

print(text.format(my_name, my_age))