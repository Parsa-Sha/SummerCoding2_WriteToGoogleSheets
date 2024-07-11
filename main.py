import gspread
from google.oauth2.service_account import Credentials

# Beginning of gspread setup

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1zBEKfujdY0X7vP7KMCbGTfdOztwUQiXv1Gah-ex9k9Q"
workbook = client.open_by_key(sheet_id)

# End of gspread setup

sheet = workbook.worksheet("Sheet1")
sheet.update_title("Hello World")