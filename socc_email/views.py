from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User, auth
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
def index(request):
    if request.method == 'POST':
        n = request.POST['user']
        p = request.POST['pass']
        q = request.POST['full']
        s = request.POST['email']
        user = User.objects.create_user(username=n, password=p, first_name=q, email=s)
        subject = 'Welcome to InstaGrive'
        message = f'Hi {user.username}, thank you for registering in our Instagrive.\n ' \
                  f'Thanks for sending us the complaint \n'\
                  f'We will review your complaint as soon as possible and we will make sure that there will be no inconvience this time\n'\
                  f'\n'\
                  f'\n'\
                  f' Our policies are different such that we make sure that we will  \n'\
                  f' The objective of the Policy is to assist the Management and public in general handling of complaints in an efficient, effective and professional manner wherein every possible step is taken to ensure that instances of misconduct do not escape scrutiny and action, while at the same time, the morale of the employees is not adversely affected by complaints of trivial nature.   \n'\
                f' The Vigilance Department deals mainly with matters related to corruption and / or where there is a vigilance angle. Only those complaints which contain allegations of corruption / indicate presence of vigilance angle will be addressed. Complaints must contain factual details, verifiable facts and related matters. They should not be vague or contain sweeping allegations. Complaints which do not meet the above criteria may be filed or dropped. \n'\
                  f'Enter the below provided code \n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("Sent successfully go to login")
    else:
        return render(request, 'index.html')