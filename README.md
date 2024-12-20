# Individual Assignment
## Overview
The Stock Selection Tool is a Python-based application designed to help users examine historical stock closing prices from the Malaysian market. The tool allows users to safely register and log in, retrieve past closing prices information for certain stocks, carry out necessary analyses, and save the outcomes for later use.
## Features
- User registration and login system.
- Fetch and analyze historical stock closing prices.
- Save and retrieve user interactions in a CSV file.
## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- **Python** Version 3.8 or later
- **pip** (Python package Installer)
### Clone the Repository
```
git clone https://github.com/wnurfatihah/Assignment.git
cd Assignment
```
 ### Install Required Libraries
 Run the following command to install dependencies:
 ```Python
 pip install pandas yfinance
 ```
 ### Run the Program
 Execute the `main.py` file:
 ```
python main.py
```
### Usage Instructions
1. *Register or Login*
  - Register with a valid email (must include @) and a password.
  - Log in using registered credentials.
2. *Fetch Stock Data*
  - Enter a valid stock ticker (e.g., 1155.KL for Maybank).
  - Specify the start and end dates for the analysis.
3. *View Saved Data*
  - Select this option to see previously saved analysis results.
4. *Exit Program*
  - End the session at any time.
### File Descriptions
- `main.py`:
  This is the entry point of the program. It handles user authentication, displays the main menu, and integrates functionality from `functions.py`
- `functions.py`:
  This file contains modular functions to handle tasks like user registration, login validation, fetching stock data from YFinance, performing analysis, and saving results to files.
- `data.csv`:
  A CSV file used to store user interactions, including email, selected stock tickers, and analysis results.
- `users.json`:
  A JSON file that securely stores registered user credentials for authentication.
### License
This project is licensed under the MIT License.
### Contact
For issues or suggestions, feel free to reach out or create an issue in this repository.
