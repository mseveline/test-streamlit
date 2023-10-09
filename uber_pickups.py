import tkinter as tk

def tambahkan():
    try:
        angka1 = float(entry_angka1.get())
        angka2 = float(entry_angka2.get())
        hasil = angka1 + angka2
        label_hasil.config(text=f'Hasil: {hasil}')
    except ValueError:
        label_hasil.config(text='Masukkan angka yang valid')

# Membuat jendela utama
root = tk.Tk()
root.title('Kalkulator Sederhana')

# Membuat input field dan label
label_angka1 = tk.Label(root, text='Angka 1:')
label_angka1.pack()
entry_angka1 = tk.Entry(root)
entry_angka1.pack()

label_angka2 = tk.Label(root, text='Angka 2:')
label_angka2.pack()
entry_angka2 = tk.Entry(root)
entry_angka2.pack()

# Membuat tombol untuk menghitung hasil
tombol_hitung = tk.Button(root, text='Hitung', command=tambahkan)
tombol_hitung.pack()

# Membuat label untuk menampilkan hasil
label_hasil = tk.Label(root, text='')
label_hasil.pack()

root.mainloop()
