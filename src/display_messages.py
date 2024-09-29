import getpass

header = '''
░██████╗░█████╗░░█████╗░██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
░╚═══██╗██║░░██╗██╔══██║██╔══██╗██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██████╔╝╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
A CROSS-PLATFORM SYMMETRIC ENCRYPTION AND DECRYPTION TOOL FOR ALL KINDS OF FILES
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- author- 14mb1v45h


'''


uh_oh = '''

██╗░░░██╗██╗░░██╗  ░█████╗░██╗░░██╗  ██╗
██║░░░██║██║░░██║  ██╔══██╗██║░░██║  ██║
██║░░░██║███████║  ██║░░██║███████║  ██║
██║░░░██║██╔══██║  ██║░░██║██╔══██║  ╚═╝
╚██████╔╝██║░░██║  ╚█████╔╝██║░░██║  ██╗
░╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝  ╚═╝

'''


no_args_provided = '''
█▄░█ █▀█   ▄▀█ █▀█ █▀▀ █░█ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀   █▀█ █▀█ █▀█ █░█ █ █▀▄ █▀▀ █▀▄
█░▀█ █▄█   █▀█ █▀▄ █▄█ █▄█ █░▀░█ ██▄ █░▀█ ░█░ ▄█   █▀▀ █▀▄ █▄█ ▀▄▀ █ █▄▀ ██▄ █▄▀
'''


thanks_msg=f'''
-----------------------------------------------------------------------------------------
███████████████████████████████████████████████████████████████████████████████████████▀█
█─▄─▄─█─█─██▀▄─██▄─▀█▄─▄█▄─█─▄█─▄▄▄▄███▄─▄▄─█─▄▄─█▄─▄▄▀███▄─██─▄█─▄▄▄▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█
███─███─▄─██─▀─███─█▄▀─███─▄▀██▄▄▄▄─████─▄███─██─██─▄─▄████─██─██▄▄▄▄─██─███─█▄▀─██─██▄─█
▀▀▄▄▄▀▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀
-----------------------------------------------------------------------------------------
This has been a great ride {getpass.getuser()} :) Have a good one, buddy !   C i a o   !
-----------------------------------------------------------------------------------------

'''


help_msg=f'''
Hello {getpass.getuser()},

!!! Important Note/Disclaimer Before You Start !!!
This tool can be used for various malicious purposes and that is not at all an intention behind developing this. This is developed completely for Educational Purpose. So, Request you to use this wisely.

Thanks.

----------------------------------------------------------

Usage:
Command: scarecrypt
Parameters (Case Sensitive):
-h | --help     :   This displays the help message of how you can use the tool.
encrypt         :   Encrypts the files stored in a location you'll specify after running the tool.
decrypt         :   Decrypts the files stored in a location you'll specify after running the tool.
testmail        :   Sends a Test Mail from and to the mail id provided in mailceds.py

Syntax:
-> python3 scarecrypt --help     OR     -> python3 scarecrypt --h
-> python3 scarecrypt encrypt
-> python3 scarecrypt decrypt

::::: WARNING :::::
Make sure you have all your mail details stored in the file named "mailcreds.py" stored under SECRETS folder correctly as that's where your encryption key will be mailed and if you fail to put the correct details, you might suffer from massive data loses in the path you specify while running the tool.

To avoid this, Please make use of the testmail feature of the tool to ensure the mail part is working properly using 'python3 scarecrypt testmail'

Use Wisely.

Thanks.
'''


def help_message():
    print(header)
    print(help_msg)