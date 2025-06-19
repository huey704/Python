from configparser import ConfigParser

# loads the ini file
config = ConfigParser()
config.read(r'C:\Users\artur\OneDrive\Documents\Assetto Corsa\personalbest.ini')

# loop through the ini file for car, track, date, time
for section in config.sections():
    date = (config[section]['DATE'])
    time = (config[section]['TIME'])

    # prints everything out
    print(f'\n Car & Track: {section}')
    print(f'\n Date and Time of Race: {date}')
    print(f'\n Lap Time: {time}')


# print(config['KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN'])
# print(config['KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN']['DATE'])
# print(config['KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN']['Time'])
