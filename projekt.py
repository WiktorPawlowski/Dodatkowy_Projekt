import tkinter as tk
from tkinter import *

Menu = tk.Tk()
Menu.title("Książka Kucharska")
Menu.geometry("700x400")

#############################################################################################################
#                                                  MENU
def wyjscie():
    Menu.destroy()

##############################################################################################################
#                                                 ZUPY
def przerzuc_na_okno_zupy():
    Menu.withdraw()
    okno_zupy = tk.Toplevel()
    okno_zupy.title("Zupy")
    okno_zupy.geometry("700x400")

    wybor_zupy = tk.Label(okno_zupy, text="Wybierz przepis na zupę:", font=("Arial", 20), fg="blue")
    wybor_zupy.place(x=200, y=30)

    rosol = tk.Button(okno_zupy, text="Rosół", width=30)
    rosol.place(x=120, y=100)

    ogorkowa = tk.Button(okno_zupy, text="Ogórkowa", width=30)
    ogorkowa.place(x=350, y=100)

    barszcz_czerwony = tk.Button(okno_zupy, text=("Barszcz czerwony"), width=30)
    barszcz_czerwony.place(x=120, y= 140)
################################################################################################################

def przerzuc_na_okno_sniadania():
    Menu.withdraw()
    okno_sniadania = tk.Toplevel()
    okno_sniadania.title("Śniadania")
    okno_sniadania.geometry("700x400")

def przerzuc_na_okno_obiady():
    Menu.withdraw()
    okno_obiady = tk.Toplevel()
    okno_obiady.title("Obiady")
    okno_obiady.geometry("700x400")

def przerzuc_na_okno_kolacje():
    Menu.withdraw()
    okno_kolacje = tk.Toplevel()
    okno_kolacje.title("Kolacje")
    okno_kolacje.geometry("700x400")

def przerzuc_na_okno_desery():
    Menu.withdraw()
    okno_desery = tk.Toplevel()
    okno_desery.title("Desery")
    okno_desery.geometry("700x400")

def przerzuc_na_okno_przekaski():
    Menu.withdraw()
    okno_przekaski = tk.Toplevel()
    okno_przekaski.title("Przekąski")
    okno_przekaski.geometry("700x400")

napis_menu = tk.Label(Menu, text="Menu Książki", font=("Arial", 20), fg="red")
napis_menu.pack()

powitanie = tk.Label(Menu, text="Witaj w Menu książki kucharskiej!", font=("Arial", 18), fg="blue")
powitanie.place(x=180, y=60)

wybierz = tk.Label(Menu, text="Wybierz katygorię:", font=("Arial", 18), fg="blue")
wybierz.place(x=250, y=110)

napis_wyjsc = tk.Label(Menu, text="Naciśnij przycisk jeżeli chcesz wyjść: ", font=("Arial", 17), fg="blue")
napis_wyjsc.place(x=160, y=300)



zupy = tk.Button(Menu, text="Zupy", width=30, command=przerzuc_na_okno_zupy)
zupy.place(x=130, y=170)

sniadania = tk.Button(Menu, text="Śniadania", width=30, command=przerzuc_na_okno_sniadania)
sniadania.place(x=360, y=170)

obiady = tk.Button(Menu, text="Obiady", width=30, command=przerzuc_na_okno_obiady)
obiady.place(x=130, y=210)

kolacje = tk.Button(Menu, text="Kolacje", width=30, command=przerzuc_na_okno_kolacje)
kolacje.place(x=360, y=210)

desery = tk.Button(Menu, text="Desery", width=30, command=przerzuc_na_okno_desery)
desery.place(x=130, y=250)

przekaski = tk.Button(Menu, text="Przekąski", width=30, command=przerzuc_na_okno_przekaski)
przekaski.place(x=360, y=250)

wyjsc = tk.Button(Menu, text="Wyjdź", width=30, command=wyjscie)
wyjsc.place(x=240, y=340)







Menu.mainloop()