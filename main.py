import psutil

from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()
def is_process_malicious(process):
    """
    Check if a process is potentially malicious based on certain criteria.
    You can customize this function according to your requirements.
    """
    try:
        # Check if the process name contains suspicious keywords
        suspicious_keywords = ['hack', 'malware', 'virus', 'keylogger', 'keystroke']
        for keyword in suspicious_keywords:
            if keyword in process.name().lower():
                n.show_toast("Anti-Keylogger", "You have a keylogger running on background", duration=5)
                return True

        # Check if the process is running from a suspicious location
        suspicious_locations = ['/tmp', '/var/tmp']
        if process.exe().lower() in suspicious_locations:
            return True

    except psutil.AccessDenied:
        # Ignore processes that raise an AccessDenied exception
        pass

    return False

def detect_malicious_processes():
    """
    Detect and print information about potentially malicious processes.
    """

    while True:
        all_processes = list(psutil.process_iter(['name', 'exe']))
        print(f"Total processes: {len(all_processes)}")
        malicious_processes = []
        for process in all_processes:
            if is_process_malicious(process):
                malicious_processes.append(process)

        print(f"Potentially malicious processes found: {len(malicious_processes)}")
        for process in malicious_processes:
            print("Potentially malicious process found:")
            print(f"Process Name: {process.name()}")
            print(f"Process Path: {process.exe()}")
            print("")

        user_input = input("Enter 'exit' to stop: ")
        if user_input == 'exit' :
            break

def main():
    detect_malicious_processes()


if __name__ == "__main__":
    main()
