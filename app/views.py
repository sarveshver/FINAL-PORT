from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Contact

def sample(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')

        # Save data to the Contact model
        contact = Contact(subject=sub, message=msg, email=email)
        contact.save()

        # Send mail with text and PDF attachment
        subject = 'Your Subject Here'
        message = 'Your text message here.'

        # Render the text message as HTML
        html_message = render_to_string('sam.html', {'message': message})

        # Strip HTML tags to get the plain text content
        plain_message = strip_tags(html_message)

        # Create an EmailMessage object
        email_message = EmailMessage(
            subject,
            plain_message,
            'sarveshver77@gmail.com',  # From email address
            [email],  # To email address
        )


        pdf_file_path = 'static\pdf\sarveshver (2) (1).pdf'
        with open(pdf_file_path, 'rb') as file:
            email_message.attach(
                'sarveshver (2) (1).pdf',  # Attachment name
                file.read(),
                'application/pdf'  # MIME type for PDF files
            )

        # Send the email
        email_message.send()

        # Attach the PDF file (replace 'your_pdf_file.pdf' with the actual file path)
       

        # Send the email
        email_message.send()

        return HttpResponse('send')
    return render(request, 'mail.html')
