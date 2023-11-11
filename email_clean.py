"""re to clean emails and os  to create directories and write emails in them"""

import os
import re

# Function to clean email but preserve periods


def clean_email(email: str) -> str:
    """this funxtion will clean the email and preserve only needed characters """

    # Remove unwanted characters except for @, but keep dots, dashes, and underscores
    email = re.sub(r'[^\w@.]', '', email)

    # Remove dots at beginning, end, and around '@'
    email = re.sub(r'^[._]+|[._]+(?=@)|(?<=@)[._]+|[._]+$', '', email)
    # Ensure an underscore is not immediately followed by a dot
    # and vice versa, keep the first character
    email = re.sub(r'(\._)|(_\.)', lambda m: m.group()[0], email)
    return email


def extract_emails(file_path: str) -> list:
    """this function will extract emails from a file and return a list of emails"""
    with open(f'./{file_path}', 'r', encoding='utf-8') as file:
        # This will read the file and return it as a string
        email_data = file.read()
        # This will split the emails on whitespace
        emails = email_data.split()
        return emails


def process_emails(emails: list):
    """this function will process the emails and return a dictionary of emails and etablisement"""
    etablisement_emails = {}
    # This will loop through the emails and split them on the '@' symbol
    for email in emails:
        # This will clean the email
        email = clean_email(email)
        if '@' in email:
            etablisement = email.split('@')[1].split('.')[0]
            # This will check if the etablisement is in the dictionary
            if etablisement not in etablisement_emails:
                etablisement_emails[etablisement] = []
            # This will append the email to the list of emails for the etablisement
            etablisement_emails.get(etablisement).append(email)
    return etablisement_emails


def write_emails_to_file(etablisement_emails: dict):
    """this function will write the emails to a file and create directories for each etablisement"""
    current_directory = os.getcwd()
    for etablisement, emails in etablisement_emails.items():
        directory = f"{current_directory}/emails/{etablisement}"
        os.makedirs(directory, exist_ok=True)
        with open(f'{directory}/emails.txt', 'w', encoding='utf-8') as f:
            for email in emails:
                f.write(email + '\n')


def main():
    """this function will call all the functions"""
    print(os.getcwd())
    emails = extract_emails('emails_file.txt')
    etablisement_emails = process_emails(emails)
    write_emails_to_file(etablisement_emails)


if __name__ == "__main__":
    main()
