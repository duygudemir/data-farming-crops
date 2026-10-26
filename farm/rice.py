"""class Rice:
    def __init__(self):
        # Pirinç de başlangıçta 0 tane ile başlar.
        self.grains = 0

    def water(self):
        # Pirinç sulandığında Corn'dan farklı olarak 5 tane grain ekler.
        self.grains += 5

    def ripe(self):
        # Olgunlaşma kuralı Mısır ile aynı: 15 veya daha fazlası True döner.
        return self.grains >= 15

    def transplant(self):
        # Pirince özel bu metot, çağrıldığında 10 grain daha ekler.
        self.grains += 10"""

from farm.crop import Crop

class Rice(Crop):
    def water(self):
        # Pirince özel sulama: Her seferinde 5 grain ekler
        self.grains += 5

    def transplant(self):
        # Pirince özel aktarma: 10 grain ekler
        self.grains += 10