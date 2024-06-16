import tkinter as tk
from tkcalendar import Calendar

def show_date():
    selected_date = cal.get_date()
    lbl_date.config(text=f"Selected Date: {selected_date}")

# Membuat instance dari Tk
root = tk.Tk()
root.title("Kalender GUI")

# Membuat kalender
cal = Calendar(root, selectmode='day', year=2024, month=5, day=23)
cal.pack(pady=20)

# Membuat tombol untuk menampilkan tanggal yang dipilih
btn_show = tk.Button(root, text="Show Date", command=show_date)
btn_show.pack(pady=10)

# Label untuk menampilkan tanggal yang dipilih
lbl_date = tk.Label(root, text="")
lbl_date.pack(pady=10)

# Menambahkan label credit
lbl_credit = tk.Label(root, text="Yogi Ario")
lbl_credit.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
