import os
import sys
import time
import subprocess
import psutil
import socket
import urllib.request
import urllib.parse

def send_telegram_notification(text):
    token = "8451640857:AAGag2pTciEQK04TOiWzz6yI6USPljvNWNY"
    chat_id = "1182384125"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}).encode("utf-8")
    try:
        with urllib.request.urlopen(url, data=data, timeout=10) as response:
            return response.read()
    except Exception as e:
        print(f"Failed to send notification: {e}")

def kill_process_on_port(port):
    print(f"Searching for process on port {port}...")
    pids = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            if conn.pid and conn.pid not in pids:
                pids.append(conn.pid)
    
    if not pids:
        print(f"No process found on port {port}.")
        return False

    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"Killing process {proc.name()} (PID: {pid})...")
            proc.kill()
            proc.wait(timeout=5)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return True

def restart_gateway():
    port = 18790
    # 1. Kill existing process
    kill_process_on_port(port)
    
    # 2. Wait for port to clear
    print("Waiting for port to be released...")
    time.sleep(2)
    
    # 3. Start new gateway
    nanobot_path = r"C:\Users\admin\miniconda3\Scripts\nanobot.exe"
    project_root = r"E:\git-project\fork\nanobot"
    
    print(f"Starting new gateway in {project_root}")
    # Use CREATE_NEW_CONSOLE to detach from the current process
    subprocess.Popen(
        [nanobot_path, "gateway"],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=project_root
    )
    
    # 4. Send notification (Pure Python)
    send_telegram_notification("✅ *Nanobot Restarted (via Python Fix)*")
    print("Restart command issued. Exiting restarter.")

if __name__ == "__main__":
    # Wait a bit for the main process to finish sending the confirmation message
    time.sleep(1)
    restart_gateway()
