
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams=100
ounces = grams_to_ounces(grams)
print(f"{grams} grams is equal to {ounces:.2f} ounces")