"""
Funkcija prima listu tuple-a o studentima (id, ime, prezime). Vraća novu
sortiranu po id-u (manji->veci) listu dictionary-a o studentima kojima ime
i prezime počinje istim slovom. (One-liner u return-u)
"""
def function(lista):
    return sorted([{"id": x[0], "ime": x[1], "prezime": x[2]} for x in lista if x[1][0] == x[2][0]], key = lambda x: x["id"])

print(function([(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]))