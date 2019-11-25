from api import create_app
from logging import FileHandler, WARNING

from api.Events.MailEvents import MailEvents
from api.ProxySender.EmailSender import EmailSender

app = create_app('prod.cfg')

file_handler = FileHandler('picus_log.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

me = MailEvents()
ems = EmailSender()
ems.attach(me)

if __name__ == '__main__':
    app.run(debug=True)
