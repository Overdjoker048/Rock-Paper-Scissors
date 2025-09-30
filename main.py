from random import randint
from sys import stdout

items = {
        "name": "Rock",
        "force": "Scissors"
    },{
        "name": "Paper",
        "force": "Rock"
    },{
        "name": "Scissors",
        "force": "paper"
    }
win = 0
loose = 0
cout = stdout.write

try:
    while True:
        cout(f"""\033c _____            _      _____                        _____       _
| __  | ___  ___ | |_   |  _  | ___  ___  ___  ___   |   __| ___ |_| ___  ___  ___  ___  ___ 
|    -|| . ||  _|| '_|  |   __|| .'|| . || -_||  _|  |__   ||  _|| ||_ -||_ -|| . ||  _||_ -|
|__|__||___||___||_,_|  |__|   |__,||  _||___||_|    |_____||___||_||___||___||___||_|  |___|
                                        |_|
    Victory: {win} Defeat: {loose}

    [*] Rock
    [*] Paper
    [*] Scissors\n
    """)
        choice = input("[Game] What do you want to play:\n>>>").replace(" ", "").title()

        if choice in ("Rock", "Paper", "Scissors"):
            cout(f"\n[You] {choice}\n")
            match randint(0, 2):
                case 0:
                    for item in items:
                        if choice == item["force"]:
                            cout(f"[Computer] {item["name"]}\n[Game] You loose\n")
                            loose += 1
                            break
                case 1:
                    for item in items:
                        if choice == item["name"]:
                            cout(f"[Computer] {item["force"]}\n[Game] You win !\n")
                            win += 1
                            break
                case _:
                    cout(f"[Computer] {choice}\n[Game] You equalized\n")
        else:
            cout("\n[Error] What you entered is not part of the expected answers.\n")

        input("\n[Game] Press Enter to restart...")
except KeyboardInterrupt:
    cout("\n\nGood Bye :)")
