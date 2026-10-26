"""class Corn:
    def __init__(self):
        # Mısır ekildiğinde başlangıçta tane (grain) sayısı 0'dır.
        self.grains = 0

    def water(self):
        # Su verildiğinde mısır tanesi 10 adet artar.
        self.grains += 10

    def ripe(self):
        # Tane sayısı 15 veya daha büyükse olgunlaşmıştır (True döner), değilse False döner.
        return self.grains >= 15"""

from farm.crop import Crop

# Sınıf tanımında parantez içinde Crop yazarak ondan miras (inheritance) alıyoruz
class Corn(Crop):
    def water(self):
        # Mısıra özel sulama: Her seferinde 10 grain ekler
        self.grains += 10