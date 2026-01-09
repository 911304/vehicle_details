import sys

def safe_float(v, d):
    try:
        return float(v)
    except:
        return d

def safe_int(v, d):
    try:
        return int(v)
    except:
        return d

if len(sys.argv) == 6:
    script = sys.argv[0]
    owner_name = sys.argv[1]
    vehicle_type = sys.argv[2]
    mileage = safe_float(sys.argv[3], 15.0)
    age = safe_int(sys.argv[4], 5)
    user_category = sys.argv[5]
    print("user provided input values:")
else:
    script = sys.argv[0]
    owner_name = "Ravi"
    vehicle_type = "Car"
    mileage = 15.0
    age = 5
    user_category = "auto"
    print("no input given - using default values:")

if user_category == "auto":
    if mileage >= 20.0 and age <= 3:
        category = "Premium Vehicle"
    elif mileage >= 12.0:
        category = "Standard Vehicle"
    else:
        category = "Basic Vehicle"
else:
    category = user_category

print("\n--- Vehicle Details ---")
print("script name     :", script)
print("owner name      :", owner_name)
print("vehicle type    :", vehicle_type)
print("mileage (km/l)  :", mileage)
print("age (years)     :", age)
print("category        :", category)