#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)


print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)


print("-- Create a new State --")
my_state = State()
my_state.name = "Maputo"
my_state.save()
print(my_state)

print("-- Create a new City --")
my_city = City()
my_city.state_id = my_state.id
my_city.name = "Maputo city"
my_city.save()
print(my_city)

print("-- Create a new Amenity --")
my_amenity = Amenity()
my_amenity.name = "Amenity name"
my_amenity.save()
print(my_amenity)


print("-- Create a new Place --")
my_place = Place()
my_place.city_id = my_city.id
my_place.user_id = my_user.id
my_place.name = "Flamingo House"
my_place.description = "Simple house description..."
my_place.number_rooms = 4
my_place.number_bathrooms = 2
my_place.max_guest = 8
my_place.price_by_night = 100
my_place.latitude = 123.123123
my_place.longitude = 12132.123132
my_place.amenity_ids = list(my_amenity.id)
my_place.save()
print(my_place)

print("--Create a new review--")
my_review = Review()
my_review.place_id = my_place.id
my_review.user_id = my_user.id
my_review.text = "SImple text review...."
my_review.save()
print(my_review)
