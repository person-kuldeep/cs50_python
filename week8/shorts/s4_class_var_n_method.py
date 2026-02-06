# A class that make instance of food and calculate the heart it gave according to ingrediants

class Food:
    base_heart = 1

    def __init__(self, ingrediants):
        self.ingrediants = ingrediants
        self.hearts = Food.calculate_hearts(ingrediants)

    @classmethod
    def calculate_hearts(cls, ingrediants):
        hearts = cls.base_heart
        for ingrediant in ingrediants:
            if "hearty" in ingrediant.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod 
    def from_nothing(cls, hearts):
        food = cls([])
        food.hearts = hearts + cls.base_heart
        return food
    
def main():
    musroom_strew = Food(["musroom", "hearty mushroom"])
    print(f"it heals {musroom_strew.hearts} hearts")

    musroom = Food.from_nothing(2)
    print(f"it heals {musroom.hearts} hearts")

if __name__ == "__main__":
    main()