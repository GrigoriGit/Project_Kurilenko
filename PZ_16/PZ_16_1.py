#Создайте класс "Товар" с атрибутами "название", "цена" и "количество".
#Напишите метод, который выводит информацию о товаре в формате
#"Название: название, Цена: цена, Количество: кол-во".
class Tovar:
    def __init__(self, nazvanie, cena, colichestvo):
        self.nazvanie = nazvanie
        self.cena = cena
        self.colichestvo = colichestvo
    def vivod(self):
        print("Название:", self.nazvanie + ",", "Цена:", str(self.cena) + ",", "Количество:", self.colichestvo)
moloko = Tovar("Молоко", 50, 3)
suhariki = Tovar("Сухарики", 30, 2)
chocolate = Tovar("Шоколад", 70, 1)
moloko.vivod()
suhariki.vivod()
chocolate.vivod()
