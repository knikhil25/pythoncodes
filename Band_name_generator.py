city_name = input("What is your city name? ")
while city_name == "":
    city_name = input("What is your city name? Please enter something!") 
pets_name = input("what is your pets name? ")
if pets_name == "None":
    user_name = input("What is your name? ")
elif pets_name == "none":
    user_name = input("What is your name? ")
    print("Your band name should be: " + user_name + " from " + city_name + "'s band")
elif pets_name == "" :
    print("Your band should be named: The " + city_name + "kers")
else:
    print("your band name should be : The " + city_name + " " + pets_name + "s")
