s = "hello world"  # Chuỗi trong Python là immutable (không thể thay đổi trực tiếp từng ký tự)

# s[0] = "R" # ❌ Lỗi: không thể gán lại ký tự trong chuỗi

a = len(s)
# print(a) # 👉 Kết quả: 11 (độ dài của "hello world")

# print(s.upper(), s)
# 👉 Kết quả: "HELLO WORLD hello world"
# upper() trả về chuỗi in hoa, không làm thay đổi s gốc

# print(s.lower())
# 👉 Kết quả: "hello world"
# lower() chuyển toàn bộ về chữ thường

# print(s.capitalize())
# 👉 Kết quả: "Hello world"
# capitalize() viết hoa chữ cái đầu tiên

# print(s.title())
# 👉 Kết quả: "Hello World"
# title() viết hoa chữ cái đầu mỗi từ


# text = " \nhello world "
# print(text.strip())
# 👉 Kết quả: "hello world"
# strip() xóa khoảng trắng và ký tự xuống dòng ở 2 đầu

# print(text.lstrip())
# 👉 Kết quả: "hello world "
# lstrip() xóa bên trái

# print(text.rstrip())
# 👉 Kết quả: " \nhello world"
# rstrip() xóa bên phải


# text = "Python is fun and fun and fun"
# print(text.find("is"))
# 👉 Kết quả: 7
# find() trả về vị trí xuất hiện đầu tiên của "is"

# print(text.replace("fun", "awesome"))
# 👉 Kết quả: "Python is awesome and awesome and awesome"
# replace() thay tất cả "fun" bằng "awesome"


# text = "Apples,Bananas,Pineapples"
# print(text.split(","))
# 👉 Kết quả: ['Apples', 'Bananas', 'Pineapples']
# split() tách chuỗi thành list theo dấu ","

print(",".join(["Apples", "Bananas", "Pineapples"]))
# 👉 Kết quả: "Apples,Bananas,Pineapples"
# join() nối các phần tử list thành chuỗi, ngăn cách bởi ","


text = "Python123"
print(text.isalpha())  # 👉 False: vì có số, không phải toàn chữ cái
print(text.isdigit())  # 👉 False: vì có chữ, không phải toàn số
print(text.isalnum())  # 👉 True: chỉ gồm chữ và số (không có ký tự đặc biệt)
print(text.isspace())  # 👉 False: không phải chỉ chứa khoảng trắng
