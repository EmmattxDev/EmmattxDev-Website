from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from backend.settings import development, production
from portfolio.models import Project, Experience
# from base.views import *
# from blog.models import Post
from contact.forms import ContactForm

# Create your views here.

def home(request):
    projects = Project.objects.all()
    experience = Experience.objects.all()

    # """
    # FOR BLOG POST
    # posts = Post.objects.all()
    # """
    

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST or None)
        
        # check whether it's valid:
        if form.is_valid():
            #create model instance to be saved to the database...
            form.save()

            # process the data in form.cleaned_data as required
            # ...
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            message_body = render_to_string(
                template_name= 'contact/contact_message.html',
                context={
                    'name': "%s %s" % (first_name, last_name),
                    'email': email,
                    'subject': subject,
                    'message': message,
                }
            )

            if development.DEBUG:
                sender = development.EMAIL_HOST_USER
            else:
                sender = production.EMAIL_HOST_USER
            recipients = ['emmattxdev@gmail.com', 'emmanuelchukwukac1@gmail.com']

            #send email
            for recipient in recipients:

                email_to_send = EmailMessage(
                    subject, 
                    message_body,
                    sender, 
                    [recipient], 
                )

                #raises an exception when the email did not send
                email_to_send.send(fail_silently=False)

            #send html email to the visitor that the message has been receieved
            email_subject = "Thank you %s for contacting us - EmmattxDev" % (first_name)
            email_message = render_to_string(
                template_name= 'contact/contact_reply_message.html',
                context={
                 'name': first_name,
                 'subject': subject,
                }
            )

            for recipient in recipients:

                email_to_send = EmailMessage(
                    email_subject, 
                    email_message,
                    sender, 
                    [recipient], 
                )

                #raises an exception when the email did not send
                email_to_send.send(fail_silently=False)

            #alert user on screen that the message has been receieved
            messages.success(request, "Thank you, your message has been receieved we will send a reply to your inbox as soon as possible...")

            # redirect to a new URL:
            return redirect('/')
        
    else:
        form = ContactForm()
        
    context = {
        'projects': projects,
        'experience': experience,
        # 'posts': posts,
        'form': form
    }

    return render(request, "pages/index.html", context)

def about(request):
    return render(request, "pages/about.html")

def portfolio(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, "pages/portfolio.html", context)



def portfolio_details(request, slug=None):
    project = get_object_or_404(Project, slug=slug)
    context = {
        "project": project
    }

    return render(request, 'pages/portfolio_details.html', context)


def contact(request):
    return render(request, "pages/contact.html")