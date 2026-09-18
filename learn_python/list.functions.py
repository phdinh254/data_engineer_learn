student_name = ["Nguyen", "Hung", "Tien", "Quang", "Thanh"]
math_score = [10, 9, 8, 7, 6]

math_score.sort() ##sắp xếp list
print(math_score)

math_score.reverse() ##đảo ngược list
print(math_score)

student_name2 = student_name.copy() ##tạo ra một bản sao của list
print (student_name2)

print(student_name)

student_name.extend(math_score) ##nối list
print(student_name)

student_name.append("Trung") ##thêm 1 phần tử vào cuối list
print(student_name)

student_name.insert(1, "Linh") ##thêm 1 phần tử vào list tại vị trí index
print(student_name)

student_name.remove("Quang") ##xóa 1 phần tử bất kỳ trong list
print(student_name)

student_name.pop(2) ##xóa 1 phần tử bất kỳ trong list
print(student_name)

print(student_name.index("Linh")) ##trả về vị trí index của phần tử trong list

print(student_name.count("Linh")) ##đếm số lần xuất hiện của phần tử trong list

student_name.reverse() ##đảo ngược list
print(student_name)

student_name.clear() ##xóa tất cả các phần tử trong list
print(student_name)
