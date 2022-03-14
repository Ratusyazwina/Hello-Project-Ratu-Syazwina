kunci = int(input("kunci : "))
tebakan = int(input("tebakan : "))
salah = tebakan != kunci
while (salah):
    tebakan = int(input("tebakan : "))
    salah = tebakan != kunci
print("tebakan user benar")