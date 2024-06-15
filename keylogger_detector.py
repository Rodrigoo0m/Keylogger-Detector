import psutil
import hashlib
import keyboard

# Function to check for suspicious processes
def check_suspicious_processes():
    suspicious_process_names = ["keylogger", "spyware", "logger"]
    found_suspicious_processes = False

    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() in suspicious_process_names:
            found_suspicious_processes = True
            print(f"Suspicious process found: {process.info['name']} (PID: {process.info['pid']})")

    if not found_suspicious_processes:
        print("No suspicious processes found.")

# Function to calculate the hash of a file
def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to check the integrity of files
def check_file_integrity(file_path, expected_hash):
    current_hash = get_file_hash(file_path)
    if current_hash and current_hash != expected_hash:
        print(f"File integrity compromised: {file_path}")
    elif current_hash:
        print(f"File integrity verified: {file_path}")

# Function to monitor keyboard inputs
def detect_keylogging():
    print("Monitoring keyboard inputs... Press ESC to exit.")

    def on_key_event(e):
        print(f"Key pressed: {e.name}")

    keyboard.hook(on_key_event)
    keyboard.wait('esc')

if __name__ == "__main__":
    # Check for suspicious processes
    print("Checking for suspicious processes...")
    check_suspicious_processes()

    # Check integrity of critical files
    print("\nChecking integrity of critical files...")
    files_to_check = {
        '/path/to/critical/file1': 'expected_hash_here',
        '/path/to/critical/file2': 'expected_hash_here',
    }
    for file_path, expected_hash in files_to_check.items():
        check_file_integrity(file_path, expected_hash)

    # Monitor keyboard inputs
    print("\nStarting keyboard input monitoring...")
    detect_keylogging()
