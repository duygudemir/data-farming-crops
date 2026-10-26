"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn
from farm.rice import Rice

def day_one():
    print("📝 Day One: Corn")

    # 1. Corn (Mısır) sınıfından yeni bir mısır nesnesi üretiyoruz
    my_corn = Corn()

    # 2. Mısırımızı suluyoruz (su verince 10 grain ekleniyordu)
    my_corn.water()
    print(f"The corn crop produced {my_corn.grains} grains")

    # 3. Olgunlaşıp olgunlaşmadığını kontrol ediyoruz
    if my_corn.ripe():
        print("The corn crop is ripe")
    else:
        print("The corn crop is not ripe")


def day_two():
    print("\n🌾 Day Two: Rice")

    # 1. Rice (Pirinç) sınıfından yeni bir nesne üretiyoruz
    my_rice = Rice()

    # 2. Pirinci suluyoruz (her sulamada 5 grain ekleniyordu)
    my_rice.water()
    print(f"The rice crop produced {my_rice.grains} grains")

    # 3. Şaşırtma / aktarma (transplant) yapıyoruz (10 grain ekliyordu)
    my_rice.transplant()
    print(f"After transplanting, the rice crop produced {my_rice.grains} grains")

    # 4. Olgunluk kontrolü (15 veya daha fazlası True döner)
    if my_rice.ripe():
        print("The rice crop is ripe")
    else:
        print("The rice crop is not ripe")

if __name__ == "__main__":
    day_one()
    day_two()
