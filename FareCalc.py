def calculate_fare(km,type,hour):
    vechile_types={
    'Economy':10,
    'Premium':18,
    'SUV':25
    }
    type=type.capitalize()
    try:
        rate_vachile=vechile_types[type]
    except KeyError:
        return "Service Not Availabe"  
    if(hour>=17 and hour<=20):
        FareCalc=(km*rate_vachile)*1.5
    else:
        FareCalc=km*rate_vachile
    return FareCalc
hour=int(input("enter the hour of day"))
vechile_type=input("enter a vechile type")
distance=int(input("enter the distance"))
result=calculate_fare(distance,vechile_type,hour)
print("--------Price Receipt----------")
print("Vechile Type: ",vechile_type)
print("Distance: ",distance,"km")
print("Hour:",hour)
print("Total Fare:",result)
