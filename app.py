from configparser import ConfigParser
config = ConfigParser()
config.read('personalbest.ini')
print(config['[KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN]'])
print(config['[KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN]']['DATE'])
print(config['[KS_PORSCHE_911_GT1@KS_NORDSCHLEIFE-TOURISTENFAHRTEN]']['Time'])
