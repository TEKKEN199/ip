import requests, os

ip = input("IP >>")
url = "http://demo.ip-api.com/json/{}".format(ip)
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"'
}
r = requests.get(url).json()
print("ip $ " + r["query"])
print("country $ " + r["country"])
print("countryCode $ " + r["countryCode"])
print("regionName $ " + r["regionName"])
x = r["lat"]
xx = r["lon"]
xxx = str(x) + " " + str(xx)
print("Coordinates $ " + xxx)
print("timezone $ " + r["timezone"])
print("net $ " + r["isp"])
print("Contact company $ " + r["as"])
