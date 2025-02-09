import os
import re

# Define your FiveM vehicle resource folder
FIVEM_VEHICLES_PATH = r""  # Add your car folder path here

# Output file for Lua
OUTPUT_FILE = os.path.join(FIVEM_VEHICLES_PATH, "vehicles.lua")

# Regular expressions to extract data from .meta files
MODEL_PATTERN = re.compile(r'<modelName>(.*?)</modelName>')
BRAND_PATTERN = re.compile(r'<gameName>(.*?)</gameName>')  # Some files use <gameName> for brand
CATEGORY_PATTERN = re.compile(r'<vehicleClass>(.*?)</vehicleClass>')

# Default category mapping based on known vehicle classes
CATEGORY_MAP = {
    "compacts": "compacts",
    "coupes": "coupes",
    "muscle": "muscle",
    "offroad": "offroad",
    "suvs": "suv",
    "sports": "sports",
    "sedans": "sedans",
    "vans": "vans",
    "motorcycles": "motorcycles",
    "super": "super",
}

# Function to extract vehicle data from a meta file
def extract_vehicle_data(file_path):
    vehicles = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

            models = MODEL_PATTERN.findall(content)
            brands = BRAND_PATTERN.findall(content)
            categories = CATEGORY_PATTERN.findall(content)

            for i, model in enumerate(models):
                brand = brands[i] if i < len(brands) else "Unknown"
                raw_category = categories[i] if i < len(categories) else "super"  # Default to super
                category = CATEGORY_MAP.get(raw_category.lower(), "super")  # Map to known category

                vehicles.append({
                    'name': model.capitalize(),
                    'brand': brand.capitalize(),
                    'model': model,
                    'price': 20000,  # Default price (customizable)
                    'category': category,
                    'categoryLabel': category.capitalize(),
                    'hash': f'`{model}`',  # Hash must have backticks
                    'shop': 'pdm',  # Default shop (can be changed)
                })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return vehicles

# Scan all vehicle folders and .meta files
def scan_vehicle_files():
    all_vehicles = []

    for root, _, files in os.walk(FIVEM_VEHICLES_PATH):
        for file in files:
            if file.endswith("vehicles.meta"):  # Only look for vehicles.meta files
                file_path = os.path.join(root, file)
                found_vehicles = extract_vehicle_data(file_path)
                all_vehicles.extend(found_vehicles)

    return all_vehicles

# Generate vehicles.lua with structured vehicle data
def generate_lua_file(vehicles):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as lua_file:
        lua_file.write("-- Auto-generated vehicles.lua\n")
        lua_file.write("Config.Vehicles = {\n")

        for vehicle in vehicles:
            lua_file.write(f"    ['{vehicle['model']}'] = {{\n")
            lua_file.write(f"        ['name'] = '{vehicle['name']}',\n")
            lua_file.write(f"        ['brand'] = '{vehicle['brand']}',\n")
            lua_file.write(f"        ['model'] = '{vehicle['model']}',\n")
            lua_file.write(f"        ['price'] = {vehicle['price']},\n")
            lua_file.write(f"        ['category'] = '{vehicle['category']}',\n")
            lua_file.write(f"        ['categoryLabel'] = '{vehicle['categoryLabel']}',\n")
            lua_file.write(f"        ['hash'] = {vehicle['hash']},\n")  # Backticks included
            lua_file.write(f"        ['shop'] = '{vehicle['shop']}',\n")
            lua_file.write(f"    }},\n")

        lua_file.write("}\n")

    print(f"vehicles.lua has been generated at {OUTPUT_FILE}")

# Run the script
if __name__ == "__main__":
    vehicles = scan_vehicle_files()
    if vehicles:
        generate_lua_file(vehicles)
    else:
        print("No vehicles found.")


