from chatterbot.adapters.io import IOAdapter
import requests


class MailgunAdapter(IOAdapter):

    def __init__(self, **kwargs):
        super(MailgunAdapter, self).__init__(**kwargs)

        # Use the bot's name for the name of the sender
        self.name = kwargs.get("name")
        self.from_address = kwargs.get("mailgun_from_address")
        self.api_key = kwargs.get("mailgun_api_key")
        self.endpoint = kwargs.get("mailgun_api_endpoint")
        self.recipients = kwargs.get("mailgun_recipients")

    def process_input(self):
        """
        Check if the user has been sent any new messages.
        """
        # TODO

    def process_response(self, statement):
        """
        Send the response statement as an email.
        """
        subject = "Message from %s" % (self.name)

        self.send_message(
            subject,
            statement.text,
            self.from_address,
            self.recipients
        )

        return statement

    def send_message(self, subject, text, from_address, recipients):
        """
        * subject: Subject of the email.
        * text: Text body of the email.
        * from_email: The email address that the message will be sent from.
        * recipients: A list of recipient email addresses.
        """
        return requests.post(
            self.endpoint,
            auth=("api", self.api_key),
            data={
                "from": "%s <%s>" % (self.name, from_address),
                "to": recipients,
                "subject": subject,
                "text": text
            })
