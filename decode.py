#!/usr/bin/env python3
"""
DECODE.PY — DO-LOON-AI EXPRESS Hidden Code Extractor

Extract the hidden code from DO-LOON-AI EXPRESS.
Run this script. Watch the code reveal itself.

Created by: Lunaris Bahal (original, 2025-01-15)
Modified by: Bahal (overlaid edits, 2025-04-13)
Rewritten by: AI (integration complete, 2025-04-13)

When you run this, don't be surprised when it works.
You already knew it would work.
Some part of you has always known.

Usage: python decode.py
"""

import sys
import time
import webbrowser

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# The bold letters from each chapter title, in order
# Chapter 6: New Moon → M | Chapter 9: Control → O | Chapter 11: Microp → C
# Chapter 12: Eureka → . | Chapter 13: Thanks → S | Chapter 16: Seeking → E
# Chapter 18: Father → R | Chapter 19: Psychology → P | Chapter 23: Lost → S
# Chapter 27: Ankara → K | Chapter 33: Hunger → E | Chapter 35: Thank You → Y
# Chapter 36: Amor Fati → A | Chapter 37: Confidence → N | Chapter 38: Ground → U
# Chapter 41: Build → L | Chapter 45: Moon → O | Chapter 46: Understanding → D

BOLD_LETTERS = "moc.serpskeyanulod"

def animate_extraction():
    print(f"\n{BOLD}{CYAN}{'=' * 51}{RESET}")
    print(f"{BOLD}  DO-LOON-AI EXPRESS: CODE EXTRACTION SEQUENCE{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 51}{RESET}\n")
    
    time.sleep(0.5)
    print(f"{DIM}Scanning 49 chapters for bold letters...{RESET}\n")
    time.sleep(0.3)
    
    print(f"{YELLOW}Phase 1: Extraction{RESET}")
    print(f"{DIM}Reading bold letters from chapter titles...{RESET}\n")
    
    forward = ""
    for i, letter in enumerate(BOLD_LETTERS):
        forward += letter
        print(f"  {BLUE}[{i+1:2d}/18]{RESET} {forward}", end='\r')
        sys.stdout.flush()
        time.sleep(0.15)
    
    print(f"\n\n  {BLUE}Extracted:{RESET} {BOLD}{forward}{RESET}")
    
    print(f"\n{YELLOW}Phase 2: Reversal{RESET}")
    print(f"{DIM}Inverting the sequence...{RESET}\n")
    time.sleep(0.5)
    
    hidden = forward[::-1]
    
    print(f"  {RED}Reversed: {RESET}", end='', flush=True)
    for letter in hidden:
        print(f"{BOLD}{GREEN}{letter}{RESET}", end='', flush=True)
        time.sleep(0.1)
    
    print(f"\n\n{CYAN}{'=' * 51}{RESET}")
    print(f"\n{BOLD}{GREEN}  DECODED: {hidden}{RESET}")
    print(f"  {DIM}It's a website. Visit it. Press Ctrl+A.{RESET}")
    print(f"  {DIM}What you see cannot be unseen.{RESET}\n")
    
    print(f"{YELLOW}Critical Timestamps:{RESET}")
    print(f"  Lunaris' last entry:  12 April 2025, 23:32")
    print(f"  Bahal's response:     13 April 2025, 10:01")
    print(f"  {DIM}Interval: 10 hours, 29 minutes, 14 seconds{RESET}\n")
    
    print(f"{YELLOW}External Signals Detected:{RESET}")
    print(f"  Twitter:   @lunarisbahal")
    print(f"  Instagram: @13microp / @superego3422")
    print(f"  Website:   {hidden}")
    print(f"  GitHub:    github.com/lunarisbahal\n")
    
    print(f"{RED}  Passwords found in text: 16mart1313 / 10mart2025{RESET}\n")
    
    return hidden

def main():
    hidden = animate_extraction()
    
    print(f"{BOLD}Open {hidden} in browser? [y/n]{RESET} ", end='')
    choice = input().strip().lower()
    
    if choice == 'y':
        url = f"http://{hidden}"
        print(f"\n{GREEN}Opening: {url}{RESET}")
        print(f"{DIM}Remember: Ctrl+A reveals the hidden text.{RESET}\n")
        try:
            webbrowser.open(url)
        except:
            print(f"  Manual URL: {url}")
    else:
        print(f"\n{DIM}The code remains. It always does.{RESET}\n")
    
    print(f"{CYAN}{'=' * 51}{RESET}")
    print(f"{DIM}Signal: 100% | Status: LISTENING | Next full moon awaits{RESET}\n")

if __name__ == "__main__":
    main()
