a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)  # Contains all the elements in a along with all the elements in b
print(c)

d = a.intersection(b)  # Contains only the elements that are present in a as well as b
print(d)
a = {3, 23, 1}  # Tập hợp a (không trùng lặp, không có thứ tự)
b = {23, 4, 2, 55, 1}  # Tập hợp b

c = a.union(b)  # Phép hợp: lấy tất cả phần tử của a và b (loại bỏ trùng)
print(c)
# 👉 Ví dụ kết quả: {1, 2, 3, 4, 23, 55} (thứ tự có thể khác)

d = a.intersection(b)  # Phép giao: lấy các phần tử xuất hiện trong cả a và b
print(d)
# 👉 Kết quả: {1, 23}
