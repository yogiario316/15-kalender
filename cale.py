import tkinter as tk
from tkcalendar import Calendar

def show_date():
    selected_date = cal.get_date()
    lbl_date.config(text=f"Selected Date: {selected_date}")

root = tk.Tk()
root.title("Kalender GUI")

cal = Calendar(root, selectmode='day', year=2024, month=5, day=23)
cal.pack(pady=20)

btn_show = tk.Button(root, text="Show Date", command=show_date)
btn_show.pack(pady=10)

lbl_date = tk.Label(root, text="")
lbl_date.pack(pady=10)

lbl_credit = tk.Label(root, text="Credit: Yogi Ario")
lbl_credit.pack(pady=10)

root.mainloop()
