from django.db import models


class URLItem(models.Model):
    url_string = models.CharField(max_length=2083)  # 2083 max length of a URL
    code = models.CharField(max_length=5)  # code should be 5 char long?

    def __str__(self):
        return self.url_string
