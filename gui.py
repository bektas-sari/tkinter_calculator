import customtkinter as ctk

# Arayüz penceresini oluştur
ctk.set_appearance_mode("dark")  # "light" veya "dark"
ctk.set_default_color_theme("blue")

class ModernHesapMakinesi(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Hesap Makinesi")
        self.geometry("350x500")
        self.resizable(False, False)

        self.ekran = ctk.CTkEntry(self, font=("Arial", 24), width=320, height=50, justify="right")
        self.ekran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        butonlar = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for btn in butonlar:
            text, row, col = btn[:3]
            colspan = btn[3] if len(btn) == 4 else 1
            action = lambda x=text: self.buton_tikla(x)
            
            ctk.CTkButton(self, text=text, command=action, width=75, height=75, font=("Arial", 20)).grid(
                row=row, column=col, columnspan=colspan, padx=5, pady=5
            )

    def buton_tikla(self, deger):
        if deger == "C":
            self.ekran.delete(0, "end")
        elif deger == "=":
            try:
                sonuc = eval(self.ekran.get())
                self.ekran.delete(0, "end")
                self.ekran.insert("end", str(sonuc))
            except:
                self.ekran.delete(0, "end")
                self.ekran.insert("end", "Hata")
        else:
            self.ekran.insert("end", deger)

if __name__ == "__main__":
    app = ModernHesapMakinesi()
    app.mainloop()
