class Corn:
    def __init__(self):
        # Mısır ekildiğinde başlangıçta tane (grain) sayısı 0'dır.
        self.grains = 0

    def water(self):
        # Su verildiğinde mısır tanesi 10 adet artar.
        self.grains += 10

    def ripe(self):
        # Tane sayısı 15 veya daha büyükse olgunlaşmıştır (True döner), değilse False döner.
        return self.grains >= 15