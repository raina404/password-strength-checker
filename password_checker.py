import re
import sys
import getpass
from dataclasses import dataclass, field

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567",
    "letmein", "trustno1", "dragon", "baseball", "iloveyou", "master", "sunshine",
    "ashley", "bailey", "passw0rd", "shadow", "123123", "654321", "superman",
    "qazwsx", "michael", "football", "password1", "password123", "admin", "welcome",
    "login", "hello", "charlie", "donald", "password2", "qwerty123", "1q2w3e",
    "zxcvbnm", "whatever", "qwertyuiop", "iloveyou1", "111111", "1234567890",
}

SEQUENTIAL_PATTERNS = [
    "abcdefghijklmnopqrstuvwxyz",
    "qwertyuiopasdfghjklzxcvbnm",
    "0123456789",
]


@dataclass
class StrengthResult:
    score: int          # 0–100
    label: str          # Very Weak / Weak / Fair / Strong / Very Strong
    feedback: list[str] = field(default_factory=list)


def _has_sequential(password: str, length: int = 3) -> bool:
    lower = password.lower()
    for pattern in SEQUENTIAL_PATTERNS:
        for i in range(len(pattern) - length + 1):
            chunk = pattern[i:i + length]
            if chunk in lower or chunk[::-1] in lower:
                return True
    return False


def _has_repeated(password: str, length: int = 3) -> bool:
    for i in range(len(password) - length + 1):
        if len(set(password[i:i + length])) == 1:
            return True
    return False


def check_strength(password: str) -> StrengthResult:
    feedback: list[str] = []
    score = 0

    # --- length ---
    n = len(password)
    if n == 0:
        return StrengthResult(0, "Very Weak", ["Password cannot be empty."])

    if n < 8:
        feedback.append(f"Too short ({n} chars). Use at least 8.")
    elif n < 12:
        score += 10
    elif n < 16:
        score += 20
    else:
        score += 30

    # --- character variety ---
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^a-zA-Z0-9]", password))

    if has_lower:
        score += 10
    else:
        feedback.append("Add lowercase letters.")

    if has_upper:
        score += 10
    else:
        feedback.append("Add uppercase letters.")

    if has_digit:
        score += 10
    else:
        feedback.append("Add numbers.")

    if has_special:
        score += 20
    else:
        feedback.append("Add special characters (e.g. !@#$%).")

    # variety bonus: all four types present
    if has_lower and has_upper and has_digit and has_special:
        score += 10

    # --- common passwords ---
    if password.lower() in COMMON_PASSWORDS:
        score = min(score, 10)
        feedback.append("This is a commonly used password — choose something unique.")

    # --- sequential / repeated ---
    if _has_sequential(password):
        score -= 10
        feedback.append("Avoid sequential characters (e.g. 'abc', '123', 'qwerty').")

    if _has_repeated(password):
        score -= 10
        feedback.append("Avoid repeated characters (e.g. 'aaa', '111').")

    score = max(0, min(score, 100))

    if score < 20:
        label = "Very Weak"
    elif score < 40:
        label = "Weak"
    elif score < 60:
        label = "Fair"
    elif score < 80:
        label = "Strong"
    else:
        label = "Very Strong"

    return StrengthResult(score, label, feedback)


def _bar(score: int, width: int = 20) -> str:
    filled = round(score / 100 * width)
    empty = width - filled
    colors = {
        "Very Weak":   "\033[91m",   # red
        "Weak":        "\033[33m",   # yellow
        "Fair":        "\033[93m",   # bright yellow
        "Strong":      "\033[32m",   # green
        "Very Strong": "\033[92m",   # bright green
    }
    reset = "\033[0m"
    return ""


def _colored_label(result: StrengthResult) -> str:
    ansi = {
        "Very Weak":   "\033[91m",
        "Weak":        "\033[33m",
        "Fair":        "\033[93m",
        "Strong":      "\033[32m",
        "Very Strong": "\033[92m",
    }
    reset = "\033[0m"
    color = ansi.get(result.label, "")
    bar_width = 20
    filled = round(result.score / 100 * bar_width)
    bar = color + "█" * filled + "\033[90m" + "░" * (bar_width - filled) + reset
    return f"{bar}  {color}{result.label}{reset} ({result.score}/100)"


def display(result: StrengthResult) -> None:
    print()
    print(_colored_label(result))
    if result.feedback:
        print()
        for tip in result.feedback:
            print(f"  • {tip}")
    print()


def main() -> None:
    if len(sys.argv) > 1:
        # password passed as argument (useful for scripting / piping)
        password = sys.argv[1]
        print(f"Checking: {'*' * len(password)}")
    else:
        try:
            password = getpass.getpass("Enter password to check: ")
        except (KeyboardInterrupt, EOFError):
            print()
            sys.exit(0)

    result = check_strength(password)
    display(result)

    # exit code reflects strength: 0 = strong enough (Fair+), 1 = too weak
    sys.exit(0 if result.score >= 40 else 1)


if __name__ == "__main__":
    main()
