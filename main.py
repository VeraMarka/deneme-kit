import os
import colorama

# colorama kütüphanesini init et
colorama.init()

# Terminal ekranını temizle
os.system("clear")

# Figlet ile metni oluştur
text = "Zindan"
figlet_command = f"figlet {text}"
figlet_output = os.popen(figlet_command).read()

# Renkli metni yazdır
colored_text = "\033[91m\033[1m" + figlet_output + "\033[0m"  # Kırmızı ve kalın renk
print(colored_text)

isim = input("Kullanıcı İsmi: ")
print("\033[92m\033[1m[1] Pingini Ölç\033[0m")
print("\033[95m\033[1m[2]Nmap Kullan\033[0m")
print("\033[90m\033[1m[3]Whoİs Kullan\033[0m")
print("\033[94m\033[1m[4]TraceRoute Kullan\033[0m")

secim = input("Seçim yapın: ")

if secim == "1":
    ip = input(f"Merhaba {isim} Pingini Ölçmek istediğin ip adresi: ")
    os.system(f"ping {ip}")

elif secim == "2":
    os.system("pkg install nmap")
    os.system("clear")
    os.system("figlet Zindan")
    print("[1] Ip Adresi Veya Alan Adı İçin Arama Yap")
    print("[2] Belirli Bir Port Aralığı İçin Arama Yap")
    print("[3] Bir İp Aralığını Tarama Yap")
    print("[4] Hızlı Arama Yap")
    print("[5] Servis Ve Sistem Bilgilerini Görüntüle (Bakımda)")
    print("[6] Detaylı Çıktı İle Arama Yapın (Bakımda)")
    print("[7] İşletim Sistemine Arama Yap (Bakımda)")
    print("[8] Açık Portları Belirle (Bakımda)")
    print("[9] UDP Taraması Yapma (Bakımda)")

    nmap_secim = input("Kullanmak İstediğiniz Program: ")
    if nmap_secim == "1":
        sjs = input("İp Adresi Veya Url Giriniz: ")
        os.system(f"nmap {sjs}")
    elif nmap_secim == "2":
        site = input("Siteyi Giriniz (http olmadan): ")
        os.system(f"nmap -p 1-1000 {site}")
    elif nmap_secim == "3":
        ip_ara = input("ip ve port örnek=192.163.1.1/24: ")
        os.system(f"nmap {ip_ara}")
    elif nmap_secim == "4":
        hedef = input("site giriniz: ")
        os.system(f"nmap -F {hedef}")
    else:
        print("Geçersiz seçim!")

elif secim == "3":
    os.system("pkg install whois")
    whois = input("ip veya site girin: ")
    os.system(f"whois {whois}")

elif secim == "4":
    print("bakımda")

else:
    print("Geçersiz seçim!")
