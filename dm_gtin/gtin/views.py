from django.shortcuts import render,redirect
from gtin.models import *
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from gtin.models import *
from django.contrib import auth
import datetime

# Create your views here.
class generateGtin(View):
    template_name = 'generate-gtin.html'

    def get(self, request, *args, **kwargs):
        request.session['userId'] = 10
        return render(request, self.template_name)

class GTINProductEntry(View):
    template_name = 'gtin-product-entry.html'

    def get(self, request, *args, **kwargs):
        request.session['userId'] = 10
        return render(request, self.template_name)