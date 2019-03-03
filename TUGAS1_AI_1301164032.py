# Tugas ini dibuat oleh Bintang Peryoga 1301.1640.32

# step-1 : inisialisasi variable, function, dan library yang dibutuhkan
from math import *
import random

def objective(a,b):
    Energi = - abs(sin(a)*cos(b)*exp(fabs(1-(sqrt(a**2 + b**2)/pi))))
    return Energi

x1 = -10
x2 = -10
T = 100000
x1_best = x1
x2_best = x2
E_best = objective(x1_best,x2_best)
E = objective(x1,x2)

# step-2 looping mencari x1 dan x2 yang menyebabkan fungsi memiliki nilai minimum hingga T = 0
while T > 0:
    x1_new = x1 + random.random()
    x2_new = x2 + random.random()
    E_new = objective(x1_new,x2_new)
    deltaE = E_new - E
    # ditambah syarat agar x1_new dan x2_new masih dalam range kurang dari sama dengan 10 dan lebih dari sama dengan -10
    if deltaE < 0 and x1_new <= 10 and x1_new >= -10 and x2_new <= 10 and x2_new >= -10:
        x1 = x1_new
        x2 = x2_new
        E = E_new
        # Jika Energinya lebih kecil maka E_best dan x1_best dan x2_best nya diganti ke yang baru.
        if E_new < E_best:
            x1_best = x1_new
            x2_best = x2_new
            E_best = E_new
    # dipertimbangkan ulang apakah x1_new dan x2_new nya dapat diambil
    elif x1_new <= 10 and x1_new >= -10 and x2_new <= 10 and x2_new >= -10:
        P = exp(- (deltaE)/T)
        R = random.random()
        if R < P:
            x1 = x1_new
            x2 = x2_new
    # pengurangan temprature agar ketika di-looping T. Diharapkan semakin kecil suhu maka nilai x1_best, x2_best, dan E_best semakin optimum
    T = T - 1

# step-3 return x1 dan x2 serta nilai minimum yang dihasilkan dari rumusnya
print("x1 : ",x1_best)
print("x2 : ",x2_best)
print("Nilai Minimum : ",E_best)