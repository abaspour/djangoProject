from django import forms
from django.forms import ModelForm

from flight.models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ['updated','created']

    def clean(self):
        cleaned_data = super().clean()
        origin= self.cleaned_data.get('origin')
        desti = self.cleaned_data.get('destination')
        if origin==desti:
            self.add_error("origin","This is not  valid origin and destination")

    def clean_flightNo(self):
        flightNo= self.cleaned_data.get('flightNo').upper()
        if self.instance.flightNo!=flightNo:
            flight=Flight.objects.filter(flightNo=flightNo)
            if flight.exists():
                self.add_error("flightNo","already exist flightNo="+flightNo)
        return flightNo

    def clean_edt(self):
        edt = self.cleaned_data.get('edt')
        if edt > 24 or edt <= 0:
            raise forms.ValidationError("This is not a valid edt")
        return edt

    def clean_estimatedDuration(self):
        estimatedDuration = self.cleaned_data.get('estimatedDuration')
        if estimatedDuration > 2 or estimatedDuration <= 0:
            raise forms.ValidationError("This is not a valid estimatedDuration")
        return estimatedDuration