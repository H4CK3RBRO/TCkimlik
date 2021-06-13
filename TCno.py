# Coder: HACKERBRO
#TC Kimlik No Son 2 Haneyi Bulma!
def tcno(tcno):
    if len(tcno) == 9:
        a = 7*(int(tcno[0])+int(tcno[2])+int(tcno[4])+int(tcno[6])+int(tcno[8]))
        b = int(tcno[1])+int(tcno[3])+int(tcno[5])+int(tcno[7])
        haneOn = (a-b)%10
        onHaneli=str(tcno)+str(haneOn)
        toplamOn = 0
        for i in range(10):
            toplamOn=toplamOn+int(onHaneli[i])
        haneOnBir = toplamOn%10
        return tcno+str(haneOn)+str(haneOnBir)
    else:
        print("Girilen TC No 9 Haneli Olmalıdır.")
tcnumara = input("TC Kimlik No ilk 9 Hanesini Giriniz. ")
print("TC Kimlik No'nun Tamamı :",tcno(tcnumara))
