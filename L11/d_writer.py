import d_classes
import pickle

car1=d_classes.Car('i330','BMW',2005,3.1,'petrol','silver')
car2=d_classes.Car('S-Klasse','Mercedes',1986,2.8,'petrol','green')

cars=[car1,car2]

with open('cars.pkl','wb') as f:
    pickle.dump(cars,f)