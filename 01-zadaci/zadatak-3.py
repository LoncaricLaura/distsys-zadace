""" 
Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error.
(“cijena”,“naziv”,“kolicina”) (Moze i u dvije linije) Vraća novi nested
dictionary s ključem “ukupno” i dictionary sa ključem “artikli” i listom
svih odabranih artikala te “cijena” s ukupnom cijenom računa. (Ne treba
biti One-liner)
"""
def function(lista):
    assert isinstance(lista, list)
    assert all(isinstance(x, dict) for x in lista)
    assert all(list(x.keys()) == ["cijena", "naziv", "kolicina"] for x in lista)
    return {"ukupno": {"artikli": [x["naziv"] for x in lista], "cijena": sum(x["cijena"] * x["kolicina"] for x in lista)}}

print(function([{"cijena":8,"naziv":"Kruh","kolicina":1}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}]))
   