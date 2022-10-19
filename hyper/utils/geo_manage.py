import folium
from hyper.dashboard.models import device


def gen_map():
    m = folium.Map(location=[45.5236, -122.6750])
    devices = device.objects.all()

    for x in devices:
        coords = x.coords.split(",")
        folium.Marker([coords[0],coords[1]], popup=f"<i>{x.ip}</i>").add_to(m)

    m.save("/usr/src/app/hyper/templates/dashboard/geo/index.html")