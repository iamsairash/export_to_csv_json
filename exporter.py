import csv
import json
import os


# Folder where exported files will be saved
EXPORT_FOLDER = "exports"


def create_export_folder():
    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)
        print(f"SUCCESS: Created '{EXPORT_FOLDER}' folder.")


def export_to_csv(products):
    if not products:
        print("WARNING: No products to export.")
        return

    create_export_folder()
    filepath = os.path.join(EXPORT_FOLDER, "products.csv")

    try:
        # get column names from dictionary keys
        fieldnames = products[0].keys()

        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()       # writes the column names as first row
            writer.writerows(products) # writes all products

        print(f"SUCCESS: Data exported to {filepath}")

    except PermissionError:
        print("ERROR: Permission denied. Close the CSV file if it's open.")
    except Exception as e:
        print(f"ERROR: Could not export to CSV: {e}")


def export_to_json(products):
    """
    Takes a list of product dictionaries and exports them to a JSON file.
    """
    if not products:
        print("WARNING: No products to export.")
        return

    create_export_folder()
    filepath = os.path.join(EXPORT_FOLDER, "products.json")

    try:
        with open(filepath, mode="w", encoding="utf-8") as file:
            json.dump(products, file, indent=4)

        print(f"SUCCESS: Data exported to {filepath}")

    except PermissionError:
        print("ERROR: Permission denied. Could not write to file.")
    except Exception as e:
        print(f"ERROR: Could not export to JSON: {e}")
