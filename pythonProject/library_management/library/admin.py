from django.contrib import admin
from . import models

admin.site.register(models.Customer)
admin.site.register(models.Book)
admin.site.register(models.BorrowedBook)
admin.site.register(models.Category)

