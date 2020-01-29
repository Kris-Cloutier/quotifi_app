from django import forms

from .models import Order
from customers.models import CustomerInfo

class NewOrderForm(forms.ModelForm):
    # customer_id = forms.ModelChoiceField(queryset=CustomerInfo.objects.all(), empty_label='Select Customer', to_field_name='selected_customer')
    # order_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}))
    # quantity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smith'}))
    # room_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234 Main St'}))
    # width = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#357'}))
    # height = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fort Worth'}))
    # openess = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Texas'}))
    # product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '76179'}))
    # color = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'john@example.com'}))
    # frame = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'jsmith@example.com'}))
    # custom = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': '555-555-5555'}))
    # angled_build_out = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': 'form-control', 'placeholder': '555-555-5555'}))
    # safety_drive = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # referral = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any customer notes? Enter them here.'}))


    class Meta:
        model = Order
        fields = '__all__' 

    
              