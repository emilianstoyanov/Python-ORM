from django.db import models


class CustomManager(models.Manager):
    def my_custom_query(self):
        return "Really hard filtration"


