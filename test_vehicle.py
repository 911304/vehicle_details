import sys

def safe_float(v, d): 
    try: return float(v)
    except: return d

def safe_int(v, d): 
    try: return int(v)
    except: return d

if len(sys.argv) == 6:
    _, owner, vtype, mileage, age, ucat = sys.argv
    mileage, age = safe_float(mileage, 15.0), safe_int(age, 5)
else:
    owner, vtype, mileage, age, ucat = "Ravi", "Car", 15.0, 5, "auto"

if ucat == "auto":
    if mileage >= 20 and age <= 3: category = "Premium Vehicle"
    elif mileage >= 12: category = "Standard Vehicle"
    else: category = "Basic Vehicle"
else: category = ucat

print(f"\n--- Vehicle Details ---\nOwner: {owner}\nType: {vtype}\nMileage: {mileage}\nAge: {age}\nCategory: {category}")