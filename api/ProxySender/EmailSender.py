import smtplib

from api.Subject.Subject import Subject


def send_mail(recvrs, text):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls( )
        s.login("mail", "password")
        s.sendmail("sender", recvrs, text)
    except Exception as e:
        print(e)
    finally:
        s.quit( )


class EmailSender(Subject):
    list_observer = []

    def notify(self, crc):
        for o in self.list_observer:
            o.update(crc)

    def attach(self, observer):
        self.list_observer.append(observer)

    def detach(self, observer):
        self.list_observer.remove(observer)

    def send(self, recvrs, crc, text):
        send_mail(recvrs, text)
        self.notify(crc)
