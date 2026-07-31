import os
import numpy as np
from sklearn.cluster import KMeans
from PIL import ImageGrab

# Trik agar warna ANSI berfungsi di terminal Windows standar
os.system('')

def rgb_to_hex(rgb):
    """Mengubah format komponen RGB menjadi string HEX (#RRGGBB)"""
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def format_warna_terminal(rgb, kode_hex):
    """Membuat blok warna menggunakan ANSI escape code 24-bit (True Color)"""
    r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
    blok_warna = f"\033[48;2;{r};{g};{b}m        \033[0m"
    return f"{blok_warna}  {kode_hex.upper()}"

def proses_warna_clipboard(jumlah_warna=5):
    print("\n[Sistem]: Membaca data dari clipboard...")

    img = ImageGrab.grabclipboard()

    if img is None:
        return "Gagal: Clipboard kosong atau bukan berbentuk gambar. Silakan ulangi screenshot."

    if isinstance(img, list):
        try:
            from PIL import Image
            img = Image.open(img[0])
        except Exception as e:
            return f"Gagal membaca file gambar: {e}"

    img = img.convert('RGB')
    matriks_gambar = np.array(img)
    barisan_piksel = matriks_gambar.reshape(-1, 3)

    print(f"[Sistem]: Menganalisis total {len(barisan_piksel):,} piksel gambar...")

    kmeans = KMeans(n_clusters=jumlah_warna, random_state=42, n_init='auto')
    kmeans.fit(barisan_piksel)

    titik_warna_rgb = kmeans.cluster_centers_

    hasil_warna = []
    for rgb in titik_warna_rgb:
        hex_code = rgb_to_hex(rgb)
        hasil_warna.append((rgb, hex_code))

    return hasil_warna

def main():
    print("=============================================")
    print("   APLIKASI PENCARI WARNA DARI SCREENSHOT   ")
    print("=============================================")
    print("Cara penggunaan:")
    print("1. Tekan [Win + Shift + S] untuk men-screenshot area layar.")
    print("2. Kembali ke terminal.")

    # Memulai perulangan utama sistem
    while True:
        print("\n---------------------------------------------")
        input("-> Tekan [ENTER] jika gambar sudah siap di clipboard...")

        target_warna = 5
        hasil = proses_warna_clipboard(jumlah_warna=target_warna)

        if isinstance(hasil, list):
            print(f"\n[Hasil]: Berhasil menemukan {target_warna} warna paling dominan:")
            print("---------------------------------------------")
            for indeks, (rgb, kode_hex) in enumerate(hasil, 1):
                tampilan_visual = format_warna_terminal(rgb, kode_hex)
                print(f" Warna {indeks} : {tampilan_visual}")
            print("---------------------------------------------")
        else:
            print(f"\n{hasil}")

        # Logika pertanyaan perulangan
        # .strip().lower() digunakan agar input variasi 'Y', 'y ', atau 'n' tetap terbaca akurat
        pilihan = input("Pick color again? (y/n) [default: y]: ").strip().lower()

        # Jika user memilih 'n', hentikan perulangan dan keluar dari program
        if pilihan == 'n':
            print("\nTerima kasih telah menggunakan aplikasi ini! Sampai jumpa.")
            break

if __name__ == "__main__":
    main()
