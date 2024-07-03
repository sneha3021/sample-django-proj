from django.db import models

class FiboModel(models.Model):
    numstr = models.CharField(max_length=50)
    terms = models.TextField()
    
    def __str__(self):
        return 'The first ' + self.numstr + ' terms in fibonacci series : ' + self.terms

    class Meta:
        ordering = ['numstr',]
