import converters
from converters import find_max

weight_kg = converters.lbs_to_kg(89)
print(weight_kg)

weight_lbs = converters.kg_to_lbs(89)
print(weight_lbs)

numbers = [10, 20, 1, 2, 30, 45]
print(find_max(numbers))
