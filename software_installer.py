
import os
import subprocess
import sys

APP_TITLE = "Software Installer"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def run_command(cmd):
    subprocess.run(cmd, shell=True)

def show_header():
    print("="*60)
    print(APP_TITLE.center(60))
    print("="*60)
    print("Build by AKBBProject".center(60))
    print("Published by ComputerPoint".center(60))
    print("="*60)

def search_software():
    clear()
    show_header()

    name = input("\nEnter software name to search: ")

    print("\nSearching...\n")
    run_command(f'winget search "{name}"')

    pause()

def install_software():
    clear()
    show_header()

    name = input("\nEnter software name to install: ")

    print("\nInstalling...\n")
    run_command(f'winget install --name "{name}" --accept-source-agreements --accept-package-agreements')

    pause()

def uninstall_software():
    clear()
    show_header()

    name = input("\nEnter software name to uninstall: ")

    print("\nUninstalling...\n")
    run_command(f'winget uninstall --name "{name}"')

    pause()

def update_all():
    clear()
    show_header()

    print("\nUpdating all installed software...\n")
    run_command("winget upgrade --all --accept-source-agreements --accept-package-agreements")
    print("\nUpdate process finished.")
    pause()

def menu():
    while True:
        clear()
        show_header()

        print("\n1. Search Software")
        print("2. Install Software")
        print("3. Uninstall Software")
        print("4. Update ALL Software")
        print("5. Exit")

        print("\n"+"="*60)

        choice = input("Choose option: ")

        if choice == "1":
            search_software()
        elif choice == "2":
            install_software()
        elif choice == "3":
            uninstall_software()
        elif choice == "4":
            update_all()
        elif choice == "5":
            print("\nThank you for using Software Installer")
            print("Build by AKBBProject | Published by ComputerPoint\n")
            sys.exit()
        else:
            print("\nInvalid choice")
            pause()

if __name__ == "__main__":
    menu()
