
# Overview 📺
ScareCrypt is developed and tested on `Python 3.11` and uses `Fernet` as it's Cryptography Library to achieve Symmetric Encryption. The tool encrypts all the data stored in a specific path (which will be asked by the tool at the runtime) using a Secret Key which is generated everytime you run the script.
The Secret Key is not stored locally on the machine for Security Reasons but is sent directly to the mail address configured in `SECRETS/mailcreds.py`.
Taking one step further on the Security part, the mail module uses SSL SMTP to make the connection to the e-mail account. Once the connection is made, you'll be provided both the Encoded and Decoded key on your mail which you can use to decrypt the data. The tool can be used on a local machine as well as on a remote machine as well. 
<br>
Language: `Python` <br>
Libraries Used: `Fernet`, `pathlib`, `smtplib`, `datetime`<br>
Platform: `Linux & Windows`<br>
<br><br>


## 🛠️ Installation Steps (Linux Distros and MacOS) 🖥️

#### 3. Now from `ScareCrypt/src/SECRETS` and edit `mailcreds.py` with your credentials. Example Below:

```Bash
# This file contains all the details about the E-Mail

# SMTP Details
smtp_server = "smtp.gmail.com"
smtp_port_no = 465

# Make sure you have the SMTP-SSL Mode Setup on your mail for your account
sender_email_id = "sendermailid@gmail.com"
sender_email_password = "SenderPassw0rd@123456789"
receiver_email_id = "recievermailid@gmail.com"
```

<br>

#### 4. Just run the Install Script

```Bash
./install.sh
```

<br><br>

###



## 🛠️ Installation Steps (Windows) 💽
> Note: Make sure that GIT Works and you have Python 3 installed on your machine. If not, please download and install git from <a href="https://git-scm.com/download/win">here</a> and Python from <a href="https://www.python.org/downloads/windows/">here</a>. Once downloaded and Installed, Please follow the steps below:

#### 1. Clone the Repository


#### 3. Go inside the Repository and Install all the Dependencies from `requirements.txt`:

```Bash
cd /d ScareCrypt
pip3 install -r requirements.txt
```
> We recommend using `pip3` because we are using `python3` for executing this tool. If you don't have pip3 installed on your machine, Please install it first and for which I find <a href="https://www.activestate.com/resources/quick-reads/how-to-install-and-use-pip3/">this link</a> quite useful.

<br>

#### 2. Go Inside `src/SECRETS` and edit `mailcreds.py` with your credentials. Example Below:

```Bash
# This file contains all the details about the E-Mail

# SMTP Details
smtp_server = "smtp.gmail.com"
smtp_port_no = 465

# Make sure you have the SMTP-SSL Mode Setup on your mail for your account
sender_email_id = "sendermailid@gmail.com"
sender_email_password = "SenderPassw0rd@123456789"
receiver_email_id = "recievermailid@gmail.com"
```

<br>



#### 3.  Run the Python File directly using the command below:

```Bash
python3 scarecrypt.py -h
```
> Above Command will display the help message for the tool.

<br>
<br>


## ❗ How to Use ? 🤓
 There are 2 ways using which you can use this tool.
 1. By Local Installation (Works only on Linux Distros) 😎
 2. By Python Script Directly 🔥 

No Method listed above is good or bad. It's just your preference. So, Please feel free to use any of the methods. Both are the recommended methods.
We do recommend you to use the `testmail` feature befoe using the `encrypt` or `decrypt` feature of the tool though. Doing this, you will make sure that the mailmodule is working correctly and you will recieve the Secret Key to your mail as expected.
 
> Please read the instructions below according to your OS and according to what method you want to use in order to use ScareCrypt:️

<br><br>

<h2 align="center"> 📟 Linux Distros and MacOS 📟 </h2>

### By Local Installation 🔋
<br>

**For help:**
```Bash
$> scarecrypt -h
OR 
$> scarecrypt --help
```
<br><br>

