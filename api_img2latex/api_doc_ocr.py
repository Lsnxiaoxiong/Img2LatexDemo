import requests

url = "https://server.simpletex.cn/api/doc_ocr"


headers = {
    "token": "npfsnu1EuC62Crru2gm7MNKBaKrmyzT6seKFO8llu19vZmrKTelDJg6d0BDFJUCY"
}

with open("../images/test4.png", "rb") as file:
    files = {
        "file": ("test4.png", file, "image/png")
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        print("Request successful!")
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)

    latex_str = response.json()["res"]["content"].replace("\\\\", "\\")
    print("="*20)
    print(latex_str)


