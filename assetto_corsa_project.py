from configparser import ConfigParser
from tkinter import *

root = Tk()

root.title("Assetto Corsa Project")
root.geometry('900x850')

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, yscrollcommand=scroll_bar.set)


# loads the ini file
config = ConfigParser()
config.read(r'C:\Users\artur\OneDrive\Documents\Assetto Corsa\personalbest.ini')

# loop through the ini file for car, track, date, time
for section in config.sections():
    date = (config[section]['DATE'])
    time = (config[section]['TIME'])

# prints everything out
    # print(f'\n Car & Track: {section}')
    # print(f'\n Date and Time of Race: {date}')
    # print(f'\n Lap Time: {time}')
    lbl = Label(root, text=f'\n Car & Track: {section}')
    lbl.pack()
    lbl2 = Label(root, text=f'\n Date and Time of Race: {date}')
    lbl2.pack()
    lbl3 = Label(root, text=f'\n Lap Time: {time}')
    lbl3.pack()

mylist.pack(side=LEFT, fill=BOTH)
scroll_bar.config(command=mylist.yview)
root.mainloop()


# print(config['KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN'])
# print(config['KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN']['DATE'])
# print(config['KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN']['Time'])
