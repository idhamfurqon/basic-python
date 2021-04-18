# """ # a = 33
# b = 100
# c = 22
# d = 22

# #if c == d :
#     #print ("betul")
# #else:
#     #print("salah")

# if b > a:
#     print("b lebih besar dari a")
# elif a > c:
#     print("a lebih besar dari c")
# else:
#     print("a lebih besar dari b")

x = int(input("Masukkan nilai : "))

if x % 2 == 1:
    if x < 10:
        print("x adalah bil ganjil dibawah 10")
    else:
        print("x adalah bil ganjil diatas 10")
else:
    print("x adalah bil genap")