from model import *
from add_functions import *
import numpy as np

input_str = input("Введите через пробел {Длина чашелистика} {Ширина чашелистика} {Длина лепестка} {Ширина лепестка}:\n").strip()

classes = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

clear_x = clearing_input(input_str)

x_np = np.array(clear_x)[np.newaxis]
print(x_np.shape)
model = Model()
model.prepare_data()
model.networking() 
# print(x_np.transpose)
result = model.prediction(x_np)
print(f"Результат: {classes[result]}")
