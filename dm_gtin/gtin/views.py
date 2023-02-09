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
class loginUser(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if 'login' in request.session:
            return redirect('/dashboard/')
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        req = request.POST
        print('--------')
        username = req.get('username')
        password = req.get('password')
        if username == "admin" and password == "passme2023":
            request.session['userId'] = 10
            request.session['login'] = True
            request.session['userRole'] = 1
            request.session['userName'] = username
            return JsonResponse({'status':1,'message':'Login success'})
        elif username == "user" and password == "passme2023":
            request.session['userId'] = 11
            request.session['login'] = True
            request.session['userRole'] = 2
            request.session['userName'] = username
            return JsonResponse({'status':1,'message':'Login success'})
        else:
            return JsonResponse({'status':0,'message':'Invalid username or password'})
        
class logout(View):
    def get(self, request, *args, **kwargs):
        for key in list(request.session.keys()):
            del request.session[key]
        return redirect('/')
        
    
class generateGtin(View):
    template_name = 'generate-gtin.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('/')
        return render(request, self.template_name)

class GTINList(View):
    template_name = 'gtin-list.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('/')
        return render(request, self.template_name)

class GTINProductEntry(View):
    template_name = 'gtin-product-entry.html'

    def get(self, request, *args, **kwargs):
        if 'login' not in request.session:
            return redirect('/')
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        data=[]
        Product_data =Product.objects.filter()
        for Products in Product_data:
            print(Products)
            data.append({ 
                'gtin' :  Products.gtin,
                'BrandOwnerName' : Products.BrandOwnerName,
                'DataProviderName' : Products.DataProviderName,
                'ManufacturerName' : Products.ManufacturerName,
                'ContactTypeCode' : Products.ContactTypeCode,
                'Contact' : Products.Contact,
                'ContactAddress' : Products.ContactAddress,
                'ContactMethodCode':Products.ContactMethodCode,
                'ContactDetails' : Products.ContactDetails,
                'BrandName' : Products.BrandName,
                'SubBrandName' : Products.SubBrandName,
                'ShortProductName' : Products.ShortProductName,
                'ProductMarketingMessage' : Products.ProductMarketingMessage,
                'SearchKeyWordsforProduct' : Products.SearchKeyWordsforProduct,
                'ProductTypeDescription':Products.ProductTypeDescription,
                'Length' : Products.Length,
                'LengthUnit' : Products.LengthUnit,
                'Height' : Products.Height,
                'HeightUnit' : Products.HeightUnit,
                'Width' : Products.Width,
                'WidthUnit' : Products.WidthUnit,
                'GrossWeight':Products.GrossWeight,
                'GrossWeightUnit' : Products.GrossWeightUnit,
                'MarketAvailabilityDate' : Products.MarketAvailabilityDate,
                'AllergenContainmentCode' : Products.AllergenContainmentCode,
                'AllergenTypeCode' : Products.AllergenTypeCode,
                'AllergenStatement' : Products.AllergenStatement,
                'IngredientStatement' : Products.IngredientStatement,
                'AllergenDeclarationsIndicator':Products.AllergenDeclarationsIndicator,
                'id':Products.id,
                'GPCCode' :Products.GPCCode,
                'FeedTypeCertification' :Products.FeedTypeCertification,
                'svrStatus' :Products.svrStatus,
            }) 
        return JsonResponse({'data':data})

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
        GPCCode = req.get('GPCCode')
        FeedTypeCertification = req.get('FeedTypeCertification')
        Id = req.get('Id')
        svrStatus = req.get('svrStatus')
        
        print(MarketAvailabilityDate)
        if MarketAvailabilityDate == "":
            MarketAvailabilityDate = None
        if Length == "":
            Length = 0
        if Height == "":
            Height = 0
        if Width == "":
            Width = 0
        if GrossWeight == "":
            GrossWeight = 0
        print(AllergenDeclarationsIndicator)
        print("AllergenDeclarationsIndicator")
        if AllergenDeclarationsIndicator == 'false':
            AllergenDeclarationsIndicator = False
        else:
            AllergenDeclarationsIndicator = True
        
        
        if Id == "":
            res = Product.objects.create(gtin=gtin,BrandOwnerName=BrandOwnerName,DataProviderName=DataProviderName,ManufacturerName=ManufacturerName,ContactTypeCode=ContactTypeCode,Contact=Contact,ContactAddress=ContactAddress,ContactMethodCode=ContactMethodCode,ContactDetails=ContactDetails,BrandName=BrandName,SubBrandName=SubBrandName,ShortProductName=ShortProductName,ProductMarketingMessage=ProductMarketingMessage,SearchKeyWordsforProduct=SearchKeyWordsforProduct,ProductTypeDescription=ProductTypeDescription,Length=Length,LengthUnit=LengthUnit,Height=Height,HeightUnit=HeightUnit,Width=Width,WidthUnit=WidthUnit,GrossWeight=GrossWeight,GrossWeightUnit=GrossWeightUnit,MarketAvailabilityDate=MarketAvailabilityDate,AllergenContainmentCode=AllergenContainmentCode,AllergenTypeCode=AllergenTypeCode,AllergenStatement=AllergenStatement,IngredientStatement=IngredientStatement,AllergenDeclarationsIndicator=AllergenDeclarationsIndicator,svrStatus=1,GPCCode=GPCCode,FeedTypeCertification=FeedTypeCertification)
            return JsonResponse({'status':1,'message':'Successfully add new product.','id':res.id})
        else:
            Product.objects.filter(id=Id).update(BrandOwnerName=BrandOwnerName,DataProviderName=DataProviderName,ManufacturerName=ManufacturerName,ContactTypeCode=ContactTypeCode,Contact=Contact,ContactAddress=ContactAddress,ContactMethodCode=ContactMethodCode,ContactDetails=ContactDetails,BrandName=BrandName,SubBrandName=SubBrandName,ShortProductName=ShortProductName,ProductMarketingMessage=ProductMarketingMessage,SearchKeyWordsforProduct=SearchKeyWordsforProduct,ProductTypeDescription=ProductTypeDescription,Length=Length,LengthUnit=LengthUnit,Height=Height,HeightUnit=HeightUnit,Width=Width,WidthUnit=WidthUnit,GrossWeight=GrossWeight,GrossWeightUnit=GrossWeightUnit,MarketAvailabilityDate=MarketAvailabilityDate,AllergenContainmentCode=AllergenContainmentCode,AllergenTypeCode=AllergenTypeCode,AllergenStatement=AllergenStatement,IngredientStatement=IngredientStatement,AllergenDeclarationsIndicator=AllergenDeclarationsIndicator,svrStatus=svrStatus,GPCCode=GPCCode,FeedTypeCertification=FeedTypeCertification)
            return JsonResponse({'status':1,'message':'Successfully update product.'})
       
class editGTINProductEntry(View):
    template_name = 'gtin-product-entry.html'

    def post(self, request, *args, **kwargs):
        data = []
        req = request.POST
        id = req.get('id')
        res = Product.objects.filter(id=id)
        data.append({
            'gtin': res[0].gtin,
            'BrandOwnerName' : res[0].BrandOwnerName,
            'DataProviderName' : res[0].DataProviderName,
            'ManufacturerName' : res[0].ManufacturerName,
            'ContactTypeCode' : res[0].ContactTypeCode,
            'Contact' : res[0].Contact,
            'ContactAddress' : res[0].ContactAddress,
            'ContactMethodCode':res[0].ContactMethodCode,
            'ContactDetails' : res[0].ContactDetails,
            'BrandName' : res[0].BrandName,
            'SubBrandName' : res[0].SubBrandName,
            'ShortProductName' : res[0].ShortProductName,
            'ProductMarketingMessage' : res[0].ProductMarketingMessage,
            'SearchKeyWordsforProduct' : res[0].SearchKeyWordsforProduct,
            'ProductTypeDescription':res[0].ProductTypeDescription,
            'Length' : res[0].Length,
            'LengthUnit' : res[0].LengthUnit,
            'Height' : res[0].Height,
            'HeightUnit' : res[0].HeightUnit,
            'Width' : res[0].Width,
            'WidthUnit' : res[0].WidthUnit,
            'GrossWeight':res[0].GrossWeight,
            'GrossWeightUnit' : res[0].GrossWeightUnit,
            'MarketAvailabilityDate' : res[0].MarketAvailabilityDate,
            'AllergenContainmentCode' : res[0].AllergenContainmentCode,
            'AllergenTypeCode' : res[0].AllergenTypeCode,
            'AllergenStatement' : res[0].AllergenStatement,
            'IngredientStatement' : res[0].IngredientStatement,
            'AllergenDeclarationsIndicator':res[0].AllergenDeclarationsIndicator,
            'svrStatus':res[0].svrStatus,
            'GPCCode':res[0].GPCCode,
            'FeedTypeCertification':res[0].FeedTypeCertification,
        })

        return JsonResponse({'status':1,'data':data})


        
        