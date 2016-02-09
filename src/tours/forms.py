from django import forms

from tours.models import Tour


PUBLISHED_CHOICES = (
    ('publish', "Publish"),
    ('draft', "Draft"),
    )


# Can get rid of this class
class TourAddForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "class" : "title-class",
            "placeholder" : "Title",
        }))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class" : "description-class",
            "placeholder" : "Description",
        }))

    price = forms.DecimalField()
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISHED_CHOICES)

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


class TourModelForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [
            "title",
            "description",
            "price",
        ]

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
