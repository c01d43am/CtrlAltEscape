import time
import os
import sys

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro():
    """Displays the intro text."""
    intro_text = '''
    ░█████╗░████████╗██████╗░██╗░░░░░░█████╗░██╗░░░░░████████╗███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗
    ██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗██║░░░░░╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ██║░░╚═╝░░░██║░░░██████╔╝██║░░░░░███████║██║░░░░░░░░██║░░░█████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░
    ██║░░██╗░░░██║░░░██╔══██╗██║░░░░░██╔══██║██║░░░░░░░░██║░░░██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░
    ╚█████╔╝░░░██║░░░██║░░██║███████╗██║░░██║███████╗░░░██║░░░███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗
    ░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝
    v0.0.1    c01d43am'''
    print(intro_text)

def loading_animation():
    """Displays a loading animation."""
    animation = ["[=       ]", "[==        ]", "[===       ]", "[====      ]", "[=====     ]", "[======    ]", "[=======   ]", "[========  ]", "[========= ]", "[==========]"]

    print("\nLoading...")
    for i in range(len(animation)):
        sys.stdout.write(f"\r{animation[i]}")
        sys.stdout.flush()
        time.sleep(0.3)

    print("\n\nWelcome to the application!")

def main():
    clear_screen()
    show_intro()
    time.sleep(2)  # Pause for dramatic effect
    loading_animation()

if __name__ == "__main__":
    main()
