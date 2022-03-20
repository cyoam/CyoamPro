from django import forms

# Contact Form


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        label='Your Email', max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Email'})
    )
    address = forms.CharField(label='Your Address', max_length=100)
    company = forms.CharField(label='Your Company', max_length=100)
    date = forms.DateField(label='When do you want to start?')
    budget = forms.CharField(label="What your budget?", max_length=10)
    description = forms.CharField(widget=forms.Textarea, label="What your budget?", max_length=100)