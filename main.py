import colorama
from colorama import Fore, Style

def hesap_makinesi():
    colorama.init(autoreset=True)

    print(Fore.CYAN + "********** HESAP MAKİNESİ **********")
    print(Fore.GREEN + "1: Toplama")
    print(Fore.YELLOW + "2: Çıkarma")
    print(Fore.MAGENTA + "3: Çarpma")
    print(Fore.RED + "4: Bölme")
    print(Fore.BLUE + "0: Çıkış\n")

    while True:
        secim = input(Fore.WHITE + "Yapmak istediğiniz işlemi seçin (0-4): ")

        if secim == '0':
            print(Fore.CYAN + "Çıkış yapılıyor...")
            break

        if secim not in ['1', '2', '3', '4']:
            print(Fore.RED + "Geçersiz seçim! Lütfen 1-4 arasında bir değer girin.")
            continue

        try:
            sayilar = list(map(float, input(Fore.WHITE + "Sayıları boşlukla ayırarak girin: ").split()))

            if len(sayilar) < 2:
                print(Fore.RED + "En az iki sayı girmelisiniz!")
                continue

            if secim == '1':
                print(Fore.GREEN + f"Sonuç: {sum(sayilar)}")
            elif secim == '2':
                sonuc = sayilar[0]
                for s in sayilar[1:]:
                    sonuc -= s
                print(Fore.YELLOW + f"Sonuç: {sonuc}")
            elif secim == '3':
                sonuc = 1
                for s in sayilar:
                    sonuc *= s
                print(Fore.MAGENTA + f"Sonuç: {sonuc}")
            elif secim == '4':
                sonuc = sayilar[0]
                try:
                    for s in sayilar[1:]:
                        sonuc /= s
                    print(Fore.RED + f"Sonuç: {sonuc}")
                except ZeroDivisionError:
                    print(Fore.RED + "Hata: Sıfıra bölme yapılamaz!")

        except ValueError:
            print(Fore.RED + "Hata: Lütfen geçerli sayılar girin.")

if __name__ == "__main__":
    hesap_makinesi()
