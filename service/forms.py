from django.forms import ModelForm

from service.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['updated', 'created','user']

    def clean_locationCode(self):
        locationCode = self.cleaned_data.get('locationCode').upper()
        if len(locationCode) != 3:
            self.add_error("locationCode","This is not avalid locationCode")
        if self.instance.locationCode != locationCode:
            service = Service.objects.filter(locationCode=locationCode)
            if service.exists():
                self.add_error("locationCode", "already exist locationCode="+locationCode)

        return locationCode
