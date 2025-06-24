from configparser import ConfigParser
from tkinter import *
import datetime

root = Tk()

root.title("Assetto Corsa Project")
root.geometry('900x850')

# scroll_bar = Scrollbar(root)
# scroll_bar.pack(side=RIGHT, fill=Y)
# mylist = Listbox(root, yscrollcommand=scroll_bar.set)

# loads the ini file
config = ConfigParser()
config.read(r'C:\Users\artur\OneDrive\Documents\Assetto Corsa\personalbest.ini')
# breakpoint()
# loop through a verison of the sorted ini file for car, track, date, time

# converts the miliseconds to minutes and seconds, and miliseconds


def convertMiliseconds(time_ms):
    total_seconds, miliseconds = divmod(time_ms, 1000)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}:{miliseconds:03d}"


for section in sorted(config.sections()):
    date_of_race = int(config[section]['DATE'])//1000
    raw_lap_time = int(config[section]['TIME'])
    formatted_lap_time = convertMiliseconds(raw_lap_time)

    # converts the unix timestamp to a readable set of numbers YEAR, MONTH, DATE
    date_of_race = datetime.datetime.fromtimestamp(date_of_race, datetime.UTC)

    # allows the text to be printed with editted size, font, and bold and location to be on the left side
    car_track_label = Label(
        root, text=f'\n Car & Track: {section}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    car_track_label.pack(anchor='w', padx=20, pady=2)

    date_time_label = Label(
        root, text=f'\n Date and Time of Race: {date_of_race}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    date_time_label.pack(anchor='w', padx=20, pady=2)

    lap_time_label = Label(
        root, text=f'\n Lap Time: {formatted_lap_time}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    lap_time_label.pack(anchor='w', padx=20, pady=2)

# mylist.pack(side=LEFT, fill=BOTH)
# scroll_bar.config(command=mylist.yview)
root.mainloop()
