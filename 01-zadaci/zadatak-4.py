"""
Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a
Error. Vraća novu listu uspoređujući elemente na istim indeksima. Ako
su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji.
(Funkcija mora imati dvije linije)
"""
def function(list1, list2):
    assert len(list1) == len(list2)
    return [x if x == y else -1 for x,y in zip(list1, list2)]

print(function([1,2,3,4,5],[2,2,4,4,5]))