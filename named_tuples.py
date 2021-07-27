import collections as c
City = c.namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', '36.933', (35.432432, 139.532432))
#print(tokyo)
#print(tokyo.population)
#print(tokyo.coordinates)
#print(tokyo[1])

#print(City._fields)
Latlong = c.namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, Latlong(28.614324, 77.20884324))
delhi = City._make(delhi_data)
#print(delhi)
#print(delhi._asdict())
for key,  value in delhi._asdict().items():
    print(f"{key} : {value}")
    