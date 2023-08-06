# Aim: Implement functions that allow user to work with google drive.

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials
from mimetypes import MimeTypes

import os

class GoogleDrive(object):
    """
    Class allows for programmatic:
        - Uploading of files to a Google Drive
        - Listing of all files & folders available to a service account.
        - Sharing of files with a list of email addresses.
        
    This code has been modified from the version found here:
        https://gist.github.com/rajarsheem/1d9790f0e9846fb429d7
    This code has been tested on V3 of the google drive api found here:
        https://developers.google.com/drive/api/v3/about-sdk
    """
    def __init__(self):
        # Recommended: Use the 'create_credentials' function below to overwrite the credentials variables in this __init__ function.
        # This helps avoid having to manually pass the credentials parameter into each of the functions below.
        self.credentials = None
        
    def create_credentials(self, service_account_json_filename):
        """
        Function creates service account credentials used to authenticate Google Drive requests.
        A service account credentials json object is used as a authenticator.
        See links for details:
            https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console
            https://support.google.com/a/answer/7378726?hl=en

        Parameters:
        ----------
            service_account_json_filename - str
                A string with the full path & name to a .json object that authenticates a service account.
                E.g: '/Users/luyanda.dhlamini/Projects/client_secrets.json'

        Returns:
        ----------
            credentials - oauth2client.service_account.ServiceAccountCredentials
                Google Service Account credentials object.
               
        """
        # Check if provided string contains the phrase '.json'
        assert '.json' in service_account_json_filename, 'Ensure that your service account filename is a json file.'

        # create credenntials used to access google services.
        credentials = ServiceAccountCredentials.from_json_keyfile_name(filename=service_account_json_filename)

        return credentials


    def upload_file_to_google_drive(self, path, credentials=None, parent_id=None):
        """
        Upload a file to a google drive folder.

        Parameters:
        ----------
            path - str
                The full/absolute string path to a file.
                E.g: '/Users/luyanda.dhlamini/Projects/Folder/2021_02_07_customer_classification_1.csv'
            credentials - oauth2client.service_account.ServiceAccountCredentials. Default: None
                Google Service Account credentials object.
            parent_id - str, None Default: None.
                The item used to identify which folder to place a file in.
                E.g: '1czCX8xlhkPyxu00000UbEqncVOPX0000'
                The root / home Drive folder is used if parent_id = None

        Returns:
        ----------
            file_id_dict - dict
                A dictionary with the id of the uploaded file.
        """
        if self.credentials is not None:
            credentials = self.credentials

        mime = MimeTypes()
        service = build('drive', 'v3', credentials=credentials)

        file_metadata = {
            'name': os.path.basename(path),
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]

        media = MediaFileUpload(path,
                                mimetype=mime.guess_type(os.path.basename(path))[0],
                                resumable=True)

        file_id_dict = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()

        return file_id_dict

    def list_files_in_google_drive(self, credentials=None):
        """
        List files that are available to a google drive service account.
        NB: The files shown are files that are available TO THE SERVICE ACCOUNT and not necessarily those of the person running this code.

        Parameters:
        ----------
        credentials - oauth2client.service_account.ServiceAccountCredentials. Default: None
            Google Service Account credentials object.
               

        Returns:
        ----------
        item_dict - dict
            A dictionary with a google drive acount's file details.
        """
        if self.credentials is not None:
            credentials = self.credentials

        service = build('drive', 'v3', credentials=credentials)
        results = service.files().list(fields="nextPageToken, files(id, name,mimeType)").execute()
        items = results.get('files', [])
        item_dict = {'name':[],'id':[]}
        if not items:
            print('No files found.')
        else:

            for item in items:
                item_dict['name'].append(item['name'])
                item_dict['id'].append(item['id'])
            print('Total files found:', len(items))
        return item_dict

    def share_google_drive_file(self, file_id, emails, credentials = None, role = 'writer'):
        """
        Share a google drive file with email address accounts.
        See link below for available role options:
            https://developers.google.com/drive/api/v3/ref-roles
            
        Parameters:
        ----------
        file_id - str
            A string unique identifier to a google drive file.
        emails - list
            A list of email addresses to share a file with.
        credentials - oauth2client.service_account.ServiceAccountCredentials. Default: None
            Google Service Account credentials object of type:   
        role - str
            The user permissions type to assign to a user with access to a file. Default: 'writer'.

        Returns:
        ----------
        results - dict
            A dictionary with the results of sharing files with user email addresses. 
        """
        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print(exception)

        if self.credentials is not None:
            credentials = self.credentials

        results = {'User':[],'Role':[]}
        service = build('drive', 'v3', credentials=credentials)
        batch = service.new_batch_http_request(callback=callback)
        for user in emails:
            user_permission = {
                'type': 'user',
                'role': role,
                'emailAddress': user
            }

            batch.add(service.permissions().create(
                fileId=file_id,
                body=user_permission,
                fields='id',
            ))
            batch.execute()
            results['User'].append(user)
            results['Role'].append(role)

        return results
