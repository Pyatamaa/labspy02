#Program1
#Persen diubah ke desimal

modal = 100000000
 
print("modal awal usaha",modal)

#m = month alias bulan
for m in range (1,9):
    if(m>=1 and m<=2):
        hasil1 = modal *0
        print("laba bulan ke-",m,"sebesar = ",hasil1)
    if(m>=3 and m<=4):
        hasil2 = modal *0.01
        print("laba bulan ke-",m,"sebesar = ",hasil2)
    if(m>=5 and m<=7):
        hasil3 = modal *0.05
        print("laba bulan ke-",m,"sebesar = ",hasil3)
    if(m==8):
        hasil4 = modal *0
        print("laba bulan ke-",m,"sebesar = ",hasil4)