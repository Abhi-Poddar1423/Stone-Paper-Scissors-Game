import random
import time

def play_rps():
    
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    options = ["Stone", "Paper", "Scissors"]

    print(f"\n{MAGENTA}════════════════════════════════{RESET}")
    print(f"{MAGENTA}🧱 📄 ✂️   STONE-PAPER-SCISSORS  {RESET}")
    print(f"{MAGENTA}════════════════════════════════{RESET}")

    
    user_input = input(f"\n{YELLOW}Your Move (Stone, Paper, Scissors): {RESET}").strip().capitalize()

    if user_input not in options:
        print(f"{RED}⚠️  Invalid Move! Choose from: Stone, Paper, or Scissors.{RESET}")
        return

    
    print(f"\n{CYAN}Computer is choosing...{RESET}")
    time.sleep(1)
    
    computer_choice = random.choice(options)
    
    
    print(f"\n{BOLD}--- SHOWDOWN ---{RESET}")
    print(f"🧑🏻‍🦱 YOU:{CYAN}{user_input}{RESET}")
    print(f"🤖 COMPUTER: {YELLOW}{computer_choice}{RESET}")
    print(f"{BOLD}----------------{RESET}")

    
    if user_input == computer_choice:
        print(f"{YELLOW}🤝 RESULT: It's a Tie!{RESET}")
    elif (user_input == "Stone" and computer_choice == "Scissors") or \
         (user_input == "Paper" and computer_choice == "Stone") or \
         (user_input == "Scissors" and computer_choice == "Paper"):
        print(f"{GREEN}🏆 RESULT: YOU WIN!😍🎊 {user_input} beats {computer_choice}. 🎉{RESET}")
    else:
        print(f"{RED}💀 RESULT: COMPUTER WINS!😂 {computer_choice} beats {user_input}.{RESET}")

    print(f"{MAGENTA}════════════════════════════════{RESET}\n")