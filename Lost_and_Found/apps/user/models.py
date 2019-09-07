from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        db_table = 'user'

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_email = models.EmailField()
    item_telephone = models.CharField(max_length=11)
    item_type = models.ForeignKey("Type", on_delete=models.CASCADE)
    item_user = models.ForeignKey("User", on_delete=models.CASCADE)
    #picture = models.ForeignKey("Picture", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=False)
    time = models.CharField(max_length=20, null=False)
    area = models.CharField(max_length=10, null=False)
    location = models.TextField(null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    detail = models.TextField(null=False)
    price = models.CharField(max_length=10)
    is_found = models.BooleanField(default=False)

    class Meta:
        db_table = 'item'


class Type(models.Model):
    name = models.CharField(max_length=5, null=False)

    class Meta:
        db_table = 'type'


class Picture(models.Model):
    id=models.AutoField(primary_key=True)
    pic1 = models.ImageField(upload_to='media')
    pic2 = models.ImageField(upload_to='media')
    pic3 = models.ImageField(upload_to='media')
    item = models.OneToOneField("Item", on_delete=models.CASCADE)

    class Meta:
        db_table = 'picture'


class Suggestion(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        db_table = 'suggestions'


# class Answer(models.Model):
#     id = models.AutoField(primary_key=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     suggestion_id = models.ForeignKey("Suggestion", on_delete=models.CASCADE)
#     user_id = models.ForeignKey("User", on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'answer'
