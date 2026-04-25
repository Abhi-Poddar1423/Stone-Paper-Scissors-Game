from rsp_engine import play_rps
def main():
    
    BORDER = "\033[35m"  
    TEXT = "\033[36m"    
    GOLD = "\033[33m"
    RESET = "\033[0m"

    while True:
        
        print(f"\n{BORDER}╔═════════════════════════════════╗{RESET}")
        print(f"{BORDER}║       🛸 GAMING HUB 🛸          ║{RESET}")
        print(f"{BORDER}╚═════════════════════════════════╝{RESET}")
        
        print(f" {TEXT}[1]{RESET} Play Stone-Paper-Scissors🎮")
        print(f" {TEXT}[2]{RESET} Quit Game👉🖐️")
        print(f"{BORDER}───────────────────────────────────{RESET}")

        
        choice = input(f"{GOLD}Enter your choice (1-2) ❯ {RESET}").strip()

        if choice == '1':
            play_rps()
        elif choice == '2':
            
            print(f"\n{BORDER}✨ Transmission ended. See you next time, Player! ✨{RESET}\n")
            break
        else:
            
            print(f"\n\033[31m⚠️  Oops! That choice doesn't exist. Try 1 or 2.\033[0m")

if __name__ == "__main__":
    main()
