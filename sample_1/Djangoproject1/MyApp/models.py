from django.db import models
from django import forms

class MyAppBlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-timestamp',]
"""
class MyAppBlogPostForm(forms.Form):
    title = forms.CharField(max_length=150)
    #body = forms.CharField(widget=forms.Textarea)
    #body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60}))
    #body = forms.CharField(widget=forms.Textarea(attrs=dict(zip(('rows','cols'),(3,60))))) 
    #body = forms.CharField(widget=forms.Textarea(attribs=dict(zip(('rows','cols'),(3,60))))) 
    body = forms.CharField(widget=forms.Textarea(attrs=dict([('rows',3),('cols',60)]))) 
    timestamp = forms.DateTimeField()
"""
class MyAppBlogPostForm(forms.ModelForm):
    class Meta:
        model = MyAppBlogPost
        exclude = ('timestamp',)
    
