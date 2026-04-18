def sonlarni_tartiblash(sonlar):
    sonlar.sort()
    return sonlar

def sonlarni_teskari_qilish(sonlar):
    sonlar.reverse()
    return sonlar

def median_qiymatini_topish(sonlar):
    sonlar.sort()
    uzunlik = len(sonlar)
    if uzunlik % 2 == 0:
        o_rta = (sonlar[uzunlik // 2 - 1] + sonlar[uzunlik // 2]) / 2
    else:
        o_rta = sonlar[uzunlik // 2]
    return o_rta

def asosiy_dastur():
    sonlar = [12, 45, 7, 23, 56, 89, 34]
    print("Asl sonlar ro'yxati:", sonlar)
    tartiblangan_sonlar = sonlarni_tartiblash(sonlar.copy())
    print("Tartiblangan sonlar ro'yxati:", tartiblangan_sonlar)
    teskari_sonlar = sonlarni_teskari_qilish(sonlar.copy())
    print("Teskari sonlar ro'yxati:", teskari_sonlar)
    median = median_qiymatini_topish(sonlar)
    print("Median qiymati:", median)
    sonlar_2 = [1, 3, 5, 7, 9]
    print("Asl sonlar ro'yxati 2:", sonlar_2)
    tartiblangan_sonlar_2 = sonlarni_tartiblash(sonlar_2.copy())
    print("Tartiblangan sonlar ro'yxati 2:", tartiblangan_sonlar_2)
    teskari_sonlar_2 = sonlarni_teskari_qilish(sonlar_2.copy())
    print("Teskari sonlar ro'yxati 2:", teskari_sonlar_2)
    median_2 = median_qiymatini_topish(sonlar_2)
    print("Median qiymati 2:", median_2)

asosiy_dastur()