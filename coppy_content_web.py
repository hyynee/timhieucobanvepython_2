import urllib.request
import os

SAVING_PATH = "saving_file"
def download_url(url):
    try:
        with urllib.request.urlopen(url) as connection:
            return connection.read()
    except:
        return None
print(download_url("https://www.tiki.vn"))

def download_and_save(url,path):
    data = download_url(url)
    if data is None:
        return
    file_name = os.path.basename(url).replace("?", "-").replace("&", "-")
    # print(f"Saving {file_name} to {path}")
    file_path = os.path.join(path, file_name)
    with open(file_path, "wb") as f:
        f.write(data)

download_and_save('https://tiki.vn/dien-thoai-may-tinh-bang/c1789', SAVING_PATH)