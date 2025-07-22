import tkinter as tk

pencere = tk.Tk()
pencere.title("Belediye Arıza Takip Sistemi")
pencere.geometry("400x300")

etiket = tk.Label(pencere, text="Hoş geldiniz!", font=("Arial", 16))
etiket.pack(pady=20)

pencere.mainloop()
