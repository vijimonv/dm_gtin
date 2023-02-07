from distutils.command.upload import upload
import profile
from django.db import models
from django.forms import ModelForm, DateField, ChoiceField, CharField
from datetime import date
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField
from django.forms.widgets import MultipleHiddenInput
from django.contrib.postgres.fields import *

from django.contrib.auth.models import User,Group

# Create your models here.

class Product(models.Model):
    gtin = models.CharField(max_length=50)
    BrandOwnerName = models.CharField(max_length=225)
    DataProviderName = models.CharField(max_length=225)
    ManufacturerName = models.CharField(max_length=225)
    ContactTypeCode = models.CharField(max_length=225)
    Contact = models.CharField(max_length=50)
    ContactAddress = models.TextField()
    ContactMethodCode = models.CharField(max_length=225)
    ContactDetails = models.TextField()
    BrandName = models.CharField(max_length=225)
    SubBrandName = models.CharField(max_length=225)
    ShortProductName = models.CharField(max_length=225)
    ProductMarketingMessage = models.TextField()
    SearchKeyWordsforProduct = models.TextField()
    ProductTypeDescription = models.TextField()
    Length = models.IntegerField(default=0)
    LengthUnit = models.CharField(max_length=10)
    Height = models.IntegerField(default=0)
    HeightUnit = models.CharField(max_length=10)
    Width = models.IntegerField(default=0)
    WidthUnit = models.CharField(max_length=10)
    GrossWeight = models.IntegerField(default=0)
    GrossWeightUnit = models.CharField(max_length=10)
    MarketAvailabilityDate = models.DateField()
    AllergenContainmentCode = models.CharField(max_length=225)
    AllergenTypeCode = models.CharField(max_length=225)
    AllergenStatement = models.CharField(max_length=225)
    IngredientStatement = models.TextField()
    AllergenDeclarationsIndicator = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
