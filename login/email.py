from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


class SendEmail():
    def __init__(self):
        pass

    def test_email(self, subject='', from_email='', to=['']):
        try:
            email_template = get_template('email_templates/base.html')
            #template_data = Context() #This is for when we load dict data into the template
            content = email_template.render()
            message = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to)
            message.attach_alternative(content, "text/html")
            send = message.send()
            if send == 0:
                raise Exception(send)
            return send
        except Exception as e:
            raise Exception(e)
