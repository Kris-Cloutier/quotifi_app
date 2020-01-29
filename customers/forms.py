from django import forms
from .models import CustomerInfo

class NewCustomerForm(forms.ModelForm):
    business_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "John's Shoe Co"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#357'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fort Worth'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Texas'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '76179'}))
    email_1 = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john@example.com'}))
    email_2 = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'jsmith@example.com'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': '555-555-5555'}))
    landline = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': '555-555-5555'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    referral = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any customer notes? Enter them here.'}))


    class Meta:
        model = CustomerInfo
        fields = '__all__' 
              