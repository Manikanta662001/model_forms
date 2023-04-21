from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        
class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #exclude=['name']
        help_texts={'name':'enter a valid name','url':'accept only urls'}
        #labels={'name':'Name'}
        #widgets={'url':forms.PasswordInput}