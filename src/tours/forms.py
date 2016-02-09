from django import forms

class TourAddForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

    # Form Validations Here
    def clean_price(self):
        price = self.cleaned_data.get("price")
        return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 140:
            raise forms.ValidationError("Title cannot be greater than 140 characters long.")
        elif len(title) < 5:
            raise forms.ValidationError("Title cannot be smaller than 5 characters long.")
        else:
            return title
