batken = float(input('Введите температуру Баткена:'))
osh = float(input('Введите температуру Оша:'))
jalal_abad = float(input('Введите температуру Жалал-Абад:'))
chuy = float(input('Введите температуру Чуя:'))
talas = float(input('Введите температуру Таласа:'))
yssyk_kol = float(input('Введите температуру Ыссык-Куля:'))
naryn = float(input('Введите температуру Нарына:'))
temp = batken + osh + jalal_abad + chuy + talas + yssyk_kol + naryn / 7
print(f'Средний показатель температуры воздуха по КР на сегодня {round(temp, 1)}°C')