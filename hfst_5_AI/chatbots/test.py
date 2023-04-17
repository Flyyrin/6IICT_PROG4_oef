""" Oefening 1: maak de gegeven GUI na (zie pasen_1.exe).

De GUI is een "Klikker-spel". Door op de knop te klikken, verhoogt de gebruiker een teller.
Hoeveel de teller verhoogt, hangt af van de waarde in de Entry bovenaan.

Let zeker op volgende zaken:
    - De titel van de app is "Klikker-spel".
    - Beide Entries hebben een startwaarde gelijk aan 0.
    - De gebruikte FONT voor alle elementen is "Helvetica" met een gwindowte van 14.
    - De bovenste Entry moet als waarde een getal bevatten. 
      Is dit niet zo wanneer de gebruiker klikt? Dan reset de Entry onderaan terug naar 0.

Breng commentaar aan bij de code. Dit moet het doel/werking ervan uitleggen.
Je mag verschillende regels code samen uitleggen.
"""
from tkinter import *

def tel_op():
  getal_waarde = waarde.get()
  teller_waarde = teller.get() 

  try:
    teller_waarde = int(teller_waarde)
  except:
    teller_waarde = 0

  try:
    getal_waarde = int(getal_waarde)
    teller_waarde += getal_waarde
  except:
    teller_waarde = 0

  teller.delete(0, END)
  teller.insert(0, teller_waarde)

window = Tk()
window.title("Klikker-spel")
window.option_add("*Font", "Helvetica 14")

Label(window, text="Verhoog waarde met:").grid(column=0, row=0)
waarde = Entry(window)
waarde.insert(0, "0")
waarde.grid(column=1, row=0)

Button(window, text="Klik", width=30, command=tel_op).grid(column=0, row=1, columnspan=2)

Label(window, text="Teller:").grid(column=0, row=2)
teller = Entry(window)
teller.insert(0, "0")
teller.grid(column=1, row=2)

window.mainloop()