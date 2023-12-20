class stanley:
    def __init__(self, product, volume, color, material, DOMF):
        self.volume = volume
        self.color = color
        self.material = material
        self.product = product
        self.DOMF = DOMF


    def make_and_modle(self):
        print(f"was mad in {self.DOMF}, color is {self.color}")




bottle = stanley("Ice Flow", 30, "Orange", "steel", "A 23")

bottle.make_and_modle()