from django.db import models

class User(models.Model):
    nickname = models.CharField('昵称', max_length=150)
    openid = models.CharField('ID', max_length=128, primary_key=True)
    head = models.URLField('头像')
    gender = models.CharField('性别', max_length=2, default='保密')
    telephone = models.CharField(max_length=11)
    password = models.CharField(max_length=20)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return "[{id},{name},{author},{price}]".format(id=self.id, name=self.name, author=self.author, price=self.price)
