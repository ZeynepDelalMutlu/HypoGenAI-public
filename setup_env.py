import os
import subprocess
import sys

VENV_DIR = ".venv"

def create_venv():
    if not os.path.isdir(VENV_DIR):
        print("Creating virtual environment.")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

def install_requirements():
    pip_path = os.path.join(VENV_DIR, "Scripts", "pip.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "pip")
    if not os.path.isfile("requirements.txt"):
        print("No requirements.txt found.")
        return
    print("Installing requirements from requirements.txt...")
    subprocess.run([pip_path, "install", "-r", "requirements.txt"])
    print("Requirements installed.")

def activate_reminder():
    print("\nAll set!")
    if os.name == "nt":
        print(f"To activate your environment:\n    {VENV_DIR}\\Scripts\\activate")
    else:
        print(f"To activate your environment:\n    source {VENV_DIR}/bin/activate")

if __name__ == "__main__":
    create_venv()
    install_requirements()
    activate_reminder()
