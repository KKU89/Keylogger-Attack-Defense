import psutil
import time

def detect_keylogger():
    print("Scanning for keylogger processes...")
    
    suspicious_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            proc_name = proc.info['name'].lower()
            cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
            
            if 'keylogger' in proc_name or 'keylogger.py' in cmdline:
                suspicious_processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cmdline': cmdline
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    if suspicious_processes:
        print("\n[ALERT] Suspicious keylogger processes detected!")
        for proc in suspicious_processes:
            print(f"  PID: {proc['pid']}")
            print(f"  Name: {proc['name']}")
            print(f"  Command: {proc['cmdline']}\n")
        return True
    else:
        print("[OK] No keylogger detected.")
        return False

if __name__ == "__main__":
    detect_keylogger()
