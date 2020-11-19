import pickle
import base64
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    aid = "ANGjdJ_aENQY_Japg6ghrVxEC_z-SREpdT9HM9JXCBifUdte1xscpyizWaNEHhI32dD_LsN-45pO5sOmRKgYELj6z0mUV-jTv3Cmd8uLngQyh7_LBPNhsbUQv7pNCOj7FhA56rU4D0_Bp27WUa2rD3gUDUnwOhomlrhPQFajOae5WDSLG8IU-r9X9KYYmmzuCKQOZeX1BDqsl4fWBQh-N-OlgpMfMbYnxb8Ef9RK_wGS6oYmIprpA4hvNa7WxFcpz-H-euntnjSgHp5YnRH7ZN8GwKA_PxYtwU2w6dt1KeSI9eFk1HPt3xaEMDi4hvxg0h6s3MpmfCACprBtwrYMGoPO1WEAbLeIMUTzFjr_tuRggGrt6_PJE9LuG-gNxaJdn-MBaviRbFMa8a7yKT0I"

    # attachment = service.users().messages().attachments().get(userId='me', messageId='175bb31880d1ab37',
    #                                                             id=aid).execute()
    # data = attachment['data']
    # with open('a', 'wb') as f:
    #     f.write(base64.urlsafe_b64decode(data))


    q = "before:1600962027 after:1600961487"
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="from:sachin@vnusoftware.com").execute()
    messages = results.get('messages', [])
    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()

            pass

            print(msg['snippet'])

    # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'])

if __name__ == '__main__':
    main()