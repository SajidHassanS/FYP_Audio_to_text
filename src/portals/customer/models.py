from django.db import models


class ConvertRequest(models.Model):
    name = models.CharField(max_length=255, help_text="Enter name of file here.")
    url = models.URLField(null=True, blank=True, help_text="Url where to embed file directly")
    file_url = models.FileField(max_length=255,  help_text="Upload your audio file here")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Convert Requests"

    def __str__(self):
        return self.name
