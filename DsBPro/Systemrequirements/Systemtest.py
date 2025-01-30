import subprocess
import tkinter

def check_python_installed():
    try:
        # Versucht, die Python-Version zu ermitteln
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Python ist installiert: {result.stdout.strip()}")
        else:
            print("Python ist nicht installiert.")
    except FileNotFoundError:
        print("Python ist nicht installiert.")

if __name__== "__main__":
    check_python_installed()
