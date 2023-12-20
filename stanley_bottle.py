class stanley:
    def __init__(self, product, volume, color, material, DOM):
        self.volume = volume
        self.color = color
        self.material = material
        self.product = product
        self.DOM = DOM


    def make_and_dom(self):
        print(f"modle is = {self.product} and made in = {self.DOM}")




ice_flow = stanley("Ice Flow", 30, "Orange", "steel", "A 23")
quencher = stanley("Quencher", 40, "blue", "steel", "L 22")
ice_flow.make_and_dom()
quencher.make_and_dom()