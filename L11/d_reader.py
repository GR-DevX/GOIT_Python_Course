import d_classes
import pickle

with open('cars.pkl','rb') as f:
    cars=pickle.load(f)

print(cars)
car1,car2=cars
print()
print(car1)
print(car2)
print(car1.is_old())
print(car2.is_old())