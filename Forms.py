# contains the forms used in the app

from wtforms import Form, StringField, validators


class PlacSettingsForm(Form):
    ip_addr_regex = '^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
    ip_addr_message = 'Address must match the expected format ###.###.###.###, where each "###" is between 0 and 255'
    computer_name_regex = '^[A-Za-z0-9_-]+$'
    computer_name_message = 'Computer Name must contain only alphanumeric characters or "-" or "_"'

    computer_name = StringField('Computer Name', [
            validators.Length(min=1, max=15),
            validators.Regexp(computer_name_regex, message=computer_name_message)
        ])
    ip_address = StringField('IP Address', [
            validators.Length(min=7, max=15),
            validators.Regexp(ip_addr_regex, message=ip_addr_message)
        ])
    subnet_mask = StringField('Subnet Mask', [
            validators.Length(min=7, max=15),
            validators.Regexp(ip_addr_regex, message=ip_addr_message)
        ])
    gateway = StringField('Gateway', [
            validators.Length(min=7, max=15),
            validators.Regexp(ip_addr_regex, message=ip_addr_message)
        ])
    network = StringField('Network Name', [
            validators.Length(min=1, max=15),
        ])
