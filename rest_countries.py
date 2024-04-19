# Below is an api endpoint to show you all countries that speak spanish. Dive into the data and answer the following
# questions:

# 1) Display the common name, currency symbol, population and timezone of each country that is NOT landlocked and is in
# the South American continent.

# 2) using the latitude and longitude of the data from the query above, diplay the country information on a world map (using code below)


import requests
import json

url = 'https://restcountries.com/v3.1/lang/spanish'

# make the call to the API

r = requests.get(url)




#create an output file so you can see the json response that was returned by the API call
outfile = open('country.json', 'w')



json.dump(r.json(), outfile, indent = 4)


country_list = r.json()


# Create a list of country names, longitudes, latitudes and population for all countries.
# NOTE: It is important to use these names for the map to work correctly.
names = []
lons = []
lats = []
population = []

# populate this list with the data from the api call using a loop and print out information
# per requirements in 1)



    # Loop through each country in the country list
for country_data in country_list:
    # Check if country_data is a dictionary and contains necessary keys
    if 'South America' in country_data['subregion'] and not country_data['landlocked']:
        common_name = country_data['name']['common']
        currencies = country_data.get('currencies', {})
        currency_symbol = next(iter(currencies.values()), {}).get('symbol', 'Unknown')
        time_zone = country_data['timezones'][0]
        pop = country_data['population']


        print(f'Common Name: {common_name}\nCurrency Symbol: {currency_symbol}\nTime Zone: {time_zone}\nPopulation: {pop}')

        names.append(common_name)
        lons.append(country_data['latlng'][1])
        lats.append(country_data['latlng'][0])
        population.append(pop)







#Plotly World Map (NOTE: NO CODING NEEDED HERE!)


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text':names,
    'marker':{
        'size':[p/3_000_000 for p in population],
        'color':population,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Population'}
    },
}]

my_layout = Layout(title='South American Countries that are not landlocked')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename='south_america.html')
