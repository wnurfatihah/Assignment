import functions

def is_valid_email(email):
    """Check if the provided email is in a valid format."""
    if "@" in email and email.count("@") == 1 and email.split("@")[1]:
        return True
    return False

def main():
    print("Welcome to the Stock Selection Tool!")

    while True:
        action = input("Do you want to register or login? (register/login): ").strip().lower()
        if action in ["register", "login"]:
            break
        print("Invalid choice. Please type 'register' or 'login'.")

    while True:
        email = input("Enter email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email. Please enter a valid email address.")

    password = input("Enter password: ").strip()

    if action == "register":
        success, msg = functions.register_user(email, password)
        print(msg)
        if not success:
            return
    elif action == "login":
        success, msg = functions.authenticate_user(email, password)
        print(msg)
        if not success:
            return

    while True:
        print("\n1. Fetch Stock Data")
        print("2. View Saved Data")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            ticker = input("Enter stock ticker (e.g., 1155.KL): ").strip()
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()

            closing_prices = functions.get_closing_prices(ticker, start_date, end_date)
            if closing_prices.empty:
                print("No data available for the given ticker and date range.")
                continue

            analysis = functions.analyze_closing_prices(closing_prices)
            print(f"\nAnalysis Results for {ticker}:")
            for key, value in analysis.items():
                print(f"{key}: {value}")

            data_to_save = {"email": email, "ticker": ticker, **analysis}
            functions.save_to_csv(data_to_save, "data.csv")
            print("Data saved successfully!")

        elif choice == "2":
            saved_data = functions.read_from_csv("data.csv")
            if saved_data is not None:
                print("\nSaved Data:")
                print(saved_data)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
