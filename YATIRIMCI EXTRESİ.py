aylık_extre ="""
Tarih: {} itibariyle
Yatırımcı: {}
Yatırım Başlangıc Tarihi: {}
Geçen Süre (Gün): {}
Hissedarı Olduğu Şirket / Şirketler: {} olmak üzere,
Toplam Şirket Sayısı: {} Adettir.

{} Ayı Pörtföy Durumu Aşağıdaki Gibi Gerçekleşmiştir:

{} Endeksi: {} {} 
Karda Olan Şirket Sayısı: {}
Zararda Olan Şirket Sayısı: {}
Durumu En iyi Olan Şirket: {}
Durumu En Kötü Olan Şirket: {}

Yatırım Toplamı(TL): {}      
Son Değeri(TL): {}         
Kar / Zarar(TL): {}       
TL Bazında %: {}

Yatırım Toplamı(EU): {}
Son Değeri(EU): {} 
Kar / Zarar(EU): {}
EU Bazında %: {}

Yatırım toplamı(USD): {}
Son Değeri(USD): {}
Kar / Zarar(USD): {}
USD Bazında %: {}

Pörtföyün Yıllık Temettü Geliri: {}
Pörtföyün Yıllık Temettü Yüzdesi: {}

Açıklamalar: {}

Pörtföy Yönetimi: HAZİRAN COMPANY/HELSİNKİ-FİNLAND
coded by Gökay!

"""
tarih             = input("Tarih: ")
isim              = input("Yatırımcı: ")
y_b_tarihi        = input("Yatırım Başlangıç Tarihi: ")
geçen_süre        = input("Geçen Süre (Gün): ")
şirketler         = input("Hissedarı Olduğu Şirket / Şirketler: ")
tşirket           = input("Toplam Şirket Sayısı: ")
ay_adı            = input("Ekstre Ayı: ")
endeks            = input("Endeks ismi: ")
endeks_durumu     = input("Endeks Durumu: ")
pozitif_negatif   = input("+ ve -: ")
iyiler_sayı       = input("Karda Olan Şirket Sayısı: ")
kötüler_sayı      = input("Zararda Olan Şirket Sayısı: ")
best_şirket       = input("Durumu En İyi Olan Şirket: ")
worst_şirket      = input("Durumu En Kötü Olan Şirket: ")
tl_toplam         = input("Yatırım Toplamı (TL): ")
tl_son_deger      = input("Yatırım Ulaştığı Değer (TL): ")
tl_karzarar       = input("Kar / Zarar Durumu (TL): ")
tl_yüzde          = input("TL Bazında %: ")
eu_toplam         = input("Yatırım Toplamı (eu): ")
eu_son_deger      = input("Yatırım Ulaştığı Değer (eu): ")
eu_karzarar       = input("Kar / Zarar Durumu (eu): ")
eu_yüzde          = input("EU Bazında %: ")
usd_toplam        = input("Yatırım Toplamı (usd): ")
usd_son_deger     = input("Yatırım Ulaştığı Değer (usd): ")
usd_karzarar      = input("Kar / Zarar Durumu (usd): ")
usd_yüzde         = input("USD Bazında %: ")
yıllık_temettü    = input("Pörtföyün Yıllık Temettü Geliri (TL):  ")
yıllık_temettü_yz = input("Pörtföyün Yıllık Temettü Kazancı %: ")
açıklama          = input("Açıklamalar: ")

dosya = open("Aylık Yatırımcı Ekstresi.txt","w")
print(aylık_extre.format(tarih,
                         isim,
                         y_b_tarihi,
                         geçen_süre,
                         şirketler,
                         tşirket,
                         ay_adı,
                         endeks,
                         endeks_durumu,
                         pozitif_negatif,
                         iyiler_sayı,
                         kötüler_sayı,
                         best_şirket,
                         worst_şirket,
                         tl_toplam,
                         tl_son_deger,
                         tl_karzarar,
                         tl_yüzde,
                         eu_toplam,
                         eu_son_deger,
                         eu_karzarar,
                         eu_yüzde,
                         usd_toplam,
                         usd_son_deger,
                         usd_karzarar,            
                         usd_yüzde,
                         yıllık_temettü,
                         yıllık_temettü_yz,
                         açıklama),file=dosya)
dosya.close()






