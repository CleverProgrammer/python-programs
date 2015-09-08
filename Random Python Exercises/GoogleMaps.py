from googlemaps import GoogleMaps

gmaps = GoogleMaps("AIzaSyCRDgKn8OlRrLCaiSKkrNjNPKCuqnsUa4o")


start = 'Constitution Ave NW & 10th St NW, Washington, DC'

end   = 'Independence and 6th SW, Washington, DC 20024, USA'

dirs  = gmaps.directions(start, end)

time  = dirs['Directions']['Duration']['seconds']

print time 
