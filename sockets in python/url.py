from urllib.request import urlopen

url = 'https://www.python.org'

resp = urlopen(url)

html_bytes = resp.read()
print("BYTES:---------------------------------------")
# print(html_bytes)

html = html_bytes.decode()
print("HTML:--------------------------------------------")
print(html)
