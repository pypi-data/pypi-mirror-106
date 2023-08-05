class SplCloud:
    def __init__(self):
        return None

    def get_token(self):
        import os
        import requests
        import urllib
        import urllib3

        token = False

        url = f"http://{os.getenv('SPL_HOSTNAME')}/api/v1/login"
        passwd = urllib.parse.quote(os.getenv('SPL_PASSWORD'))
        payload = f"username={os.getenv('SPL_USERNAME')}&password={passwd}"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        urllib3.disable_warnings()
        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            token = response.json()['token']

        return token

    def clear_token(self, token):
        import os
        import requests
        import urllib3

        url = f"http://{os.getenv('SPL_HOSTNAME')}/api/v1/logout"

        payload = {}
        headers = {
            'Authorization': f'Bearer {token}'
        }
        urllib3.disable_warnings()
        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            return True

        return False

    def upload_gedi_to_cloud(self, doc):
        import requests
        import os
        from yazaki_packages.logs import Logging

        url = f"http://{os.getenv('SPL_HOSTNAME')}/api/v1/filegedi/store"

        payload = {
            'batch_id': doc['batch_id'],
            'upload_at': doc['upload_date'],
        }


        files = [
            ('file_name', (doc['file_name'], open(
                doc['file_path'], 'rb'), 'application/octet-stream'))
        ]
        headers = {
            'Authorization': f"Bearer {doc['token']}"
        }

        
        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)

        if response.status_code == 201:
            return True

        else:
            print(response.status_code)
            Logging(f"UPLOAD {doc['batch_id']}", f"UPLOAD {doc['file_name']} TO SPLCLOUD", response.status_code)


        return False

    def download_gedi(self, token):
        import requests
        import os

        url = f"http://{os.getenv('SPL_HOSTNAME')}/api/v1/filegedi/index"

        payload = {}
        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = False
        if response.status_code == 200:
            data = response.json()

        return data

    def update_gedi_status(self, token, id, statuscode):
        import requests
        import os

        url = f"http://{os.getenv('SPL_HOSTNAME')}/api/v1/filegedi/{id}/update"

        payload = f'download={statuscode}'
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        status = False
        if response.status_code == 200:
            status = True
        
        return status

    def get_text_file(self, url):
        import requests
        from bs4 import BeautifulSoup

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return BeautifulSoup(response.content, 'lxml')

    def linenotify(self, msg):
        import requests
        import os

        url = "https://notify-api.line.me/api/notify"

        payload = 'message='+msg
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {os.getenv("LINE_NOTIFY_TOKEN")}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def linenotify_error(self, msg):
        import requests
        import os

        url = "https://notify-api.line.me/api/notify"

        payload = 'message='+msg
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {os.getenv("LINE_NOTIFY_ERROR_TOKEN")}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    def check_folder(self, foldername):
        import os
        import pathlib

        if os.path.exists(f"{pathlib.Path().absolute()}/{foldername}") is False:
            os.makedirs(f"{pathlib.Path().absolute()}/{foldername}")

        folder_a = os.listdir(f"{pathlib.Path().absolute()}/{foldername}")
        dir_name = []
        for _i in folder_a:
            if _i != ".gitkeep":
                if len(os.listdir(f"{pathlib.Path().absolute()}/{foldername}/{_i}")) > 0:
                    dir_name.append(_i)

                else:
                    os.rmdir(f"{pathlib.Path().absolute()}/{foldername}/{_i}")

        return dir_name
