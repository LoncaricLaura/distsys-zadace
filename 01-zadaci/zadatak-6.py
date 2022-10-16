"""
6. Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
Vraća se spojena lista ili dictionary.
"""
def function(x,y):
    assert type(x) == type(y)
    assert isinstance(x, (list, dict))
    assert isinstance(y, (list, dict))
    return x + y if isinstance(x, list) else x | y

print(function([1,2,1,2],[3,2]))
print(function({1:2,3:2},{5:2,4:1}))
