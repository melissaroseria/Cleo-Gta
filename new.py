import os
import shutil
import zipfile

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    print(CYAN + "=" * 40)
    print(GREEN + "Powered : Copilot")
    print(YELLOW + "Github  : melissaroseria/Cleo-Gta")
    print(CYAN + "=" * 40 + RESET)
    print(MAGENTA + "🎮 GTA CLEO MOD MENU")
    print(BLUE + "[1] : 100 Save Aktarma Etkinleştir" + RESET)
    print(BLUE + "[2] : Save Dosyalarını Zip Paketle (ZArchiver için)" + RESET)
    print(CYAN + "=" * 40 + RESET)

def activate_save_transfer():
    source_dir = "./save"
    target_dir = "/storage/emulated/0/Android/data/com.rockstargames.gtasa/files"

    if not os.path.exists(source_dir):
        print(RED + "[!] Save klasörü bulunamadı." + RESET)
        return

    if not os.path.exists(target_dir):
        print(RED + "[!] Hedef klasöre erişim yok. Android 11+ bariyeri olabilir." + RESET)
        print(YELLOW + "[i] Alternatif: Menüden [2] seçeneği ile zip oluştur, ZArchiver ile aç." + RESET)
        return

    files = [f for f in os.listdir(source_dir) if f.endswith(".b")]
    if not files:
        print(YELLOW + "[•] Kopyalanacak .b uzantılı dosya bulunamadı." + RESET)
        return

    print(GREEN + "[✓] Aktarım başlıyor..." + RESET)
    for file in files:
        src = os.path.join(source_dir, file)
        dst = os.path.join(target_dir, file)
        try:
            shutil.copy2(src, dst)
            print(BLUE + f"[+] Kopyalandı: {file}" + RESET)
        except Exception as e:
            print(RED + f"[!] Hata: {file} → {e}" + RESET)

    print(GREEN + "[✓] Aktarım tamamlandı. Melissa Roseria uçtu!" + RESET)

def zip_saves():
    source_dir = "./save"
    output_zip = "/storage/emulated/0/Download/GTASA_100SAVE.zip"

    if not os.path.exists(source_dir):
        print(RED + "[!] Save klasörü bulunamadı." + RESET)
        return

    files = [f for f in os.listdir(source_dir) if f.endswith(".b")]
    if not files:
        print(YELLOW + "[•] Zip içine koyulacak .b dosyası bulunamadı." + RESET)
        return

    with zipfile.ZipFile(output_zip, "w") as zipf:
        for file in files:
            zipf.write(os.path.join(source_dir, file), file)
            print(BLUE + f"[+] Zip’e eklendi: {file}" + RESET)

    print(GREEN + f"[✓] Zip oluşturuldu: {output_zip}" + RESET)
    print(YELLOW + "[i] Şimdi ZArchiver ile açıp GTA klasörüne taşıyabilirsin." + RESET)

def main():
    banner()
    choice = input(YELLOW + "Seçiminizi girin: " + RESET)
    if choice == "1":
        activate_save_transfer()
    elif choice == "2":
        zip_saves()
    else:
        print(RED + "[!] Geçersiz seçim." + RESET)

if __name__ == "__main__":
    main()
