"""
Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
linije)
"""
def function(lista):
  assert all(isinstance(x, str) for x in lista)
  return [x for x in lista if len(x) > 4] 

print(function(["Pas", "Macka", "Stol"]))
