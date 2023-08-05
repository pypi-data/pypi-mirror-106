import gspread
from google.oauth2.service_account import Credentials

class GoogleDriveController:

	@classmethod
	def get_spreadsheet(self, google_secret_file, spreadsheet):
		# use creds to create a client to interact with the Google Drive API
		scope = ['https://spreadsheets.google.com/feeds',
				'https://www.googleapis.com/auth/drive']

		creds = Credentials.from_service_account_file(google_secret_file, scopes=scope)
		client = gspread.authorize(creds)

		# Find a workbook by name and open the first shpwdeet
		# Make sure you use the right name here.
		sheet = client.open(spreadsheet).sheet1

		# Extract and print all of the values
		list_of_hashes = sheet.get_all_records()
		return list_of_hashes

	@classmethod
	def update_cell_spreadsheet(self, google_secret_file, spreadsheet, cell, value):
		# use creds to create a client to interact with the Google Drive API
		scope = ['https://spreadsheets.google.com/feeds',
				'https://www.googleapis.com/auth/drive']

		creds = Credentials.from_service_account_file(google_secret_file, scopes=scope)
		client = gspread.authorize(creds)

		# Find a workbook by name and open the first shpwdeet
		# Make sure you use the right name here.
		sheet = client.open(spreadsheet).sheet1

		sheet.update(cell, value)

		# Extract and print all of the values
		list_of_hashes = sheet.get_all_records()
		return list_of_hashes