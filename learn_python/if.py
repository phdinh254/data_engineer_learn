a = 100
b = 100

if a > b:
    print("a lớn hơn b")
elif a < b:
    print ("a nhỏ hơn b")
else:
    print("a bằng b")

x = 500
y = 70
z = 500

if (x > y) and (x > z): ## and: tất cả các điều kiện phải đúng thì mới đúng 
    print("x là số lớn nhất")
elif (y > x) and (y > z):
    print ("y là số lớn nhất")
else:
    print("z là số lớn nhất")

if (x==y) or (x==z): ## or: chỉ cần 1 điều kiện đúng thì sẽ đúng 
    print("x bằng y hoặc x bằng z")
    
if not (x==y): ## not: phủ định lại điều kiện 
    print("x khác y") 

