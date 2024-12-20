import json
import pandas as pd
import yfinance as yf

def register_user(email, password):
    """Register a new user and save their credentials."""
    users = {}
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        pass

    if email in users:
        return False, "Email is already registered."

    users[email] = password
    with open("users.json", "w") as f:
        json.dump(users, f)

    return True, "User registered successfully!"

def authenticate_user(email, password):
    """Authenticate a user based on their credentials."""
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return False, "No registered users found."

    if email in users and users[email] == password:
        return True, "Login successful!"

    return False, "Invalid email or password."

def get_closing_prices(ticker, start_date, end_date):
    """Fetch historical closing prices for the given stock ticker."""
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data["Close"]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.Series()

def analyze_closing_prices(data):
    """Perform basic analysis on closing prices."""
    if data.empty:
        return {}

    average_price = data.mean()
    percentage_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    highest_price = data.max()
    lowest_price = data.min()

    return {
        "Average Closing Price": round(average_price, 2),
        "Percentage Change": round(percentage_change, 2),
        "Highest Price": round(highest_price, 2),
        "Lowest Price": round(lowest_price, 2),
    }

def save_to_csv(data, filename):
    """Save user interaction data to a CSV file."""
    df = pd.DataFrame([data])
    try:
        df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def read_from_csv(filename):
    """Read and display saved data from a CSV file."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("No data found.")
        return None
