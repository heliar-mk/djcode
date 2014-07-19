from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail


def contact(request):
    error = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            error.append('Enter a subject:')
        if not request.POST.get('message', ''):
            error.append('Enter a message:')
        if request.POST.get('email') and '@' not in request.POST['email']:
            error.append('Enter a valid e-mail address:')
        if not error:
            send_mail(
                     request.POST['subject'],
                     request.POST['message'],
                     request.POST.get('email', 'noreply@example.com'),
                     ['siteowner@example.com'],
                     )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {
            'error': error,
            'subject': request.POST.get('subject', ''),
            'email': request.POST.get('email', ''),
            'message': request.POST.get('message', '')}
            )


def thanks(request):
        return render_to_response('thanks.html')
