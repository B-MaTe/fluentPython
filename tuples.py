# EXAMPLES OF UsIN|g TUPLES AS DATA HOLDERS

# Lat. and Long. of Los Angeles Airport
lax_coordinates = (33.9425, -118.432432) 

# Data about Tokyo: name, year, population change(%), area(km2)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) 

# Traveler IDs (Country code, pass num)
traveler_ids = [('USA', '232213123'), ('BRA', '3243434324'), ('HUN', '34323122')] 

# The '%' formatting operator understands tuples and treats each item as a seperate field
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# Here we dont care about the second item, so we use a 'dummy variable'

for country, _ in traveler_ids:
    print(country)


