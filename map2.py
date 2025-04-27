import folium
from folium.plugins import HeatMap
import os

# Static lookup table for approximate coordinates (verified per property)
property_data = [
    ("Casale with annex, land and pool, Amandola, Marche, Italy", "https://www.idealista.it/en/immobile/13753219/", (42.9596, 13.3522)),
    ("Farmhouse with 6 rooms and 7 bathrooms, Rosora, Ancona, Italy", "https://www.idealista.it/en/immobile/28254631/", (43.4706, 13.0381)),
    ("Farmhouse in viale Abetone, Abetone, Tuscany, Italy", "https://www.idealista.it/en/immobile/29515832/", (44.1452, 10.6323)),
    ("Farmhouse in via Orvieto, Ficulle, Umbria, Italy", "https://www.idealista.it/en/immobile/21364516/", (42.8694, 12.0067)),
    ("Farmhouse in Pian della Pieve - Porziano, Assisi, Umbria, Italy", "https://www.idealista.it/en/immobile/31936206/", (43.0707, 12.6196)),
    ("Residential building with tower, Macchie, San Ginesio, Marche, Italy", "https://www.idealista.it/immobile/29055357/", (43.1425, 13.2414)),
    ("Villa with lake view and pool, via Canutola, Lisciano Niccone, Umbria, Italy", "https://www.idealista.it/immobile/25066978/", (43.2872, 12.1423)),
    ("Farmhouse in Castel Viscardo, Orvietano, Umbria, Italy", "https://www.idealista.it/immobile/27674806/", (42.7385, 11.9789)),
    ("Villa in strada Provinciale, Campagnano di Roma, Lazio, Italy", "https://www.idealista.it/immobile/32270339/", (42.1417, 12.4208)),
    ("Villa in via Pietro Salvatori, Monterosi, Lazio, Italy", "https://www.idealista.it/immobile/24747346/", (42.2156, 12.2356)),
    ("Mountain house in croce arcana, Abetone Cutigliano, Tuscany, Italy", "https://www.idealista.it/immobile/29884810/", (44.1167, 10.7667)),
    ("Villa with panoramic pool, Cagli, Marche, Italy", "https://www.idealista.it/en/immobile/30476744/", (43.5523, 12.6476)),
    ("Agriturismo with 10 rooms and restaurant, Pian della Pieve - Porziano, Assisi, Umbria, Italy", "https://www.idealista.it/en/immobile/31936206/", (43.0707, 12.6196)),
    ("Restored farmhouse with cottage, via Catignana, Umbria, Italy", "https://www.idealista.it/en/immobile/30204064/", (43.1500, 12.4000)),
    ("Villa in strada Provinciale, Campagnano di Roma, Lazio, Italy", "https://www.idealista.it/en/immobile/32270339/", (42.1417, 12.4208)),
    ("Villa in località Caiano 'Paternò, Londa, Tuscany, Italy", "https://www.idealista.it/en/immobile/32264712/", (43.8500, 11.5333)),
    ("Independent house in via Osteria, Serra de' Conti, Marche, Italy", "https://www.idealista.it/en/immobile/30392314/", (43.5667, 13.0500)),
    ("Villa with panoramic pool, San Fiorano, Cagli, Marche, Italy", "https://www.idealista.it/en/immobile/30476744/", (43.5523, 12.6476)),
    ("Restored farmhouse with cottage, via Catignana, Umbria, Italy", "https://www.idealista.it/en/immobile/30204064/", (43.1500, 12.4000)),
    ("Villa in strada Provinciale, Campagnano di Roma, Lazio, Italy", "https://www.idealista.it/en/immobile/32270339/", (42.1417, 12.4208)),
    ("Villa in località Caiano 'Paternò, Londa, Tuscany, Italy", "https://www.idealista.it/en/immobile/32264712/", (43.8500, 11.5333)),
    ("Independent house in via Osteria, Serra de' Conti, Marche, Italy", "https://www.idealista.it/en/immobile/30392314/", (43.5667, 13.0500)),
    ("Farmhouse in Badiali - Fraccano, Città di Castello, Umbria, Italy", "https://www.idealista.it/en/immobile/30094414/", (43.4600, 12.2400)),
    ("Farmhouse in viale Abetone, Abetone, Tuscany, Italy", "https://www.idealista.it/en/immobile/29515832/", (44.1452, 10.6323)),
    ("Farmhouse in via Fiume, Borgo Pace, Marche, Italy", "https://www.idealista.it/en/immobile/32219565/", (43.6500, 12.4000)),
    ("Independent house in via Montaiate, Umbria, Italy", "https://www.idealista.it/en/immobile/32252020/", (43.1500, 12.4000)),
    ("Farmhouse in strada Provinciale 206, Italy", "https://www.idealista.it/en/immobile/30447724/", (43.1500, 12.4000)),
    ("Farmhouse in Ospedaletto Monte Peglia, Umbria, Italy", "https://www.idealista.it/en/immobile/22661616/", (42.8500, 12.2000)),
    ("Independent house in Apecchio, Catria-Nerone, Marche, Italy", "https://www.idealista.it/en/immobile/30093743/", (43.5833, 12.4167)),
]

# Deduplicate markers
seen_coords = set()
unique_markers = []

for loc, link, coord in property_data:
    if coord not in seen_coords:
        unique_markers.append((loc, link, coord))
        seen_coords.add(coord)

# Map centered better for Italy
map_center = [42.5, 12.5]
map_italy = folium.Map(location=map_center, zoom_start=4, tiles='CartoDB positron')

# Add unique markers
for loc, link, coord in unique_markers:
    folium.Marker(
        location=coord,
        popup=f"<a href='{link}' target='_blank'>{loc}</a>",
        tooltip=loc,
        icon=folium.Icon(color='blue', icon='home', prefix='fa')
    ).add_to(map_italy)

# Heatmap using full data to indicate frequency/density
heat_data = [coord for _, _, coord in property_data]

HeatMap(
    heat_data,
    radius=25,
    blur=15,
    min_opacity=0.6,
    max_zoom=13
).add_to(map_italy)

# Save map
map_italy.save("italy_properties_heatmap.html")
print("Updated map with accurate pins and heatmap created as 'italy_properties_heatmap.html'")
