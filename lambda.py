x=int(input("angka 1 "))
y=int(input("angka 2 "))
try:
    a=x/y
except:
    print("ada error")
else:
    print (a)
finally:
    print('selesai')
