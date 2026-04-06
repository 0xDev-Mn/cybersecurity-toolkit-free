from banner import show_banner
from scanner import scan_ports
from colorama import Fore, Style, init

init()

def main():
    show_banner()

    while True:
        print(Fore.CYAN + """
[1] 🔍 Port Scanner
[2] 🚀 Get Full Version
[3] ❌ Exit
""" + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "Choose option: " + Style.RESET_ALL).strip()

        if choice == "1":
            target = input(Fore.YELLOW + "Enter IP / Domain: " + Style.RESET_ALL).strip()

            if not target:
                print(Fore.RED + "❌ Invalid input\n" + Style.RESET_ALL)
                continue

            ports = range(20, 120)
            scan_ports(target, ports)

        elif choice == "2":
            print(Fore.GREEN + """
🚀 Upgrade to Full Version:

✔ Subdomain Finder
✔ Vulnerability Scanner
✔ Saved Reports
✔ Beginner Guide (PDF)

👉 Get it here:
YOUR_ITCH_LINK_HERE
""" + Style.RESET_ALL)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print(Fore.RED + "❌ Invalid choice\n" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
