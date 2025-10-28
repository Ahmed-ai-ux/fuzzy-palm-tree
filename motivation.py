import random
from colorama import Fore, Style, init
import sys

init(autoreset=True)

QUOTES = [
    "Believe you can and you're halfway there. 💪",
    "Start where you are. Use what you have. Do what you can.",
    "Don’t watch the clock; do what it does. Keep going. ⏰",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Stay positive, work hard, make it happen. 🚀",
    "Be the energy you want to attract. ✨",
    "Small steps every day lead to big results. 🧱",
    "Progress, not perfection. 🌱",
    "You’re closer than you think. 🔎",
    "One focused hour beats a scattered day. 🎯",
]

AFFIRMATIONS = [
    "I am confident, capable, and unstoppable.",
    "I grow a little every day. 🌿",
    "I attract success through positivity and effort.",
    "I am grateful for what I have and excited for what’s coming. 🙏",
]

TIPS = [
    "Use the Pomodoro technique: 25 min focus, 5 min break. ⏳",
    "Write your top 3 priorities for today. ✅",
    "Take a 5-minute walk to reset your mind. 🚶",
    "Silence notifications during deep work. 📵",
]

CATEGORIES = {
    "quote": QUOTES,
    "affirmation": AFFIRMATIONS,
    "tip": TIPS,
}

def pick_random(category=None):
    if category and category in CATEGORIES:
        pool = CATEGORIES[category]
    else:
        # Pick a random category, then a random line
        pool = random.choice(list(CATEGORIES.values()))
    return random.choice(pool)

# Optional: allow `python motivation.py quote` or `affirmation` or `tip`
category_arg = sys.argv[1].lower() if len(sys.argv) > 1 else None

print(Fore.CYAN + Style.BRIGHT + "\n🌟 Daily Boost 🌟\n")
print(Fore.YELLOW + pick_random(category_arg))
print()
