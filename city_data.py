import requests  #apilere istek göndermek 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cou=['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Bonaire, Sint Eustatius and Saba', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina', 'Saint Barthélemy', 'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada', 'Cocos (Keeling) Islands', 'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon', 'Congo, The Democratic Republic of the', 'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curaçao', 'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France', 'Faroe Islands', 'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar', 'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Heard Island and McDonald Islands', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'British Indian Ocean Territory', 'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jersey', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis', 'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Liberia', 'Libya', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat', 'Martinique', 'Mauritius', 'Malawi', 'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'Nicaragua', 'Niue', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay', 'Palestine, State of', 'French Polynesia', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'South Georgia and the South Sandwich Islands', 'Saint Helena, Ascension and Tristan da Cunha', 'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Türkiye', 'Tuvalu', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Uganda', 'Ukraine', 'United States Minor Outlying Islands', 'Uruguay', 'United States', 'Uzbekistan', 'Holy See (Vatican City State)', 'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Viet Nam', 'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']

ecl=[]
for country in cou:

  url=f"https://restcountries.com/v3.1/name/{country}"
  response=requests.get(url)
  if response.status_code != 200:
     print(f"Hata: {country} veriler alınamadı")
     continue
     
  data=response.json()
  try:

      ülke=data[0]["name"]["common"] 
      Başkent=data[0]["capital"][0]
      Nüfus=data[0]["population"]
      Para_birimi=list(data[0]["currencies"].keys())[0]
      Bölge=data[0]["region"]
      Konum=data[0]["latlng"]
      Saat_dilimi=data[0]["timezones"]
      Trafik_yönü=data[0]["car"]["side"]
      Diller=data[0]["languages"]
      alan=data[0]["area"]
      bm=data[0]['unMember']
    
    
      ecl.append({"ülke": ülke ,
                  "Başkent": Başkent,
                  "Nüfus":Nüfus ,
                  "Para birimi":Para_birimi,
                  "Bölge" :Bölge   ,
                  "Saat_dilimi":Saat_dilimi,             
                  "bm":bm,
                  "Trafik_yönü": Trafik_yönü,
                  "Diller":Diller,
                  "Alan":alan,
                  "Konum": Konum 
                  
                  
                   })
   
  except Exception as e:
     print(f"hata: {e}")
cuty=pd.DataFrame(ecl)

cuty.to_excel("C:\\Users\\buğra\\Desktop\\journee.xlsx", index=True)

ge=pd.read_excel("C:\\Users\\buğra\\Desktop\\journee.xlsx")
# hatalı eksik verilerin sayısnı verir
print(ge.isnull().sum())
# nufus yoğunluğu 
ge['nufus_yoğunlu']=ge['Nüfus'] / ge['Alan']

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

parabr=ge['Para birimi'].value_counts().reset_index().head(20)
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