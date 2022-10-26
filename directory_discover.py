import requests


def request(url):
    try:
        get_response = requests.get("https://" + url)
        print(get_response)

    except requests.exceptions.ConnectionError:
        pass


target_url = "website name"

# This part will be for file directories.
with open("path to wordlist file", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + '/' + word
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)
