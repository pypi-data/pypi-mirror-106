import requests

def kurac(url, prefix=""):
    r = requests.post("http://www.kur.ac/_generate", data={"url": url, "subdomain": prefix})
    return r.json()["url"]