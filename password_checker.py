
import string
import getpass


MIN_LENGTH = 12


def check_password_strength(password):

    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        feedback.append(
            f"Use at least {MIN_LENGTH} characters."
        )

    # 2. Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append(
            "Add an uppercase letter (A-Z)."
        )

    # 3. Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append(
            "Add a lowercase letter (a-z)."
        )

    # 4. Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append(
            "Add at least one number (0-9)."
        )

    # 5. Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append(
            "Add a special character (!, @, #, etc.)."
        )

    # 6. Classify password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    # 7. Display security report
    print("\n" + "=" * 40)
    print("       PASSWORD STRENGTH REPORT")
    print("=" * 40)

    print("Password Strength:", strength)
    print(f"Security Score: {score}/5")

    if feedback:
        print("\nSuggestions to improve your password:")

        for suggestion in feedback:
            print("-", suggestion)

    else:
        print("\nExcellent! All basic checks passed.")

    print("=" * 40)

    print("\nNote: This is a basic password checker.")
    print("A STRONG result does not guarantee security.")


# Main Program
def main():

    print("=" * 40)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    print("\nCheck your password security.")
    print("Your password input will be hidden.")

    # Get hidden password input
    password = getpass.getpass(
        "\nEnter your password: "
    )

    # Validate empty input
    if not password:
        print("\nError: Password cannot be empty.")
        return

    # Check password strength
    check_password_strength(password)


# Run the program
if __name__ == "__main__":
    main()
