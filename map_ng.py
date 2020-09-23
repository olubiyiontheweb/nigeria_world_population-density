import folium

ng_map = folium.Map(location=[9.526974, 8.044771], zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="Nigerian Map")

fg.add_child(folium.Marker(location=[9.5,7.9], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[8.5,6.9], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

for coordinates in [[10.5,9.9],[7.5,6.0]]:
	#fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", circle=folium.Circle(color='green')))
	fg.add_child(folium.CircleMarker(location=coordinates, popup="Hi I am a Marker", color='red', fill='true', fillColor='red'))

fg.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig').read()), 
style_function=lambda x: {'fillColor':'yello' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

ng_map.add_child(fg)

ng_map.save("nigeria.html")


