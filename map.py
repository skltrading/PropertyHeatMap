import folium
import os
from folium.plugins import HeatMap
# Static lookup table for approximate coordinates (no external API calls needed)
# Coordinates are approximate centers of the towns
property_data = [
    ("Monteverdi Marittimo, Pisa, Tuscany, Italy", "https://www.idealista.it/en/immobile/13753219/", (43.178, 10.674)),
    ("Palaia, Pisa, Tuscany, Italy", "https://www.idealista.it/en/immobile/28254631/", (43.602, 10.738)),
    ("Monteriggioni, Siena, Tuscany, Italy", "https://www.idealista.it/en/immobile/27325137/", (43.389, 11.216)),
    ("Castiglione della Pescaia, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/21364516/", (42.761, 10.881)),
    ("Gavorrano, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/29515832/", (42.924, 10.891)),
    ("Montecatini Val di Cecina, Pisa, Tuscany, Italy", "https://www.idealista.it/en/immobile/30094414/", (43.346, 10.738)),
    ("Volterra, Pisa, Tuscany, Italy", "https://www.idealista.it/en/immobile/31936206/", (43.403, 10.860)),
    ("Scansano, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/25066978/", (42.726, 11.324)),
    ("Casole d'Elsa, Siena, Tuscany, Italy", "https://www.idealista.it/en/immobile/27674806/", (43.357, 11.048)),
    ("Trequanda, Siena, Tuscany, Italy", "https://www.idealista.it/immobile/31488648/", (43.178, 11.659)),
    ("Gaiole in Chianti, Siena, Tuscany, Italy", "https://www.idealista.it/en/immobile/32270339/", (43.464, 11.438)),
    ("Campagnatico, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/24747346/", (42.883, 11.193)),
    ("Campiglia Marittima, Livorno, Tuscany, Italy", "https://www.idealista.it/en/immobile/29884810/", (43.060, 10.616)),
    ("Manciano, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/30476744/", (42.585, 11.514)),
    ("Castellina Marittima, Pisa, Tuscany, Italy", "https://www.idealista.it/en/immobile/30204064/", (43.402, 10.594)),
    ("Roccastrada, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/32264712/", (43.010, 11.055)),
    ("Radicondoli, Siena, Tuscany, Italy", "https://www.idealista.it/en/immobile/30392314/", (43.217, 11.017)),
    ("Monterotondo Marittimo, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/30086731/", (43.138, 10.800)),
    ("Montalcino, Siena, Tuscany, Italy", "https://www.idealista.it/en/immobile/22661616/", (43.056, 11.489)),
    ("Sorano, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/30447724/", (42.679, 11.700)),
    ("Chianni, Pisa, Tuscany, Italy", "https://www.idealista.it/en/immobile/32219565/", (43.495, 10.678)),
    ("Castiglione della Pescaia, Grosseto, Tuscany, Italy", "https://www.idealista.it/en/immobile/32252020/", (42.761, 10.881))
]


# Create base map
map_center = [43.4667, 11.0000]
map_italy = folium.Map(location=map_center, zoom_start=8)

# Add markers
for loc, link, coord in property_data:
    folium.Marker(
        location=coord,
        popup=f"<a href='{link}' target='_blank'>{loc}</a>",
        tooltip="Click for Property Link"
    ).add_to(map_italy)

# Create heatmap
heat_data = [coord for _, _, coord in property_data]
HeatMap(heat_data, radius=25, blur=15).add_to(map_italy)

# Save to HTML
output_filename = "italy_properties_heatmap.html"
map_italy.save(output_filename)

print(f"Heatmap with links created and saved as '{output_filename}'!")

