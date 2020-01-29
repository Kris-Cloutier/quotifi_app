from django import forms

from .models import TrsNatte

import io
import csv

class TrsPriceUpload(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        for trs_heigth in reader:
            TrsNatte.objects.update(f)