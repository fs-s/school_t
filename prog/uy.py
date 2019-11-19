cars = {
  "car1" : {
    "name" : "Nissan Skyline",
    "color": "black",
    "year" : "2009"
  },
  "car2" : {
    "name" : "BMW e36",
    "color": "gray",
    "year" : "1999 "
  },
  "car3" : {
    "name" : "lamborghini ursus",
    "color": "yellow",
    "year" : "2014"
  }
}
for tag, g in cars.items():
    if g['year'] == '2009':
        print(g['name'])