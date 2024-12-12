from celery import shared_task


from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#email task
@shared_task
def send_email(user_email,user_otp):
    html_content = render_to_string('send_email.html', {'otp':user_otp}) # render with dynamic value
    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

    msg = EmailMultiAlternatives("config", text_content ,to=[user_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()