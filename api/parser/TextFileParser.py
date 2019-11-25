from api.validators.validation import validate_email_address

starting_char = '<'
end_char = '>'


def parse_line(line):
    mail_start_index = line.find(starting_char)
    mail_end_index = line.find(end_char)
    if mail_start_index < 0 or mail_end_index < 0:
        return None, None

    email = line[mail_start_index + 1: mail_end_index]
    if not validate_email_address(email):
        return None, None

    full_name = line[0: mail_start_index-1].strip( )
    return email, full_name


class TextFileParser:
    def __init__(self, file):
        self.file = file
        self.dictionary = {}

    def parse_file(self):
        f = open(self.file, "r")
        for line in f:
            email, full_name = parse_line(line)
            if email and full_name:
                self.dictionary[email] = full_name
        f.close( )
