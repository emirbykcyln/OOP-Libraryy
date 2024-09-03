#Kitap Sinifi
class Kitap:
    def __init__(self,baslik,yazar,isbn):
        self.baslik = baslik
        self.yazar = yazar
        self.isbn = isbn
        self.odunc_alindi_mi = False
        
    def odunc_al(self):
        if not self.odunc_alindi_mi:
            self.odunc_alindi_mi = True
            return True
        return False
    
    def iade_et(self):
        if self.odunc_alindi_mi:
            self.odunc_alindi_mi = False
            return True
        return False
    
#Kullanici Sinifi
class Kullanici:
    def __init__(self,isim, kullanici_no):
        self.isim = isim
        self.kullanici_no = kullanici_no
        self.odunc_kitaplar = []
        
    def kitap_odunc_al(self,kitap):
        pass
    
    def kitap_iade_et(self,kitap):
        if kitap in self.odunc_kitaplar:
            kitap.iade_et()
            self.odunc_kitaplar.remove(kitap)
            return True
        return False
    
#Ogrenciler Alt Sinifi

class Ogrenci(Kullanici):
    def kitap_odunc_al(self, kitap):
        if len(self.odunc_kitaplar) < 3 and kitap.odunc_al():
            self.odunc_kitaplar.append(kitap)
            return True
        return False
    
#Personel Alt sinifi

class Personel(Kullanici):
    def kitap_odunc_al(self, kitap):
        if len(self.odunc_kitaplar) < 5 and kitap.odunc_al():
            self.odunc_kitaplar.append(kitap)
            return True
        return False

#Kütüphane Sınıfı

class Kutuphane:
    def __init__(self):
        self.__kitaplar = []
        self.__kullanicilar = []
        
    def kitap_ekle(self,kitap):
        self.__kitaplar.append(kitap)
        
    def kullanici_ekle(self,kullanici):
        self.__kullanicilar.append(kullanici)
        
    def kitap_odunc_ver(self,kullanici,isbn):
        kitap = self.__kitap_bul(isbn)
        if kitap and kullanici.kitap_odunc_al(kitap):
            print(f'{kitap.baslik} kitabi {kullanici.isim} tarafindan odunc alindi.')
        else:
            print('kitap odunc verilemedi.')
        
    def kitap_iade_al(self,kullanici,isbn):
        kitap = self.__kitap_bul(isbn)
        if kitap and kullanici.kitap_iade_et(kitap):
            print(f'{kitap.baslik} kitabi {kullanici.isim} tarafindan iade edildi')
        else:
            print('Kitap iade edilemedi.')
            
    def __kitap_bul(self,isbn):
        for kitap in self.__kitaplar:
            if kitap.isbn == isbn:
                return kitap
        return None
    
# Kullanim Senaryosu

kutuphane = Kutuphane()

kitap1 = Kitap('Sefiller','Victor Hugo','74198852')
kitap2 = Kitap('Peygamberligin Ispati','Altay Cem Meric','48256241')

ogrenci1= Ogrenci('Ahmet',1)
personel1= Personel('Veli',4)


kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)
kutuphane.kullanici_ekle(ogrenci1)
kutuphane.kullanici_ekle(personel1)

kutuphane.kitap_odunc_ver(ogrenci1,'74198852')
kutuphane.kitap_odunc_ver(personel1,'48256241')

kutuphane.kitap_iade_al(ogrenci1, "74198852")
kutuphane.kitap_iade_al(personel1, "48256241")