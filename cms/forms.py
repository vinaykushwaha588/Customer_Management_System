from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields =('image','name','mobile','email','address')

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

