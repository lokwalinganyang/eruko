from django.db import models

class SaccoForm(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='sacco_forms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title