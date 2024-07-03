from django.db import models

class FactModel(models.Model):
    numstr  = models.CharField(max_length=50)
    fact_val= models.CharField(max_length=50)
    
    def __str__(self):
        return 'factorial of ' + self.numstr + ' : ' + self.fact_val

    #class Meta:
    #    ordering = ['numstr',]


"""
class FactForm(forms.Form):
    ename =forms.CharField(max_length=30)
    eaddress = forms.CharField(widget=forms.Textarea)
    ejoin_dt =forms.DateTimeField()
    edept = forms.CharField(max_length=30)

class FactModelForm(forms.ModelForm):
    class Meta:
        model = PatternModel
        exclude = ('fcontent','linecount','match','nomatch','blank','timestamp',)
        
"""
