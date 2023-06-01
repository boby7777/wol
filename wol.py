import socket
import re
import os
import json

# 讀取或建立資料檔案
data_file = "wol_data.json"

def read_data():
    data = {}
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            data = json.load(f)
    return data

# 檢查MAC地址格式是否正確
def validate_mac(mac):
    regex = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(regex, mac) is not None

# 寄送Wake-on-LAN封包
def send_wol(mac):
    # MAC地址處理
    mac_clean = mac.replace("-", "").replace(":", "")
    mac_bytes = bytes.fromhex(mac_clean)
    
    # 建立Magic Packet封包
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    
    # 寄送封包
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, ('<broadcast>', 9))

# 輸入和寄送WoL
def send_wol_with_input(data):
    if "default_mac" in data:
        mac = data["default_mac"]
        default = True
    else:
        mac = input("請輸入MAC地址：")
        default = False
    if validate_mac(mac):
        send_wol(mac)
        print("Wake-on-LAN封包已寄送至MAC地址：" + mac)
        if default == False:
            set_default_mac(mac)
    else:
        print("無效的MAC地址格式！")

# 顯示預設MAC地址
def display_default_mac(data):
    if "default_mac" in data:
        print("預設MAC地址：" + data["default_mac"])
    else:
        print("目前沒有預設MAC地址。")

# 設定預設MAC地址
def set_default_mac(mac):
    data = {}
    if validate_mac(mac):
        data["default_mac"] = mac
        with open(data_file, 'w') as f:
            json.dump(data, f)
        print("預設MAC地址已設定為：" + mac)
    else:
        print("無效的MAC地址格式！")

# 主程式選單
def main():
    while True:
        data = read_data()
        print("選擇要執行的操作：")
        print("1. 寄送Wake-on-LAN封包")
        print("2. 顯示預設MAC地址")
        print("3. 設定預設MAC地址")
        print("4. 離開")
        
        choice = input("請輸入選項（1-4）：")
        
        if choice == "1":
            send_wol_with_input(data)
        elif choice == "2":
            display_default_mac(data)
        elif choice == "3":
            mac = input("請輸入預設MAC地址：")
            set_default_mac(mac)
        elif choice == "4":
            break
        else:
            print("無效的選項！請重新輸入。")

# 執行主程式
if __name__ == "__main__":
    main()
