import sqlite3

baglanti = sqlite3.connect("ariza_takip.db")
im = baglanti.cursor()

# Bilgisayarlar tablosu
im.execute("""
CREATE TABLE IF NOT EXISTS bilgisayarlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT,
    seri_no TEXT,
    marka_model TEXT,
    kullanici TEXT,
    departman TEXT,
    satin_alma_tarihi TEXT
)
""")

# Arızalar tablosu
im.execute("""
CREATE TABLE IF NOT EXISTS arizalar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bilgisayar_id INTEGER,
    tanim TEXT,
    tarih TEXT,
    bildiren TEXT,
    mudahale_eden TEXT,
    yapilan_islem TEXT,
    durum TEXT,
    FOREIGN KEY (bilgisayar_id) REFERENCES bilgisayarlar(id)
)
""")

baglanti.commit()
baglanti.close()

print("Veritabanı oluşturuldu.")
