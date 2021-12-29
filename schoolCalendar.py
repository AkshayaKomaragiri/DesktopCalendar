# Import Required Library
from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tkinter import *
from tkcalendar import Calendar
from datetime import date


def calendarEvents():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='nhsglobal@mpsomaha.org', timeMin=now,
                                              maxResults=100, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
    return events


# Create Object
root = Tk()
root.update_idletasks()
today = date.today()
# Set geometry
root.geometry("400x400")

# Add Calendar


cal = Calendar(root, selectmode='day',
               year=today.year, month=today.month,
               day=today.day)

cal.pack(pady=20)
for event in calendarEvents():
    start = event['start'].get('dateTime', event['start'].get('date'))
    date = cal.datetime.today();
    cal.calevent_create(date, event['summary'], 'reminder')

cal.tag_config('reminder', background='red', foreground='yellow')

eventHeader = Label(root, text="Millard North Events : " + cal.get_date())
cal.pack(fill="both", expand=True)
eventHeader.pack(pady=20)

# Execute Tkinter
root.mainloop()
