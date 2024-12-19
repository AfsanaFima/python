import os

def shutdown():
    confirmation = input("Are you sure you want to shut down the computer? (yes/no): ")
    if confirmation.lower() == 'yes':
        print("Shutting down the computer...")
        os.system('shutdown /s /t 1')
    else:
        print("Shutdown canceled.")

# Example usage:
shutdown()
