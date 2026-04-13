# Step 1 ==> import libraries
import phonenumbers                #(تحليل الارقام) parse phonenumbers , (التاكد من صحتها)validate them , (الحصول علي المعلومات والموقع)get location and carrier information
from phonenumbers import geocoder  # Tool used to get the location (Country/City) of the phone number 
from phonenumbers import carrier   # gives you the Telecom Company of the number (Vodafone / Orange / Etisalat / WE )

# Step 2 ==> get the number from user
user_number = input("Enter your phone number : ")

# Step 3 ==> build the app
try:
    parsed_number = phonenumbers.parse(user_number , "EG")  # parse the phone number and converts it into a structured object (تحليل الرقم والحصول علي المعلومات)
    
    if phonenumbers.is_valid_number(parsed_number): 
        number_location = geocoder.description_for_number(parsed_number , "en")  # Get the location of the number
        telecom = carrier.name_for_number(parsed_number , "en")           # Get the carrier (Company Name)

        print("✅ Status: Valid number")  
        print("📍 Location:", number_location) # show the location
        print("📡 Carrier:"   , telecom)         # show the Telecom Company
    else:
        print("\n❌ Invalid phone number")
except:
     print("⚠️  Error: Please enter a valid number like 011#######4")


