class Rice:
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
        self.grains += 10