import os

# Print all environment variables
print(os.environ)

# Print the value of PASSWORD
sender_password = os.environ.get('password')
print(sender_password)