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

class GTINList(View):
    template_name = 'gtin-list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class GTINProductEntry(View):
    template_name = 'gtin-product-entry.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class addGTINProductEntry(View):
    template_name = 'gtin-product-entry.html'

    def post(self, request, *args, **kwargs):
        req = request.POST
        print('--------')
        gtin = req.get('gtin')
        BrandOwnerName = req.get('BrandOwnerName')
        DataProviderName = req.get('DataProviderName')
        ManufacturerName = req.get('ManufacturerName')
        ContactTypeCode = req.get('ContactTypeCode')
        Contact = req.get('Contact')
        ContactAddress = req.get('ContactAddress')
        ContactMethodCode = req.get('ContactMethodCode')
        ContactDetails = req.get('ContactDetails')
        BrandName = req.get('BrandName')
        SubBrandName = req.get('SubBrandName')
        ShortProductName = req.get('ShortProductName')
        ProductMarketingMessage = req.get('ProductMarketingMessage')
        SearchKeyWordsforProduct = req.get('SearchKeyWordsforProduct')
        ProductTypeDescription = req.get('ProductTypeDescription')
        Length = req.get('Length')
        LengthUnit = req.get('LengthUnit')
        Height = req.get('Height')
        HeightUnit = req.get('HeightUnit')
        Width = req.get('Width')
        WidthUnit = req.get('WidthUnit')
        GrossWeight = req.get('GrossWeight')
        GrossWeightUnit = req.get('GrossWeightUnit')
        MarketAvailabilityDate = req.get('MarketAvailabilityDate')
        AllergenContainmentCode = req.get('AllergenContainmentCode')
        AllergenTypeCode = req.get('AllergenTypeCode')
        AllergenStatement = req.get('AllergenStatement')
        IngredientStatement = req.get('IngredientStatement')
        AllergenDeclarationsIndicator = req.get('AllergenDeclarationsIndicator')
        Id = req.get('Id')
        # print(AllergenDeclarationsIndicator)
        if AllergenDeclarationsIndicator == 'true':
            AllergenDeclarationsIndicator = True
        else:
            AllergenDeclarationsIndicator = False

        if Id == "":
            print('add')
            Product.objects.create(gtin=gtin,BrandOwnerName=BrandOwnerName,DataProviderName=DataProviderName,ManufacturerName=ManufacturerName,ContactTypeCode=ContactTypeCode,Contact=Contact,ContactAddress=ContactAddress,ContactMethodCode=ContactMethodCode,ContactDetails=ContactDetails,BrandName=BrandName,SubBrandName=SubBrandName,ShortProductName=ShortProductName,ProductMarketingMessage=ProductMarketingMessage,SearchKeyWordsforProduct=SearchKeyWordsforProduct,ProductTypeDescription=ProductTypeDescription,Length=Length,LengthUnit=LengthUnit,Height=Height,HeightUnit=HeightUnit,Width=Width,WidthUnit=WidthUnit,GrossWeight=GrossWeight,GrossWeightUnit=GrossWeightUnit,MarketAvailabilityDate=MarketAvailabilityDate,AllergenContainmentCode=AllergenContainmentCode,AllergenTypeCode=AllergenTypeCode,AllergenStatement=AllergenStatement,IngredientStatement=IngredientStatement,AllergenDeclarationsIndicator=AllergenDeclarationsIndicator)
            return JsonResponse({'status':1,'message':'Successfully add new product.'})
        else:
            print('update')
            return JsonResponse({'status':0})


        
        