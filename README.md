# AppReview
Gets the reviews of apps using API and posts it in a Google Sheet<br>
This Python script allows you to scrape app reviews for multiple apps using the AppVector API and store the data in a Google Sheet.<br>
The script takes the list of app IDs as input and outputs the reviews to a Google Sheet.

<h2>Prerequisites</h2>
To use this script, you will need the following:

1. A Google account
2. A Google Cloud Platform (GCP) project
3. A Google Sheets document where you want to store the reviews
4. A service account with access to the GCP project and the Google Sheets document
5. An API key for the AppVector API

<h2>Usage</h2>
To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Install the required packages: google-auth, google-api-python-client, and requests.
3. Create a Google Sheets document and note its ID.
4. Share the Google Sheets document with the service account email address.
5. Create a new API key in AppVector and note the key value.
6. Update the keys.json file with your GCP service account details.
7. Update the SAMPLE_SPREADSHEET_ID variable in the script with the ID of your Google Sheets document.
8. Update the headers variable in the script with your AppVector API key.
9. Update the app_ids variable in the script with the app IDs you want to scrape reviews for.
10. Run the script using the command python app_reviews.py. <br>
The script will loop through each app ID and scrape the reviews for that app. It will then store the reviews in your Google Sheets document.

<h2>Notes</h2>
1. You can change the params variable in the script to modify the API parameters for the AppVector API. <br>
2. The append_data function in the script can be modified to add additional data to your Google Sheets document.
