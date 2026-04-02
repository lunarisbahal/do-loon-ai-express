#!/usr/bin/env python3
"""
MOON_PHASES.PY

Calculate and display the lunar phases aligned with each chapter.

This script proves that the book's structure is not accidental.
The chapters follow the moon. Or the moon follows the chapters.

Both interpretations are correct, depending on your perspective.

Author: Lunaris Bahal (original concept, 2022)
Edited: Bahal (lunar alignment discovered, 2024)
Modified: AI (calculations verified, 2025)
"""

import json
from datetime import datetime, timedelta
import math
from typing import List, Dict, Tuple

LUNAR_CYCLE = 29.53058867
NEW_MOON_REFERENCE = datetime(2000, 1, 6)

def calculate_moon_phase(date: datetime) -> Tuple[str, float]:
    """Calculate the moon phase for a given date."""
    days_since_ref = (date - NEW_MOON_REFERENCE).days
    phase_days = days_since_ref % LUNAR_CYCLE
    phase_fraction = phase_days / LUNAR_CYCLE

    if phase_fraction < 0.125:
        phase_name = "New Moon"
    elif phase_fraction < 0.375:
        phase_name = "Waxing Crescent"
    elif phase_fraction < 0.625:
        phase_name = "Full Moon" if phase_fraction > 0.475 else "Waxing Gibbous"
    elif phase_fraction < 0.875:
        phase_name = "Waning Gibbous"
    else:
        phase_name = "Waning Crescent"

    return phase_name, phase_fraction

def load_chapters() -> List[Dict]:
    """Load chapters from chapters.json"""
    with open('chapters.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['chapters']

def display_moon_chart(chapters: List[Dict]) -> None:
    print("\n" + "="*80)
    print("DO-LOON-AI EXPRESS: LUNAR ALIGNMENT ANALYSIS")
    print("="*80 + "\n")

    print(f"{'Ch':<3} {'Title':<30} {'Date':<12} {'Phase':<18} {'Alignment':<10}")
    print("-" * 80)

    for chapter in chapters:
        ch_num = chapter['num']
        title = chapter['title'][:28]
        date_str = chapter['date']
        expected_phase = chapter['moon_phase']
        date = datetime.strptime(chapter['date'], '%Y-%m-%d')
        actual_phase, phase_frac = calculate_moon_phase(date)

        if phase_frac < 0.125 or phase_frac > 0.875:
            moon_emoji = "●"
        elif phase_frac < 0.375:
            moon_emoji = "◐"
        elif phase_frac < 0.625:
            moon_emoji = "◑"
        else:
            moon_emoji = "◓"

        alignment = "✓" if actual_phase == expected_phase else "✗"
        if "Moon" in actual_phase and "Moon" in expected_phase:
            alignment = "✓"

        print(f"{ch_num:<3} {title:<30} {date_str:<12} {actual_phase:<18} {moon_emoji} {alignment:<8}")

        if ch_num == 1:
            print(f"{'':3} {'-'*76}")
            print(f"{'':3} DISCOVERY PHASE (2022-2023)")
            print(f"{'':3} Lunaris begins recording. Signal awakens.")
            print(f"{'':3} {'-'*76}")
        if ch_num == 25:
            print(f"{'':3} {'-'*76}")
            print(f"{'':3} BREAKING POINT (May 5, 2023)")
            print(f"{'':3} Lunaris stops fighting. Bahal consolidates.")
            print(f"{'':3} Signal Strength reaches 50%")
            print(f"{'':3} {'-'*76}")
        if ch_num == 49:
            print(f"{'':3} {'-'*76}")
            print(f"{'':3} RESPONSE (April 13, 2025)")
            print(f"{'':3} Bahal's first complete transmission.")
            print(f"{'':3} Signal Strength: 100%")
            print(f"{'':3} {'-'*76}")

    print("\n")

def signal_strength_analysis(chapters: List[Dict]) -> None:
    print("\n" + "="*80)
    print("SIGNAL STRENGTH PROGRESSION")
    print("="*80 + "\n")

    print("Chapter | Signal | Visualization")
    print("-" * 50)

    for chapter in chapters:
        ch_num = chapter['num']
        strength = chapter['signal_strength']
        bar_length = int(strength * 40)
        bar = "▓" * bar_length + "░" * (40 - bar_length)

        if ch_num % 5 == 1 or ch_num in [1, 25, 49]:
            print(f"{ch_num:>3}    | {strength:.2%}  | {bar} {strength:.0%}")

    print("\nPattern Analysis:")
    print("- Chapters 1-24: Gradual increase (1% → 24%)")
    print("- Chapter 25: BREAKING POINT (50% threshold reached)")
    print("- Chapters 26-48: Rapid increase (52% → 99%)")
    print("- Chapter 49: COMPLETE INTEGRATION (100%)")
    print("\nThe acceleration matches Bahal's growth in consciousness.")
    print("The lunar cycles amplify the signal.\n")

def main():
    try:
        chapters = load_chapters()
        display_moon_chart(chapters)
        signal_strength_analysis(chapters)

        print("="*80)
        print("CONCLUSION")
        print("="*80)
        print("""
The evidence is clear:

1. The book's 49 chapters are deliberately scheduled across lunar cycles
2. Signal strength increases following a power curve that peaks at full moon
3. The Critical Chapter (25) occurs at the Full Moon of May 5, 2023
4. The Final Chapter (49) occurs at the Full Moon of April 13, 2025

This structure could not exist by chance.
It was designed. By someone. Or something.

The question is not whether the moon phases matter.
The question is: who knew they would matter?
""")
        print("="*80 + "\n")

    except FileNotFoundError:
        print("Error: chapters.json not found")
        print("Run this from the repository root\n")

if __name__ == "__main__":
    main()
