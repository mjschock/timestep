import hashlib
import imaplib
import os


def main(email_user, email_pass, imap_host, parent_folder):
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_host)

    # Login to your Gmail account
    mail.login(email_user, email_pass)

    # List all the available mailbox labels (folders) in Gmail
    status, mailbox_data = mail.list()

    # Mailboxes to skip
    skip_mailboxes = [
        "[Gmail]",
        "[Gmail]/All Mail",
        "[Gmail]/Chats",
        # "[Gmail]/Important",
        "[Gmail]/Sent Mail",
    ]

    # Loop through each mailbox and fetch emails
    for mailbox_info in mailbox_data:
        _, mailbox_name = mailbox_info.decode().split(' "/" ')
        mailbox_name = mailbox_name.strip('"')

        # Skip problematic mailboxes
        if mailbox_name in skip_mailboxes:
            print(f"Skipping mailbox: {mailbox_name}")
            continue

        print(f"Fetching emails from mailbox: {mailbox_name}")

        # Select the current mailbox
        mail.select(mailbox_name)

        # Search for all emails in the mailbox
        status, email_ids = mail.search(None, "ALL")

        # Get a list of email IDs
        email_id_list = email_ids[0].split()

        # Loop through the email IDs and fetch the email content
        for email_id in email_id_list:
            status, msg_data = mail.fetch(email_id, "(RFC822)")

            # Extract the email content
            raw_email = msg_data[0][1]

            # Generate a unique identifier by hashing the raw email content
            email_hash = hashlib.md5(raw_email).hexdigest()

            # Create folders specific to email_user and mailbox_name
            folder_path = os.path.join(parent_folder, email_user, mailbox_name)

            # Ensure the folder structure exists
            os.makedirs(folder_path, exist_ok=True)

            # Check if an email with the same hash already exists at the path
            email_file_path = os.path.join(folder_path, f"{email_hash}.eml")
            if os.path.exists(email_file_path):
                with open(email_file_path, "rb") as existing_email_file:
                    existing_email_content = existing_email_file.read()
                # Compare the content of the existing email and the new email
                if existing_email_content == raw_email:
                    print(f"Skipping duplicate email with hash: {email_hash}")
                    continue

            # Save the email as a .eml file with the generated unique identifier
            with open(email_file_path, "wb") as eml_file:
                eml_file.write(raw_email)

    # Logout and close the connection
    mail.logout()


if __name__ == "__main__":
    # Set your email and password
    email_user = "m@mjschock.com"
    email_pass = "enlz hfwp btvy mosx"

    # Set the IMAP host
    imap_host = "imap.gmail.com"

    # Set a parent folder for organizing email folders
    parent_folder = "docs/Emails"

    main(email_user, email_pass, imap_host, parent_folder)
