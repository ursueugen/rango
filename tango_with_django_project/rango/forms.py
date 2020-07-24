from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128,
        help_text='Please enter category name.')
    views = forms.IntegerField(
        widget=forms.HiddenInput(), 
        initial=0
    )
    likes = forms.IntegerField(
        widget=forms.HiddenInput(), 
        initial=0
    )
    slug = forms.CharField(
        widget=forms.HiddenInput(), 
        required=False
    )

    # inline class to provide more info on form
    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(
        max_length=128,
        help_text='Please enter the page title.'
    )
    url = forms.URLField(
        max_length=200,
        help_text="Please enter the URL of the page."
    )
    views = forms.IntegerField(
        widget=forms.HiddenInput(),
        initial=0
    )

    class Meta:
        model = Page
        # hide the category, it's a foreign key
        exclude = ('category',)  # same as fields = ('title', 'url', 'views')
    
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get('url')

    #     # if url not empty and doesn't start with
    #     #  http://, preappend. May be unnecessary in real
    #     #  app due to automatic URL checking capabilities
    #     #  of modern browsers and frameworks.
    #     if url and not url.startswith('http://'):
    #         url = 'http://' + url
    #         cleaned_data['url'] = url

    #         return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
