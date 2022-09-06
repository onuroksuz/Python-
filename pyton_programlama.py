# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:08:22 2022

@author: onuro
"""
#SAYILAR VE STRINGLERE GIRIS Ve GENEL BILINMESI GEREKENLER

#Median (medyan)
#Bir seriyi kucukten buyuge veyas buyukten kucuge 
#siraladigimizda tam orta noktadan seriyi iki esit parcaya 
#ayiran degere medyan adi verilir.                      

#Mod bir degiskende en cok gozlemlenen frenkansi encok olan degere
#mod adi verilir

#Quartiles (Kartiller) 
#Kucukten buyuge siralaanan bir seriyi 4 parcaya 
#ayiran degerlere kartiller denir

# Range (degisim araligi)
#Degisim Araligi  = Maksimum Deger – Minimum deger       


9+9

"Hello ia era"

print('HELLO AI ERA')

type(9)         # Bu intiger dir
type(9.2)       # Float dir
type(9.233123212312321)

type("HELLO AI ERA")

#STRINGLERE YAKINDAN BAKALIM

#Strings

#Ondalik sayilar FLOAT oluyor mesela 9.2

#Tam sayilar ise INTEGER denir mesela 9

#Genel anlamda saiylar ikiye ayrilir
#ama 3-4 e de ileride durumlara gore ayrilabilir

""
123
type(123)
"123"
type("123")

-'a' + 'b'
'a' 'b'

'a' + '-b'

'a' - 'b'

'a'*3

'a'/3


#STRING METODLAR - len()

gel_yaz='gelecegi_yazanlar'
#del ab

a = 9
b = 10

a*b

len(gel_yaz)

#STRING METODLARI - UPPER() & LOWER()


gel_yaz ='gelecegi_yazanlar'

gel_yaz.upper()

gel_yaz.lower()

gel_yaz.islower()
gel_yaz.isupper()

B = gel_yaz.upper()

B.isupper()


#STRING METODLARI - replace()

gel_yaz.replace('e', 'a')

gel_yaz.replace('a', 'i')

#STRING METODLARI - strip()

gel_yaz.strip()
gel_yaz= "*gelecegi_yazanlar*"
gel_yaz.strip('*')

gel_yaz= "lgelecegi_yazanlarl"
gel_yaz.strip('l')

#METODLARA GENEL BAKIS

gel_yaz = 'gelecegi_yazanlar'

dir(gel_yaz)

gel_yaz.capitalize()


gel_yaz.title()

#SUBSTRINGLER

# gel_yaz = 'gelecegi_yazanlar'

# gel_yaz[0]   bunu yazinca g harfi ortaya cikar cunku saymaya 0 dan baslar                       

# gel_yaz[20]  index hatasi verir cunku gelecegi_yazanlar 
#17 harftir

# gel_yaz[0:3] bunu yazdigimizd gel yazar

# gel_yaz[3:8] bunu yazdigimizda ecegi yazar yani ucten 
#itibaren almis oluyor


gel_yaz = 'gelecegi_yazanlar'

gel_yaz[0]                                     

gel_yaz[20]

gel_yaz[0:3]

gel_yaz[3:8]



#degiskenler


a = 9
b ='ali_uzaya_git'
c = a*2

a/c

a*c

a*5


type(100)
type(100.2)
type(1+2j)

a = 100.2

#TYPE_DONUSUMLERI

birinci_sayi = input()

9

toplama_bir = input()
toplama_iki = input()

type(toplama_bir)

toplama_bir + toplama_iki

int(toplama_bir) + int(toplama_iki)

int(11.0)

float(12)

str(12)

type(str(12))

#print

#print('gelecegi','yazanlar')   bunu yazinca   
#gelecegi yazanlar cikiyor

#print('gelecegi','yazanlar', sep ='_')   
#bunu yazinca gelecegi_yazanlar yani alt cizgi cikiyor


print('HELLOW AI ERA')

print('gelecegi','yazanlar')

print('gelecegi','yazanlar', sep ='_')

print()

type()

?print

?type

#VERI YAPILARI

#Listeler

#[]

#list ()

notlar = [90,80,70,50]

type(notlar)

liste = ['a',19.3,90,notlar]

type(liste)

list_genis = ['a', 19.3, 90, notlar]

#Degiskenler

type(list_genis)

len(list_genis)

list_genis[0]
list_genis[3]

type(list_genis[0])


tum_liste = [liste, list_genis]

#del tum_liste

#listeler -Eleman Islemleri

liste = [10,20,30,40,50]

liste[0]
liste[1]

liste[6]

liste[0:2]

liste[:2]

liste[2:]

yeni_liste = ['a',10,[20,30,40,50]]

yeni_liste

yeni_liste[2]

yeni_liste[0:2]

yeni_liste[2][1]

#Listeler - Eleman Degistirme

liste = ['ali','veli','berkan','ayse']

liste

liste[1] = 'velinin_babasi'

liste


liste[1] = 'veli'

liste[0:3] = 'alinin_babasi','velinin_babasi','berkcanin_babasi'

#liste[0:3] = 'alinin_babasi'
#velinin_babasi','berkcanin_babasi'  bunu yazip calistirinca 
#cvp boyle oluyor 
#['alinin_babasi', 'velinin_babasi','berkcanin_babasi', 'ayse']
#neden boyle oluyor cunku 0 dan 3 e kadar degistirdik ayse sabit kaldi




liste = ['ali','veli','berkan','ayse']

liste +['kemal']

liste = liste +['kemal']

del liste[2]

liste

#listeler - Liste Metotlari

#liste = ['ali','veli','berkan','ayse']
#liste +['kemal']  boyle yazarsak sadece out a ekler, variable explorer e eklemez

#liste = liste +['kemal']  ancak boyle yazarsak her ikisinede ekler

#del liste[2] nesleri silmek icinde boyle yaziliyor

#liste  ['alinin_babasi', 'velinin_babasi', 'ayse', 'kemal']



dir(liste)

liste

#append

liste.append('berkcan')

liste

#liste  ['alinin_babasi', 'velinin_babasi', 'ayse', 'kemal', 'berkcan'] 
#bu sekilde berkcan hem  variable explorer’e hemde out a eklemis oluyoruz 


liste.remove('berkcan')

liste

#liste ['alinin_babasi', 'velinin_babasi', 'ayse', 'kemal'] 
#bu sekilde remove yaparak berkcan hem  variable explorer’e
#hemde out a silmis oluyoruz 

#insert

liste  = ['ali','veli','isik']


liste

liste.insert(0,'ayse')
#liste.insert(0,'ayse')  cvp 
#['ayse', 'ali', 'veli', 'isik']  bu sekilde ayseyi eklemis oluyorz

liste

liste.insert(2,'mehmet')

liste

#len(liste) listyeyi say diyoruz

len(liste)

liste.insert(len(liste),'beren')
liste

#pop

#liste.pop(0)
#liste  ['ali', 'mehmet', 'veli', 'isik', 'beren']
# boylelikle 0. Olan ayse silindi del v.s kullanmadan


liste.pop(0)
liste

#count 

#liste.count('ali')    cvp listede kactane ali oldugnu verdi bize   2
#liste.count( 'veli')  cvp listede kactane veli oldugnu verdi bize  1


liste = ['ali', 'mehmet', 'veli', 'ali','isik', 'beren']

liste

liste.count('ali')
liste.count( 'veli')


#copy

#liste_yedek = liste.copy()    cvp liste yi kopyalar

liste_yedek = liste.copy()



#extend

#liste_yedek = liste.copy()   cvp liste yi kopyalar
#liste_yedek = liste.copy()   cvp liste yi kopyalar


liste.extend(['a','b',10])
liste

#index

#liste.index('ali') cvp index 0 inci indexed bilgisini veriyor  

liste.index('ali')

#reverse()

#liste.reverse()  cvp liste yi tersten yaziyor [10, 'b', 'a', 'beren', 'isik', 'ali', 'veli', 'mehmet', 'ali']

liste.reverse()
liste

#sort ()

#liste.sort() yazinca su hatayi aldik  
#TypeError: '<' not supported between instances of 'str' and 'int'
#yani bunun string mi int oldugunu anlamadim yaziyor ve yeni liste yazdik 


liste.sort()

liste = [10,40,5,90]

#liste.sort()  yeni liste ye gore bunlari kucukten buyuge siraladi [5, 10, 40, 90]

liste.sort()
liste

#clear
#liste.clear()  listeyi temizleme islemi , calistirinca sunu Verdi [] 
#yani listenioin icindeki hersey silindi



liste.clear()
liste


#reserve()

liste.reserve()
liste

#veri yapilari - Tuple
# Tuple olusturma

#1 Tuple lar degistirilemezler
#2 Siralidir
#3 Listeler gibi kapsayicidirlar, index islemleri yapilabilir



t =('ali','veli',1,2,3.2,[1,2,3,4])

t = 'ali','veli',1,2,3.2,[1,2,3,4]

#tuble()

t = ('eleman',)   #eger virgul koymazsan str yazar tuple yazmaz
#bundan dolayi bazen virgul yazmamiz lazim

type(t)

#Tuple Eleman Islemleri

t = ('ali','veli',1,2,3.2,[1,2,3,4])
t

t[1]         #dedigimizde t deki birincie eleman veli bizeriyor

t[0:3]       #dedigimizde bize('ali', 'veli', 1) veriyor

t[2] = 99    # yazdigimizda hata aliyoruz cunku tuple larda degistirilemez, 
             #biz burada 99 atamaya kalktik hata aldik


# Veri Yapilari - Dictionary (sozluk)

# sozlukler kapsayici, degistirile bilir ve sayisizdir

sozluk = {'REG' : 'Regresyon Modeli' ,
          'Loj' : 'lojistik Regresyon',
          'CART':'Classification and Reg'}

sozluk = {'REG' : 10,
          'LOJ' : 20,
          'CART': 30,}              #boyle rakamlarda yazilabilir

sozluk = {'REG' : ['RMSE',10],
          'LOJ' : ['MSE',20],
          'CART': ['SSE',30]}       #Sol tarafta key lerimiz var 
                                    #sag tarafata ise liste icinde iki tane
                                    #deger var

sozluk

len(sozluk) 



sozluk ['REG']



sozluk = {'REG' : {'RMSE':10,
                   'MSE' :20,
                   'SSE' :30}, 
          
    'log'          : {'RMSE':10,
                      'MSE' :20,
                      'SSE' :30},
   
    'Cart':          {'RMSE':10,
                      'MSE' :20,
                     'SSE'  :30}}        #Yani burada ic ice sozluk yapiyoruz
       

sozluk

sozluk['REG']              #Reg yazdigimizda reg sozlugunu cagirmis oluyoruz,
                           #ama ['REG']['SSE'] yazdigimizda
                           #reg in icideki kutuphaneyi cagirmis oluyoruz ellam

sozluk ['REG']['SSE']

#Sozluk - Eleman Eklemek & Degistirmek


sozluk = {'REG' : 'Regresyon Modeli' ,
          'Loj' : 'lojistik Regresyon',
          'CART': 'Classification and Reg'}

sozluk['GBM'] = 'Grandient Booting Mac'   # GBM en sona olacak sekilde eklendi

sozluk

sozluk ['REG'] = 'Coklu dogrusal Regresyon' #bu sekilde bir eleman uzerinde 
                                            #degistirme islemide yapabilirz

sozluk

sozluk[1] #yazdigimizda KeyError1 hatasi vermis olur cunku boyle bir ifade yok

sozluk[1] = 'Yapay sinir aglari'   #boylelikle 1 key degerine ve value olarakta 
                                   #Yapay Sinir Aglari yazmis olduk


sozluk 

l = [1]

l

sozluk[l] = 'yeni bir sey'    # listeyi sozluk e ekledigimiz zaman unhashable 
                              #yani tip hatasi aldik, sozluklerdei key sadece
                              #sabit veri yapasi olabilir ve str ve sayilar 
                              #sabit veri yapilaridir 
                              # genelde programlama yaparken key ler kesinlikle 
                              #degismez ama icerisindeki herzaman degisebilir 
                              #bundan dolari, yani key degerlweri hep sabittir

t = ('tuple',)

sozluk[t] = 'Yapay sinir aglari'
sozlu                            #burada tuple yi key olarak atayabildik


#Veri Yapilari - Setler
#1- setler sirasizdir
#2- setler degerleri essizdir
#3- degistirebilir
#4- farkli tipler barindirabilir


#SET olusturmak

s = set()

s

l = [1,'a','ali',123]
s =set(l)
s

t = ('a','ali')

s = set(t)
s

ali = 'lutfen_ata_bakma_uzaya_git'

type(ali)

s = set(ali)

s

l = ['ali','lutfen','ata','bakma','uzaya','git','git','ali','git' ]
     
l

s = set(l)
s

len(s)

#Eleman ekleme & cikarma

l = ['gelecegi', 'yazanlar']


s = set(l)

s

dir(s)

s.add('ile')

s

s.add('gelecege_git')
s

s.add('ile')
s


s.remove('ali')

s

s.discard('ali')  #hata uretmesin dersek bu fonksiyonu kullaniyoruz

#setler - klasik kume islemleri

# =============================================================================
# difference () ile iki kumenin farkini ya da "_" ifadesi
# intersection  () iki kume kesisimi ya da "&" ifadesi union () 
# iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari.
# =============================================================================


#difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)  # burada biz set 1 de olup iki de olmayan degerleri 
                       # sorguladik

set1.symmetric_difference(set2) # burada da ikisinde de olmayanlar nasil 
                                # buluyoruz onu gormus olduk 

#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)  #iki kumenin kesisenlerini busekilde buluyoruz
set2.intersection(set1)  #tersten yapincada ayni ifadeleri verdi

set1.union(set2)  #kumelerin birlesimi bu sekilde oluyor
                  #ancak butun elemanlardan 
                  #birertane aliyor 1 ve 3 u birerkere yazdi

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1   #set ikinin elemanlarini set bir in ifadesi olmus durumda

#Set sorgu islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])


# iki kumenin kesisiminin bos olup olmadiginin sorgulanmasi

set1.isdisjoint(set2)   # cvp false 


# bir kumenin butun elemanlarin baska bir kume icerisinde yer alip almaadigi
set1.issubset(set2)  #cvp true

#baska bir kumenin bir diger kumeyi kapsayip kapsamadigi

set2.issuperset(set1)  #cvp true evet set bir set ikiyi kapsiyor




# =============================================================================
# #Fonksiyonlara giris ve fonksiyon okuryazarligi
# =============================================================================





print()
print


# matematiksel islemler

4*4
23432/23424324
343452342343242-34545452342423
435324234234+23432432423432432
3424324234234324324-23432234324234324242423432432
3**3

#Fonksiyon nasil yazilir?

def kare_al(x):
    (x**2) #fonksiyon tanimlamak icin def yaziyoruz, 
           #fonksiyon ismi yazinca iki nokta yaziyoruz ve fonksiyonun 
           #ne yapacagini yaziyoruz
     
kare_al(3) #islem yapti ama print yazmadigimiz icin ekrana yazdirmadi

     
     
def kare_al(x):
    print(x**2) #boyle yazdik ekrana yazdirmak icin
    
    
kare_al(3)      # ve ekrana yazdirdi


#bilgi notuyla cikti uretmek



def kare_al(x):
    print(x**2)
    
    
 def kare_al(x):
    print('Girilen Sayinin Karesi:' + x**2)
    
kare_al(3)  #typeError aldik cunku str ifadeleri sadece str ile birlestirilir
    
    
  def kare_al(x):
    print('Girilen Sayinin Karesi:' + str(x**2))
    
kare_al(3) # ve cvp i almis oluyuyoruz yani biz sen islemi yap str olup olmadigi umrumda degi!


def kare_al(x):
    print('Girilen Sayi:' +
            str(x) + 
          'Karesi:' +
          str(x**2))
    
kare_al(3)
    
    
    




def kare_al(x):
    print('Girilen Sayi:' +
            str(x) + 
          ', Karesi:' +
          str(x**2))           #hersey guzel calisiyor ancak  
                               #Girilen Sayi:3Karesi:9 3 den sonra bir 
                               #bosluk birakma istiyoruz daha temiz gozukmesi icin
    

kare_al(3)

#iki argumanli fonksiyon tanimlamak

def kare_al(x):
    print(x**2)


def carpma_yap(x, y):
    print(x*y)
    
4334*32432423423423432


  
#On Tanimli Argumanlar

?print

def carpma_yap(x,y):
    print(x*y)

carpma_yap(3)        # yazdigimizda hata aliyoruz cunku y argumanini yazmadik



def carpma_yap(x, y = 1):
    print(x*y)


carpma_yap(3)  

#Argumanlarin Siralanmasi




def carpma_yap(x, y = 1):
    print(x*y)

carpma_yap(2,3)


#Ne zaman fonksiyon yazilir

#isi, nem, sarj
 40   25   90


(40+25)/90 #cvp 0.7222222222222222 degerini bulmus oluyoruz

def direk_hesap(isi, nem, sarj):
   print((isi + nem)/sarj)
   
direk_hesap(25,40,70)

#Ciktiyi girdi olarak kullanmak

def direk_hesap(isi, nem, sarj):
   print((isi + nem)/sarj)
   
cikti = direk_hesap(25,40,70)

cikti

print(cikti)



def direk_hesap(isi, nem, sarj):
   return((isi + nem)/sarj)
   
cikti = direk_hesap(25,40,70)   #return yazinca ekrana yazmis oluyor
                                #eger yazmis oldugumuz bir fonksiyonu ciktisin baska bir islemin girdisi v.s olacak sekilde kullanmak istiyorsak return olarak kullanmak zorundayiz
                               
cikti*9

def direk_hesap(isi, nem, sarj):
   return
   ((isi + nem)/sarj            #Onemli fonksiyon Return ifadesine geldiginde durur, bu yuzden return ifadesinin altindakilewre bakmadi!
    
                               
direk_hesap(25,40,70)                               


#Local ve Global Degiskenler


x = 10
y = 20

def carpma_yap(x,y):
    return x*y

carpma_yap(2,3)

def carpma_yap(x = 2,y =1):
    return x*y


carpma_yap(2,3)

#local etki alaninda global etki alanini degistirmek



def eleman_ekle(y):
    x.append(y)
    
    
x.append(1)    
x


x = []


def eleman_ekle(y):
    x.append(y)
    print(str(y) + ' ifasdesini eklendi')
    
eleman_ekle('ali')    
    
eleman_ekle('deli')    

x


# =============================================================================
# #Karar & Kontrol Yapilari
# =============================================================================

#true- False sorgulamalari

sinir = 5000

sinir == 4000

sinir == 5000

5 == 4

#If 

sinir = 50000
gelir = 40000

if gelir < sinir :
    print('Gelir sinirdan kucuk') 

#Aslinda burada su oluyor gelir sinirdan kucuk ve true bu yzden print de 
#'gelir sinirdan kucuk yazdi'




sinir = 50000
gelir = 40000

if gelir < sinir :
    print('Gelir sinirdan kucuk') 
    print(gelir*2)

#onemli birinci bolumde if in kosulunu yaziyoruz daha sonra
#koyup bu if in etki alanina girip yapmasini istedigimiz islemi elirtiyoruz

#Else



sinir = 50000
gelir = 40000

if gelir < sinir :
    print('Gelir sinirdan kucuk') 
else:
    print('Gelir sinirdan buyuk')    



sinir = 50000
gelir = 240000

if gelir < sinir :
    print('Gelir sinirdan kucuk') 
else:
    print('Gelir sinirdan buyuk')    

#diger ornek

sinir = 50000
gelir = 50000

if gelir == sinir:
    print('Gelir sinira esittir')
else:
    print('Gelir sinira esit degildir')    


#ELIF

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000


if gelir3 > sinir:
    print('Tebrikler, hediye kazandiniz')
    
elif gelir3 < sinir:
    print('Uyari!')
else:
    print('Lutfen tekrar deneyin')  

#mini uygulama


sinir = 50000
magaza_adi = input('Magza adi nedir?')
gelir = input('Gelirinizi Girin')

if gelir > sinir:
    print('Tebrikler, promosyon kazandiniz!')
elif gelir < sinir:
    print('Uyari!')
else:
    print('Takibe devam')    
    
#hata aldik  kullanicidan gelen bilgiler her zaman str olarak gelir
#ve int olarak islemek istersek bu durumda bu ifadeleri donusturmemiz gerekir




sinir = 50000
magaza_adi = input('Magza adi nedir?')
gelir =int(input('Gelirinizi Girin'))

if gelir > sinir:
    print('Tebrikler, promosyon kazandiniz!')
elif gelir < sinir:
    print('Uyari!')
else:
    print('Takibe devam')   
    
    

sinir = 50000
magaza_adi = input('Magza adi nedir?')
gelir =int(input('Gelirinizi Girin'))

if gelir > sinir:
    print('Tebrikler:' + magaza_adi + ' promosyon kazandiniz!')
elif gelir < sinir:
    print('Uyari! Cok dusuk gelir:' + str(gelir))
else:
    print('Takibe devam') 


#Donguler - for

ogrenci = ['ali','veli','isik','berk']

ogrenci[0]
ogrenci[1]
ogrenci[2]

for i in ogrenci:
    print(i)

print(ogrenci[1])



#For a devam


maaslar = [1000,2000,3000,4000,5000]

maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]


for i in maaslar:
    print(i)


print(maaslar[4])


maaslar = [1000,2000,3000,4000,5000]

maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]


for i in maaslar:
    print(maas)


#dongu ve fonksiyonlari birlikte kullanmak

def kare_al(x):
    print(x**2)
    

maaslar = [1000,2000,3000,4000,5000]

kare_al(2)

for i in maaslar:
    print(i)


#maaslara yuzde 20 zam yapildi gerekli code lari yazin amk!


1000*20/100 +1000

maaslar[0]*20/100 + maaslar[0]
maaslar[2]*20/100 + maaslar[2]
maaslar[3]*20/100 + maaslar[3] 
#dongu yazilacak binlerce insanin maasini bu sekilde arttiramayiz


#dongu yazilacak
#fonksiyon yazilacak

def yeni_maas(x):
    print(x)
    
yeni_maas(4)    


def yeni_maas(x):
    print(x*20/100 + x)

yeni_maas(1000)  
yeni_maas(2000) 
yeni_maas(3000) 

#fonksiyonu yazdik ama binlerce kisi var hepsin yazamayiz ve dongu yaziyorz
#dongu

for i in maaslar:
    yeni_maas(i)
    
 

maaslar = [1000,2000,3000,4000,5000]


def yeni_maas(x):
    print(x*20/100 + x)

for i in maaslar:
    yeni_maas(i)
    
#mini uygulama
#if, for fonksiyonlari birlikte kullanmak

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100 + x)
    
def maas_alt(x):
    print(x*20/100 + x)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)


#break & continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

maaslar.sort()
maaslar          #maaslar karisik duzenlemek istiyorlar ouzden sort yazdik


for i in maaslar:
    if i == 3000:
        print('kesildi')
        break
    print(i)
    

#while

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)
    
#biz burada sunu yapiyoruz sayi 10 kucuk oldugu surece bu islemi yap dedik
#sayi 10 dan kucuk dedik ama 10 da var true dondugu icin, 
#sayi 9 oldugunda +1 oldu ve 10 geldi.



# =============================================================================
# #Nesne Yonelimli Programlama
# =============================================================================

#sinif nedir?


class VeriBilimci():
    print('bu bir siniftir')


#Sinif ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller =[]
 
#Siniflarin ozellikleri    
VeriBilimci.bolum    
VeriBilimci.sql

#Siniflarin ozellikleini degistirmek
VeriBilimci.sql = 'Hayir'
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append('Python')

veli = VeriBilimci()
veli.sql

veli.bildigi_diller

#Ornek ozellikler

class VeriBilimci():
    def__init__(self):
        self.bildigi_diller = []


ali = VeriBilimci()
ali.bildigi_diller


veli = VeriBilimci()
veli.bildigi_diller


ali.bildigi_diller.append('Python')
ali.bildigi_diller



veli.bildigi_diller
veli.bildigi_diller.append('R')
veli.bildigi_diller

VeriBilimici.bildigi_diller #bunu yazinca hata aliyoruz ve sunu yaziyoruz


class VeriBilimci():
    bildigi_diller =['R','PYTHON']
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller =[]
    def __init__(self):
        self.bildigi_diller = []
        
ali.bolum        

veli.bildigi_diller

#ornek metodlar



class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)  
        #yeni dil ogrenmesini istedigimiz icin yeni fonksiyon yazdik
        
    

ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()

ali.bildigi_diller
ali.bolum


dir(VeriBilimci)

VeriBilimci.dil_ekle
VeriBilimci.dil_ekle('R')


ali.dil_ekle('R')

ali.bildigi_diller

veli.dil_ekle('Python')
veli.bildigi_diller



#Miras yapilari (inheritance)

class Employees():
     def __init__(self):
        self.FirstName = ''
        self.LastName = ''
        self.Address = ''


class DataScience(Employees):
     def __init__(self):
        self.Programming =''
     

veribilimci1 = DataScience()
veribilimci1.


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ''
        



class Employees():
     def __init__(self, FirstName, LastName, Address) :
        self.FirstName = FirstName
        self.LastName =  LastName
        self.Address =  Address

ali =Employees('a','b','c')

ali.FirstName


# =============================================================================
# Python'da Fonksiyonel Programlama
# =============================================================================

#Fonksiyonlar dilin bastacidir
#birinci sinif neslenerdir
#Yan etkisis fonksiyonlar (stateless, girdi-cikti)
#Yuksek seviye fonksiyonlar
#Vektorel operasyon

#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1: Yan etki


A = 9

def impure_sum(b):
    return b+A

def pure_sum(a,b):
    return a+b

impure_sum(6)

pure_sum(3,4)

#Ornek2 Olumcul yan etkiler

#cok uzundu yazmadim acip tekrar bakabirlisn istersn


#Isimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a,b):
    return a + b

old_sum(4,5)

new_sum = lambda a,b : a+b
new_sum(4,5)


#Vektorel Operasyonlar (Vectorel Operations)

a = [1,2,3,4]
b = [2,3,4,5]

ab =[]

range(0, len(a))

for i in range(0, len(a)):
    print(i)


for i in range(0, len(a)):
    ab.append(a[i]*b[i])



ab   #iki donguyu carptik fakat soz konusu matematik, veribilimi, istatistik ve makina ogrenmesi oldugunda asla b u tip dongulere girmiyoruz vektorel operasyona girtiyoruz

import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
                    
a*b                      #gordugumuz gibi numpy ile daha az vakit harcayarak yaptik

#map & filter & reduce

#lambda isimsiz fonksiyon

liste = [1,2,3,4,5]

for i in liste:
    print(i+10)
    
list(map(lambda x: x + 10, liste))    

# Map fonksiyonu bize verilen bir neslenin uzerinde tanimlanacak bir fonksiyonu calistirma imkani verir

#filter

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x % 2 == 0, liste))

#Filter Fonksiyonu bir nesle alacagini baska bir interanatif bir nesle olusturur


#Reduce

from functools import reduce

liste = [1,2,3,4,]
reduce(lambda a,b: a+b, liste)


#Modul olusturmak


#Hatalar / istisnalar (exceptions)

a = 10
b = 0

a/b

try:
    print(a/b)
except ZeroDivisionError:
    print('payda da sifir olmaz')


#tip hatasi

a = 10
b = '2'

a/b

try:
    print(a/b)
except TypeError:
    print('payda da sifir olmaz')






















































































































+











    




















































































-





















