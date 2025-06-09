import re

# Step 1: Read the input.txt file
with open('input.txt', 'r') as file:
    text = file.read()

# Step 2: Find all email addresses using regex
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

# Step 3: Write the found emails to emails.txt
with open('emails.txt', 'w') as file:
    for email in emails:
        file.write(email + '\n')

print("Done! Emails have been saved to emails.txt")