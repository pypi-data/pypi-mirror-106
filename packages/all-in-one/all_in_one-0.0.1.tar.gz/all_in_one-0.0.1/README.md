# All In One
### ```All In One``` is a package that allows the user to do lot of things regarding audio, video, networks, the web, external programs, mail, etc.

<br><br>

# Installing the package
<ul>
<li><h3>If on Windows, go to your CMD or PowerShell. If on Mac or Linux, go to your terminal.
<li><h3>Then, just type the following and hit Return</h3>

```python
pip install all_in_one
```
<li><h3>And you're all set! Just go to your code editor and import the package.</h3> 

</ul>

<br><br>

## Code example on mailing to a friend : 
<br>

```python
# Importing the package
import all_in_one

# The mail content
message = """
Hey, dude!

I am able to send a mail through Python!

Your friend, 
X
"""

# Defining the Mailer Class
mailer = all_in_one.Mail()

# Setting the Mail Credentials
mailer.set_mail_creds("foomail@foowebsite.com", "foopassword")

# Sending the message
mailer.mail_to("mail.server.com", 495, "yourfriend@foo.com", "yourmail@foo.com", message)

```

## Don't worry! More features are going to be added soon!