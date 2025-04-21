import re
phone_numbers = {"+1":"United States", "+44":"United Kingdom","+505":"Nicaragua","+91":"India","+61":"Australia","+86":"China"}

pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3,4}-\d{3,4}" 
number = input("Number: ").strip()

match =  re.search(pattern, number)
if match:
    country = phone_numbers.get(match.group("country_code"),None)
    if country:
        print("Valid number from", country)
        print("Phone number:", match.group())
    else:
        print("Valid number from unregistered country")
        print("Phone number:", match.group())
else:
    print("Invalid number")
    print("Please ensure the format is: +<country_code> <3-digit>-<3/4-digit>-<3/4-digit>")
