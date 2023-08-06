# CLI Mail System 
 This Is a simple Mail System which is used to Read and send mails using gmail api. If You want to try the beta version of this then install it using python python package index(pip) via following command<br>
```
$ pip3 install climailsystem
```
You can use this module as command line tool or you can use it as python module
## CLI Guide
```
$ climail --help
```
This will show You all the valid commands available

```
Usage: climail [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  deleteapicreds
  mdetails
  relogin
  sendmessage
  sendmessage-attach
  udetails
```
arguments of command
```
$ climail sendmessage --help
Usage: climail sendmessage [OPTIONS] EMAIL_ID_OF_SENDER SUBJECT MSSG

Options:
  --help  Show this message and exit.

```  
## Module Guide
```
import sendmail
mssg = sendmail.sendmessage(email_address_of_sender,subject,mssg)
#used for sending email without attachment
mssg_attach  = sendmail.sendmessage(email_address_of_sender,subject,mssg,path_of_file_to_be_shared)
#used for sending email with attachment
user_details = sendmail.userdetails()
#used for checking details of user like email id, displaydetails
user_mssg_details = sendmail.usermessagedetails()
#used for checking details of user messages like total number of messages, threads etc
logout = sendmail.login()
#used for changing the user 
delete_Creds = sendmail.deleteapicreds()
#used for changing api creds
```
For Using this module you need Api credentials of Gmail Api , You can use the credentials present in client.json simply copy the credentials and paste it or you can create your own credentials at developer console. Please note that this is the one time process only i.e you have to enter the credentials only on your 1st use. when you will run this module as command line Interface for 1st time or will import this module in your project for 1 st time then a message will be displayed on Your screen.
```
Enter Creds
```
Then copy your api credentials and paste it on console.
 
