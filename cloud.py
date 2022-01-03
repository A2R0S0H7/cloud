import os
import dropboz
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token - access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)


                relative_path = os.path.relpath(loca l_path, file_from)
                dropbox_path - os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

                def main():
                    acces_token = 'sl.A_YRympg0YckaqE1L9weq9ObFcKroovURmWRt0BbP3OxtxlKBwA8zpz3F6-fFNDZ7NGl4Fbm_oBwUF7zSueftAYJH0s9I0IGiYEF0r7TLy2IXrtsFfIynJ_fkO2ZeMm7qhPaMhA'
                    transferData = TransferData(access_token)

                    file_from = str(input("Enter the path to transfer"))
                    file_to = input("enter the full path to upload to dropbox")

                    transferData.upload_file(file_from,file_to)
                    print("file has been moved")

                main()
