"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn



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

if __name__ == "__main__":
    day_one()

print("\n\n📝 Day Two: Rice")

# 1. Instantiate a rice crop
pass  # YOUR CODE HERE

# 2. Water the rice crop
pass  # YOUR CODE HERE

# 3. Transplant the rice crop
pass  # YOUR CODE HERE

# 4. Print "The rice crop produced ## grains"
pass  # YOUR CODE HERE

# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
pass  # YOUR CODE HERE
