class Email:

    # Initialiser to define the email
    def __init__(self, from_address, subject_line, email_contents):
       
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False


    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True


     # Return a string representation of an email
    def __str__(self):
        return f"{self.from_address}, {self.subject_line}, {self.email_contents}"
    


class Inbox():
    def __init__(self):
            
        self.inbox_list = []


    def add_email(self, from_address, subject_line, email_contents):
        new_email = Email(from_address, subject_line, email_contents)
        self.inbox_list.append(new_email)
        return new_email


    def list_messages_from_sender(self, sender_address):
        # Empty string to capture the results
        results = ""

        # Loop in every email in the email inbox 
        for i, email in enumerate(self.inbox_list):
            #If email is from the sender
            if email.from_address == sender_address:
                # Add the email's index and subject line to the results string
                results += f"{i} {email.subject_line}\n"

        return print(results)


    def get_email(self, sender_address, index):
        for email in self.inbox_list:
            # Check if the email is from the given sender_address
            if email.from_address == sender_address:
                # Check if the email index matches the given index
                 if self.inbox_list.index(email) == index:
                    # Set email has_been_read to True                 
                    email.mark_as_read()
                    return print(email)


    
    def mark_as_spam(self, sender_address, index):
        for spam_mail in self.inbox_list:
            if spam_mail.from_address == sender_address:
                if self.inbox_list.index(spam_mail) == index:
                    # Mark the email as spam
                    spam_mail.mark_as_spam()
                return spam_mail


    def get_unread_emails(self):
        unread_emails = ""

        for email in self.inbox_list:
            if not email.has_been_read:
                # Add the email's subject line to the result string
                unread_emails += f"{email.subject_line}\n"

        return unread_emails


    def get_spam_emails(self):
        spam_emails = ""

        for email in self.inbox_list:
            if email.is_spam:
                spam_emails += f"{email.subject_line}\n"

        return spam_emails


    def delete(self, sender_address, index):
        for email in self.inbox_list:
          if email.from_address == sender_address:
              if self.inbox_list.index(email) == index:
                # Delete  email from the list
                self.inbox_list.remove(email)

usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

user_choice = ""
inbox = Inbox()

while True:
        
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":

        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")
        # Now add the email to the Inbox
        inbox.add_email(sender_address, subject_line, contents)
        
        # Print a success message
        print("Email has been added to inbox.")

    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")
        inbox.list_messages_from_sender(sender_address)
  
        
    elif user_choice == "r":
        
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))
        email = inbox.get_email(sender_address, email_index)

        
        # Step 4: display the email
        
                 
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        
        # Step 2: show all emails from this sender (with indexes)
        inbox.list_messages_from_sender(sender_address)
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be marked as spam\n:"))
        
        
        # Step 4: mark the email as spam

        inbox.mark_as_spam(sender_address,email_index)
        # Step 5: print a success message
        print("Email has been marked as spam")

    elif user_choice == "gu":
        # List all unread emails
        print(inbox.get_unread_emails())
        

    elif user_choice == "gs":
        # List all spam emails
        
        print(inbox.get_spam_emails())


    elif user_choice == "d":
        # Delete an email
        # Step 1&2: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")
        inbox.list_messages_from_sender(sender_address)
        
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email
        inbox.delete(sender_address,email_index)

        # Step 5: print a success message
        print("Email has been deleted")
    
    elif user_choice == "e":
        print("Goodbye")
        break

    else:
        print("Oops - incorrect input")


'''
When reading the emails from the sender and marking emails as spam, your program returns
- <__main__.Email object at 0x0000023B4C8E0CD0>. To get around this, you will have to define
a __str__ function to display the data for the instance in a custom way. In other words, 
inside your class Email, you can add: #This function returns a string presentation the Email class
def __str__(self):
return f'{self.from_address}, {self.subject_line}, {self.email_contents}'
'''