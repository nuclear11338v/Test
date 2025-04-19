import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing '{command}': {e}")
        sys.exit(1)

def main():
    print("=== VPS Setup Script ===")
    print("\nStep 1: Installing libraries from requirements.txt")
    if os.path.exists("requirements.txt"):
        run_command("pip3 install -r requirements.txt")
    else:
        print("Error: requirements.txt not found!")
        sys.exit(1)

    print("\nStep 2: Example usage")
    print("Make sure ARMAN/main.py is ready to run.")
    print("Example: python3 ARMAN/main.py")

    print("\nStep 3: Setting executable permissions")
    run_command("chmod +x *")
    run_command("chmod 777 *")

    print("\nStep 4: Running ARMAN/main.py")
    if os.path.exists("ARMAN/main.py"):
        run_command("python3 ARMAN/main.py")
    else:
        print("Error: ARMAN/main.py not found!")
        sys.exit(1)

if __name__ == "__main__":
    main()
