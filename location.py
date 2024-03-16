import phonenumbers
from phonenumbers import geocoder
phone_number1= phonenumbers.parse("+18705180231")

print("\n Phone Numbers Location")
print(geocoder.description_for_number(phone_number1,"en"));
