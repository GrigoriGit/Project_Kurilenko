#Приложение КОММАНДИРОВОЧНЫЕ РАСХОДЫ для автоматизированного финансового контроля на предприятии.
#БД должна содержать таблицу Статьи расходов, имеющую следующую структуру записи:
#№ приказа, Фамилия, Место командировки, Оплата, Аванс, Вид расходов, Сумма расходов.
import sqlite3 as sq
with sq.connect('komandirovochnye_rashody.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS statii_rashodov (
        nomer_prikaza INTEGER PRIMARY KEY,
        familiya TEXT NOT NULL,
        mesto_komandirovki TEXT NOT NULL,
        oplata INTEGER NOT NULL,
        avans INTEGER NOT NULL,
        vid_rashodov TEXT NOT NULL,
        summa_rashodov INTEGER NOT NULL
    )""")
    info_statii_rashodov = [
        (1001, "Попов", "Германия", 20000, 2000, "На проживание", 4000),
        (1002, "Майонезов", "Франция", 25000, 1000, "На пропитание", 2500),
        (1003, "Бобошко", "Эфиопия", 15000, 1700, "На пропитание и проживание", 7000),
        (1004, "Петрушкин", "Кения", 30000, 4000, "На проживание", 8000),
        (1005, "Эльмиров", "Дания", 17000, 2000, "На пропитание", 1300),
        (1006, "Петров", "Казахстан", 40000, 3600, "На проживание и пропитание", 3400),
        (1007, "Горбачев", "Финляндия", 34000, 6700, "На пропитание", 3334),
        (1008, "Пушкин", "Нигерия", 20900, 5500, "На проживание", 2000),
        (1009, "Пивень", "Конго", 40000, 3000, "На проживание", 3000),
        (1010, "Машеров", "Чили", 27000, 1840, "На пропитание", 2000)
    ]
    cur.executemany("INSERT INTO statii_rashodov VALUES (?, ?, ?, ?, ?, ?, ?)", info_statii_rashodov)
    cur.execute("SELECT * FROM statii_rashodov WHERE oplata > 29000 ORDER BY oplata DESC")
    oplata_over_29000 = cur.fetchall()
    print("Записи с оплатой более 29000:")
    print(oplata_over_29000)
    cur.execute("SELECT * FROM statii_rashodov WHERE avans < 2000 ORDER BY avans DESC")
    avans_less_2000 = cur.fetchall()
    print("Записи с авансом менее 2000:")
    print(avans_less_2000)
    cur.execute("SELECT * FROM statii_rashodov WHERE summa_rashodov > 2999 ORDER BY summa_rashodov DESC")
    summa_over_2999 = cur.fetchall()
    print("Записи с суммой расходов более 2999:")
    print(summa_over_2999)
    cur.execute("DELETE FROM statii_rashodov WHERE nomer_prikaza = 1009")
    cur.execute("DELETE FROM statii_rashodov WHERE vid_rashodov = 'На пропитание и проживание'")
    cur.execute("DELETE FROM statii_rashodov WHERE mesto_komandirovki = 'Чили'")
    cur.execute("UPDATE statii_rashodov SET oplata = oplata + 100 WHERE familiya = 'Пушкин'")
    cur.execute("UPDATE statii_rashodov SET summa_rashodov = summa_rashodov + 500 WHERE vid_rashodov = 'На проживание'")
    cur.execute("UPDATE statii_rashodov SET avans = avans + 200 WHERE oplata = 20000")
    cur.execute("SELECT * FROM statii_rashodov")
    all_records = cur.fetchall()
    print("Все записи после удалений и обновлений:")
    print(all_records)
