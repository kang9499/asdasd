download_url = "링크"
filename = download_url.rsplit('/', 1)[1]
r = requests.get(download_url, allow_redirects=True)

def download_file():
        if download_url.find('/'):
            open(filename, 'wb').write(r.content)