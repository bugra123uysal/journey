import requests  #apilere istek göndermek 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xml.etree.cElementTree as ET
import pycountry
"""
    currency_code: Para birimi kodu (USD, EUR...)
    xml_root: TCMB XML verisinin kökü
    return: Döviz satış fiyatı float veya None
"""
""" TCMB’den gelen XML verisinden bir para biriminin döviz satış fiyatını bulur """
def get_exchange(currency_code ,  xml_root):
    
   
    # döviz fiyatları api
      
    aal=xml_root.find(f".//Currency[@Kod='{currency_code}']/ForexSelling")

    if aal is not None and aal.text:
          
        try:
            return float(aal.text.replace(",", "."))
           # print(döv_fiy , fiyat) 
     
        except ValueError:
             
             return None
    return None
     
# ülke verisini çeken foksiyon
"""
    country: ülke ismi
    xml_root: TCMB XML kökü
    return: dictionary veya None
    """
""" country parametresindeki ülke için RestCountries API’den veri çeker """
def get_countr_data(country, xml_root):
    

    url=f"https://restcountries.com/v3.1/name/{country}"
    response=requests.get(url)
    if response.status_code != 200:
      print(f"Hata: {country} veriler alınamadı")
      return None
    
    data=response.json()[0]
    try:
      
      para_birimi=list(data.get("currencies", {}).keys())[0] if "currencies" in data  else None
      fiyat=get_exchange(para_birimi, xml_root) if para_birimi else None

             
      return{
          
          "ülke":data.get("name", {}).get("common", None),
          "Başkent":data.get("capital",[None])[0] if data.get("capital") else None,
          "Nüfus": data.get("population",None ),
          "Para_birimi": para_birimi,
          "döviz_fiyatı":fiyat,
          "Bölge":data.get("region", None),
          "Saat_dilimi":data.get("timezones", None),
          "Konum":data.get("latlng", None),
          "Trafik_yönü":data.get("car", {}).get("side", None),
          "Diller":list(data.get("languages",{}).values()) if data.get("languages") else None,
          "alan":data.get("area",None),
          "bm": data.get('unMember')
    
      } 
    
    except Exception as e:
        print(f"hata:{e}")
        return None
  
countries=[c.name for c in pycountry.countries]
# döviz fiyatları api
ddöv=f"https://www.tcmb.gov.tr/kurlar/today.xml"
respon=requests.get(ddöv)
respon.encoding= "utf-8"
root=ET.fromstring(respon.text)


ecl=[]

for country in countries:
    country_info= get_countr_data(country , root)
    if country_info:
        ecl.append(country_info)
    


cuty=pd.DataFrame(ecl)

cuty.to_excel("C:\\Users\\buğra\\Desktop\\journee.xlsx", index=True)

ge=pd.read_excel("C:\\Users\\buğra\\Desktop\\journee.xlsx")
# hatalı eksik verilerin sayısnı verir
print(ge.isnull().sum())


# nufus yoğunluğu 
ge['nufus_yoğunlu']=ge['Nüfus'] / ge['alan']

# trafik yönü 
sayısı=ge['Trafik_yönü'].value_counts().reset_index().head(20)
sayısı.columns=['adet', 'trafik_yonu']
sns.barplot(x="adet", y="trafik_yonu", data=sayısı)
plt.title("Ülkelerin Trafik Yönü Dağılımı")
plt.xlabel("Ülke Sayısı")
plt.ylabel("Trafik Yönü")
plt.show()
  
# bölge deki ülke sayıları 
bölsayı=ge['Bölge'].value_counts().reset_index().head(20)
bölsayı.columns=["sayı","Bölge"]
sns.barplot(y="Bölge" , x="sayı",data=bölsayı)
plt.title("Bölgelere Göre Ülke Sayısı")
plt.xlabel("Ülke Sayısı")
plt.ylabel("Bölge")
plt.show()

# bm de olan ve olmayan  ülke sayısı
Bmsay=ge['bm'].value_counts().reset_index().head(20)
Bmsay.columns=["sayı","bm"]
sns.barplot(y="bm",x="sayı",data=Bmsay)
plt.title("BM Üyeliğine Göre Ülke Sayısı")
plt.xlabel("Ülke Sayısı")
plt.ylabel("BM Üyesi / Değil")
plt.show()

# para birimini kullanan ülke sayıları

parabr=ge['Para_birimi'].value_counts().reset_index().head(20)
parabr.columns=["adet","birim"]
sns.barplot(y="birim", x="adet", data=parabr)
plt.title("En Çok Kullanılan Para Birimleri (İlk 20)")
plt.xlabel("Ülke Sayısı")
plt.ylabel("Para Birimi")
plt.xticks(rotation=90)
plt.show()

# dillerin kullanım sayıları 
dill=ge['Diller'].value_counts().reset_index().head(20)
dill.columns=["adet","dil"]
sns.barplot(y="dil",x="adet", data=dill)
plt.title("En Çok Kullanılan Diller (İlk 20)")
plt.xlabel("Ülke Sayısı")
plt.ylabel("Dil")
plt.xticks(rotation=90)
plt.show()
