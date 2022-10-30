from tkinter import *
import tkintermapview
import requests
import xml.etree.ElementTree as ET


def get_location():
    response = requests.get(url="https://api.3geonames.org/?randomland=yes")
    response.raise_for_status()
    r = ET.fromstring(response.content)
    latitude = float(r[0][0].text)
    longitude = float(r[0][1].text)

    location = f"{r[0][4].text} \nCoordinates: {round(latitude,4)}; {round(longitude,4)}"

    loc_label.config(text=location)
    map_widget.set_position(latitude,longitude,marker=True)
    map_widget.set_zoom(5)

BG= '#e9ecef'
root = Tk()
root.title('RANDOM LOCATION APP')
root.geometry("600x670")
root.config(padx=5,pady=5,bg=BG)
root.resizable(0,0)

main_label = Label(text="MAP", font=("Arial", 20, "bold"),bg=BG)
main_label.pack(pady=5)

my_label = LabelFrame(root)
my_label.pack()

map_widget = tkintermapview.TkinterMapView(my_label, width=500, height=500, corner_radius=5)
map_widget.pack()

loc_label = Label(text="Las Vegas\n Coordinates: 36.1699; -115.1396", bg=BG, font=("Arial", 11, "bold"))
loc_label.pack(pady=3)

button = Button(text="GET RANDOM LOCATION", font=("Arial", 12, "bold"), command=get_location)
button.pack(pady=10)

# SET COORDINATES
map_widget.set_position(36.1699,-115.1396)
map_widget.set_zoom(10)

root.mainloop()

