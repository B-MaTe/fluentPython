DIAL_CODES = [
    (36, 'Hungary'),
    (91, 'India'),
    (1, 'United States'),
    (55, 'Brasil'),
    (7, 'Russia')
]

country_code = {country: code for code, country in DIAL_CODES}
print(country_code, '\n')
codes = {code: country.upper() for country, code in country_code.items()}
print(codes, '\n')