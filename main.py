import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

print(' █████ ██████   █████ █████   █████   █████████   █████       █████ ██████████  ')
print('░░███ ░░██████ ░░███ ░░███   ░░███   ███░░░░░███ ░░███       ░░███ ░░███░░░░███ ')
print(' ░███  ░███░███ ░███  ░███    ░███  ░███    ░███  ░███        ░███  ░███   ░░███')
print(' ░███  ░███░░███░███  ░███    ░███  ░███████████  ░███        ░███  ░███    ░███')
print(' ░███  ░███ ░░██████  ░░███   ███   ░███░░░░░███  ░███        ░███  ░███    ░███')
print(' ░███  ░███  ░░█████   ░░░█████░    ░███    ░███  ░███      █ ░███  ░███    ███')
print(' █████ █████  ░░█████    ░░███      █████   █████ ███████████ █████ ██████████  ')
print('░░░░░ ░░░░░    ░░░░░      ░░░      ░░░░░   ░░░░░ ░░░░░░░░░░░ ░░░░░ ░░░░░░░░░░   ')

  
print('Please name the number to add')
if 2<3:
    while True:
        name = input()
        print('Please enter a phone number to locate')
        number = input()
        ch_number = phonenumbers.parse(number, 'CH')
        print(geocoder.description_for_number(ch_number, 'de'))

        
        service_number = phonenumbers.parse(number, 'RO')
        print(carrier.name_for_number(service_number, 'de'))

