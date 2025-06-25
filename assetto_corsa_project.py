from configparser import ConfigParser
from tkinter import *
from tkinter import ttk
import datetime

root = Tk()
root.title("Assetto Corsa Project")
root.geometry('900x850')

# loads the ini file
config = ConfigParser()
config.read(r'C:\Users\artur\OneDrive\Documents\Assetto Corsa\personalbest.ini')

# converts the miliseconds to minutes and seconds, and miliseconds


def convertMiliseconds(time_ms):
    total_seconds, miliseconds = divmod(time_ms, 1000)
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes}:{seconds:02d}:{miliseconds:03d}"


main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a Scrollbar to the Canvas
my_scrollbar = ttk.Scrollbar(
    main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Canvas to use the Scrollbar
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    scrollregion=my_canvas.bbox("all")))

# Enable mousewheel scrolling


def _on_mousewheel(self, event):
    my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")


my_canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Create another frame inside the Canvas
second_frame = Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# loop through a version of the sorted ini file for car, track, date, time
for section in sorted(config.sections()):
    date_of_race = int(config[section]['DATE']) // 1000
    raw_lap_time = int(config[section]['TIME'])
    formatted_lap_time = convertMiliseconds(raw_lap_time)

    if '@' in section:
        split_car_track = section.split('@')
        (split_car_track[1])  # track
        (split_car_track[0])  # car

    # converts the unix timestamp to a readable set of numbers YEAR, MONTH, DATE
    date_of_race = datetime.datetime.fromtimestamp(date_of_race, datetime.UTC)

    # Add all labels to the scrollable frame
    track_label = Label(
        second_frame, text=f'\n Track: {split_car_track[1]}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    track_label.pack(anchor='w', padx=20, pady=2)

    car_label = Label(
        second_frame, text=f'\n Car: {split_car_track[0]}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    car_label.pack(anchor='w', padx=20, pady=2)

    date_time_label = Label(
        second_frame, text=f'\n Date and Time of Race: {date_of_race}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    date_time_label.pack(anchor='w', padx=20, pady=2)

    lap_time_label = Label(
        second_frame, text=f'\n Lap Time: {formatted_lap_time}', anchor='w', justify=LEFT, font=('Arial', 10, 'bold'))
    lap_time_label.pack(anchor='w', padx=20, pady=2)

root.mainloop()
