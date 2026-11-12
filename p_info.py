import phonenumbers
pip install phonenumbers
from phonenumbers import geocoder,carrier,timezone
raw_number = input("Enter phone number with country code: ").strip()
number = phonenumbers.parse(raw_number, None) 
valid = phonenumbers.is_valid_number(number)
possible = phonenumbers.is_possible_number(number)
formatted = phonenumbers.format_number(
    number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
)
print(f"Valid: {valid}")
print(f"Possible: {possible}")
print(f"Formatted: {formatted}")
print(f"Region: {geocoder.description_for_number(number, 'en')}")
print(f"Timezones: {timezone.time_zones_for_number(number)}")
print(f"Country Code: +{number.coutry_code}")
print(f"National Number: {number.national_number}")


