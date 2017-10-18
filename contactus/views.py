from django.shortcuts import (get_object_or_404, render)
from .models import ContactMessage

# Create your views here.
def newmessage(request):
    return render(request, 'contactus/message_form.html', {})
