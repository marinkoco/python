import base64
from cryptography.fernet import Fernet

# Generate a new secret key
key = Fernet.generate_key()

# Save the secret key to a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Define the path to the file that contains the secret key
key_file_path = "key.key"

# Load the secret key from the file
with open(key_file_path, "rb") as key_file:
    key = key_file.read()

# Define the path to the file that contains the username and password
auth_file_path = "auth.txt"

# Load the username and password from the file
with open(auth_file_path, "r") as auth_file:
    auth_data = auth_file.read().splitlines()

# Convert the username and password to bytes
username_bytes = bytes(auth_data[0], "utf-8")
password_bytes = bytes(auth_data[1], "utf-8")

# Concatenate the username and password bytes
data_bytes = username_bytes + b"\x00" + password_bytes

# Encrypt the data using the secret key
cipher = Fernet(key)
encrypted_data = cipher.encrypt(data_bytes)

# Encode the encrypted data as base64
encoded_data = base64.b64encode(encrypted_data)

# Write the encoded data to a file
with open("auth.bin", "wb") as auth_file:
    auth_file.write(encoded_data)

# Define the path to the file that contains the encoded data
encoded_file_path = "auth.bin"

# Load the encoded data from the file
with open(encoded_file_path, "rb") as encoded_file:
    encoded_data = encoded_file.read()

# Decode the encoded data from base64
decoded_data = base64.b64decode(encoded_data)

# Decrypt the data using the secret key
cipher = Fernet(key)
decrypted_data = cipher.decrypt(decoded_data)

# Split the decrypted data into username and password bytes
username_bytes = decrypted_data[:decrypted_data.index(b"\x00")]
password_bytes = decrypted_data[decrypted_data.index(b"\x00") + 1:]

# Convert the username and password bytes to strings
username = username_bytes.decode("utf-8")
password = password_bytes.decode("utf-8")

# Define the username and password to be authenticated
user_input_username = "john.doe"
user_input_password = "mysecretpassword123"

# Authenticate the user
if user_input_username == username and user_input_password == password:
    print("Success")
else:
    print("Fail")
