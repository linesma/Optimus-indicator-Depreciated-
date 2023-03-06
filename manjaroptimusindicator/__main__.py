import os
import subprocess

def main():
    post_install_script = os.path.join(os.path.dirname(__file__), "post_install.py")
    subprocess.run(["python3", post_install_script])

if __name__ == "__main__":
    main()
