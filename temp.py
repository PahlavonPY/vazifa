# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:  
 print("Do'konimizda quyidagi mahsulotlar yo'q:")
 for mahsulot in mavjud_emas:
    print(mahsulot)
 if bor_mahsulotlar:
    print("Siz so'ragan maxsulotlar ro'yxati")
    for mahsulot in bor_mahsulotlar:
        print(mahsulot)
else:        
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  for mahsulot in bor_mahsulotlar:
      print(mahsulot)
  print(" Xaridingiz uchun raxmat!")  


