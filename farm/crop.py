class Crop:
    def __init__(self):
        # Corn ve Rice için ortak olan başlangıç tanesi
        self.grains = 0

    def ripe(self):
        # Corn ve Rice için ortak olan olgunlaşma kuralı (15 ve üzeri)
        return self.grains >= 15