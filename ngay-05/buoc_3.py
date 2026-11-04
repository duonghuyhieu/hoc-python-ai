buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
gio = [n * 1.5 for n in buoi.values()]
print(gio)
diem = {t: buoi[t] * 10 for t in buoi}
print(diem)
