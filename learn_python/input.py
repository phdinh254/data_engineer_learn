print ("Hãy điền vào form dưới đây!")
name = input ("Nhập tên : ")
age = input ("Nhập tuổi : ")
clas = input ("Nhập lớp học : ")
id = input ("Nhập mã số sinh viên : ")
print ("Cảm ơn " + name + " đã điền form! ")
print (f"Cảm ơn {name} đã điền form! ")

# Cắt chuỗi thành danh sách các từ, sau đó lấy từ cuối cùng
ten = name.split()[-1]
print ("Cảm ơn " + ten + " đã điền form! ")