**Test Mail:**
> You can use this command to test if you're able to send the mail properly using the credentials stored in `ScareCrypt/src/SECRETS/mailcreds.py`
```Bash
scarecrypt testmail
```
You should recieve the mail with the Secret Key (Encryption Key) once this command is executed successfully. If not, you will have to welcome the error on your terminal and well, check either the credentials you have entered or the mail settings from your e-mail account.
<br><br>

**To Encrypt the files:**
```Bash
$> scarecrypt encrypt
```
You will be prompted to enter the path under which the files are stored which you want to encrypt. This will encrypt all the files stored under that path including the files of the sub-directories.

<br><br>

**To Decrypt the files:**
```Bash
$> scarecrypt decrypt
```
By this command, you will be prompted to enter the path under which the files are stored which you want to decrypt. This will decrypt all the files stored under that path including the files of the sub-directories.

<br><br>
<br><br>

### By Python Script Directly 🐍 
You need to be inside the Repository for this. Once you are, use `git pull` to have the latest code and then, you can use any of the commands below.
<br>



**For help:**

```Bash

$> python3 scarecrypt.py -h

OR

$> python3 scarecrypt.py --help

```

<br><br>

  

**Test Mail:**

> You can use this command to test if you're able to send the mail properly using the credentials stored in `ScareCrypt/src/SECRETS/mailcreds.py`

```Bash
$> python3 scarecrypt.py testmail
```

You should recieve the mail with the Secret Key (Encryption Key) once this command is executed successfully. If not, you will have to welcome the error on your terminal and well, check either the credentials you have entered or the mail settings from your e-mail account.

<br><br>

  

**To Encrypt the files:**

```Bash

$> python3 scarecrypt.py encrypt

```

You will be prompted to enter the path under which the files are stored which you want to encrypt. This will encrypt all the files stored under that path including the files of the sub-directories.

  

<br><br>

  

**To Decrypt the files:**

```Bash

$> python3 scarecrypt.py decrypt

```

By this command, you will be prompted to enter the path under which the files are stored which you want to decrypt. This will decrypt all the files stored under that path including the files of the sub-directories.

  

<br><br>
<br><br>

<h2  align="center"> ⚙️ Windows Machines ⚙️ </h2>
The tool don't have a functionality where the `scarecrypt` command is available accross terminal. So, a direct method works flawlessly on Windows.

You need to be inside the Repository for this. Once you are, use `git pull` to have the latest code and then, you can use any of the commands below (Remains the same as we ran the file directly in the case of Linux Distros).

<br>

  
  
  

**For help:**

  

```Bash
\ScarreCrypt\>  python3  scarecrypt.py  -h

OR

\ScarreCrypt\> python3  scarecrypt.py  --help
```

  

<br><br>

  

  

**Test Mail:**

  

> You can use this command to test if you're able to send the mail properly using the credentials stored in `ScareCrypt/src/SECRETS/mailcreds.py`

  

```Bash
\ScarreCrypt\> python3  scarecrypt.py  testmail

```

  

You should recieve the mail with the Secret Key (Encryption Key) once this command is executed successfully. If not, you will have to welcome the error on your terminal and well, check either the credentials you have entered or the mail settings from your e-mail account.

  

<br><br>

  

  

**To Encrypt the files:**

  

```Bash
\ScarreCrypt\> python3  scarecrypt.py  encrypt
```

  

You will be prompted to enter the path under which the files are stored which you want to encrypt. This will encrypt all the files stored under that path including the files of the sub-directories.

  

  

<br><br>

  

  

**To Decrypt the files:**

  

```Bash
\ScarreCrypt\> python3  scarecrypt.py  decrypt
```

  

By this command, you will be prompted to enter the path under which the files are stored which you want to decrypt. This will decrypt all the files stored under that path including the files of the sub-directories.

  

  

<br><br>

<br><br>

