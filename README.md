# Automated-Email
Python script for automatic certificate distribution via email. Built to improve efficiency in my role as an administrator for a 5G Networks course, reducing manual effort and time.

The script loads recipient data from a JSON file, attaches the corresponding PDF certificate from a specified directory, and sends out a congratulatory email. By using a simple SMTP setup with SSL security, the script was able to send emails directly from a designated email account.

# Important Note for Gmail Users:

To use this script with a Gmail account as the sender, you need to enable "Less secure app access" in your Google account settings. To do this:

1. Go to https://myaccount.google.com/.
2. In the left-side menu, click on "Security".
3. Scroll down to the "Less secure app access" section and turn it ON.
   
Please remember to turn this setting OFF again when you're done sending emails, to maintain the security of your account. Alternatively, consider implementing OAuth 2.0 authentication in your script for a more secure solution.
