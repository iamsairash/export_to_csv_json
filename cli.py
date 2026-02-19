from scraper import scrape_products
from database import create_table, save_to_database, fetch_from_database
from exporter import export_to_csv, export_to_json


def display_menu():
    print("\n" + "-" * 40)
    print("       PRODUCT SCRAPER CLI APP")
    print("-" * 40)
    print("  1. Scrape and save to database")
    print("  2. Export to CSV")
    print("  3. Export to JSON")
    print("  4. Exit")
    print("-" * 40)


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("WARNING: Please enter a number between 1 and 5.")
        except ValueError:
            print("WARNING: Invalid input. Please enter a number, not text.")


def handle_choice(choice):
    if choice == 1:
        # scrape + save to database + export both CSV and JSON
        print("\nStarting scrape...")
        products = scrape_products()

        if products:
            create_table()
            save_to_database(products)
        else:
            print("ERROR: Scraping failed. Nothing was saved.")

    elif choice == 2:
        # fetch from database and export to CSV only
        print("\nFetching from database and exporting to CSV...")
        products = fetch_from_database()
        export_to_csv(products)

    elif choice == 3:
        # fetch from database and export to JSON only
        print("\nFetching from database and exporting to JSON...")
        products = fetch_from_database()
        export_to_json(products)

    elif choice == 4:
        print("\nGoodbye! Exiting the app.")
        return False  # signals main loop to stop

    return True  # signals main loop to continue


def run():
    print("\nWelcome to the Product Scraper CLI App!")
    create_table()  # ensure table exists every time app starts

    while True:
        display_menu()
        choice = get_user_choice()
        should_continue = handle_choice(choice)

        if not should_continue:
            break

