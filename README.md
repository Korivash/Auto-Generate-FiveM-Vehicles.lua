# Auto-Generate FiveM Vehicles.lua

## Overview
This Python script scans all vehicle-related meta files in a FiveM server and generates a structured `vehicles.lua` file. It extracts **model names, brands, categories, and hashes** to ensure all vehicles are properly configured for your server.

## Features
✔ Automatically detects all `vehicles.meta` files in your FiveM `[vehicles]` resource folder.  
✔ Extracts vehicle **names, brands, categories, model hashes** and assigns default prices.  
✔ Outputs a clean and formatted **`vehicles.lua`** file.  
✔ Customizable **price values**, **categories**, and **shop locations**.  
✔ Supports **MySQL pricing integration** (optional).  

## Requirements
- Python 3.7+
- (Optional) `mysql-connector-python` for MySQL price integration

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Korivash/fivem-vehicle-generator.git
   cd fivem-vehicle-generator
