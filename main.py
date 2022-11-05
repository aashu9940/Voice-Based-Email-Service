import smtplib                                               #smtp stand for simple mail transfer protocol
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage


listener = sr.Recognizer()
engine = pyttsx3.init()   #we are making speaking engine that would be speaking to us and we can start it using the pyttsx3 module

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,None,10)      #we have to listen whats coming frm source
            info = listener.recognize_google(voice)      #we are using google api to convert our voice to text
            print(info)
            return info.lower()
    except:
        pass
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)     #we are creating smtp server using smtb libraray,smtp server name and 587 is the port number
    server.starttls()
    server.login('guptaashutosh208@gmail.com', '********')
    email = EmailMessage()
    email['From'] = 'guptaashutosh208@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    talk('Hey your email has been sent.')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


email_list = {
    'shachi':'shachigupta.96@gmail.com',
    'nishkarsh': 'nishkarshsharma7699@gmail.com',
    'arun': 'aruncena03@gmail.com',
    'ashutosh': 'iamashu208@gmail.com',
    'abhishek': 'abhishekgupta1011x@gmail.com',
    'gowtham': 'gowthamnani946@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()

    send_email(receiver, subject, message)

get_email_info()
