import os
import platform
import textwrap
import random
import subprocess

NUM_MACHINES = 40
HOME = os.path.expanduser("~") # Works on windows too
SSH_CLIENT_FOLDER = os.path.join(HOME, ".ssh")
SSH_CONFIG_PATH = os.path.join(HOME, ".ssh", "config")

red = lambda text: f"\033[31m{text}\033[0m"
yellow = lambda text: f"\033[33m{text}\033[0m"
cyan = lambda text: f"\033[36;1m{text}\033[0m"

if not os.path.exists(SSH_CLIENT_FOLDER):
    os.makedirs(SSH_CLIENT_FOLDER)

if platform.system() == "Linux":
    CONNECTION_TEST = lambda machine_host: ["timeout", "1", "ping", "-c", "1", machine_host]
    SSH_COPY_KEY = lambda sso, machine_name: (
            f"cat ~/.ssh/{machine_name}.pub | "
            f'ssh -o StrictHostKeyChecking=no "um-ad\\{sso}@{machine_name}.managed.mst.edu" '
            '"if [ ! -d ~/.ssh ]; then mkdir ~/.ssh; fi;'
            'cat >> ~/.ssh/authorized_keys"'
        )
else: # Windows
    CONNECTION_TEST = lambda machine_host: ["ping", "/n", "1", "/w", "1000", machine_host]
    # Windows doesn't have ssh-copy-id command
    SSH_COPY_KEY = lambda sso, machine_name: (
        f"type %USERPROFILE%\.ssh\{machine_name}.pub |"
        f"ssh -o StrictHostKeyChecking=no um-ad\\{sso}@{machine_name}.managed.mst.edu "
        '"if [ ! -d ~/.ssh ]; then mkdir ~/.ssh; fi;'
        'cat >> ~/.ssh/authorized_keys"'
    )

def name_generator():
    used = set()
    while True:
        machine_id = random.randint(1, NUM_MACHINES)
        if machine_id not in used:
            used.add(machine_id)
            yield f"rc{machine_id:02d}xcs213"
        if len(used) == NUM_MACHINES:
            return

def connection_test(machine_host):
    return subprocess.call(
            CONNECTION_TEST(machine_host),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
    ) == 0

def configure_file(sso, machine_name, file):
    file.write(
        textwrap.dedent(
            f"""
            Host {machine_name}
                Hostname {machine_name}.managed.mst.edu
                User um-ad\\{sso}
                IdentityFile {os.path.join(SSH_CLIENT_FOLDER, machine_name)}
            """
        )
    )

ssh_keygen = lambda machine_name: subprocess.call([
    "ssh-keygen",
    "-f",
    os.path.join(SSH_CLIENT_FOLDER, machine_name),
    "-q",
    "-N",
    "",
])

def main():
    print(
        textwrap.dedent("""
    --------- SSH Client Configurator ---------
    This program will walk you through setting
    up your computer as an SSH Client. Only run
    this script on your personal computer. 
    -------------------------------------------"""
        )
    )
    user_sso = input("User ID: ")

    with open(SSH_CONFIG_PATH, "w") as fp:

        for machine_name in name_generator():
            print("\n=== " + yellow(f"um-ad\\{user_sso}@{machine_name}.managed.mst.edu") + " ===")
            identity_file = os.path.join(SSH_CLIENT_FOLDER, machine_name)
            if os.path.exists(identity_file):
                os.remove(identity_file)
                os.remove(identity_file + ".pub")
            
            flag = False
            while not connection_test(machine_name + ".managed.mst.edu"):
                if input("ERROR: Make sure VPN is connected. Try again (y/n)?: ") == "y":
                    continue
                else:
                    flag = True
                    break
            if flag:
                print(cyan(f"Skipping {machine_name}"))
                continue
            
            if ssh_keygen(machine_name) < 0:
                print("ssh-keygen failed")
                exit(1)

            print(
                textwrap.dedent("""
                    When entering your password, you will not see '*' show up.
                    Type your password as you normally would and press Enter
                """
                )
            )

            try:
                if subprocess.call(SSH_COPY_KEY(user_sso, machine_name), 
                        shell=True,
                        timeout=20,
                        stderr=subprocess.DEVNULL
                    ) == 0:
                    print(cyan(f"Successfully configured {machine_name}"))
                    configure_file(user_sso, machine_name, fp)

            except subprocess.TimeoutExpired:
                print(red("Timeout\n") + cyan(f"Skipping {machine_name}"))
            except KeyboardInterrupt:
                pass

            try:
                if input("Configure another machine (y/n)?: ") == "y":
                    continue
                else:
                    break
            except KeyboardInterrupt:
                exit(0)

if __name__ == "__main__":
    main()    
