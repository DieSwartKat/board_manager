from django.db import models

# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Board(models.Model):
    board_name = models.CharField(max_length=250)
    board_id = models.CharField(max_length=250, unique=True)
    board_description = models.TextField(max_length=250)

class Member(models.Model):
    trello_username = models.CharField(max_length=250)
    trello_member_id = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    trello_picture = models.URLField(max_length=250)

class Board_Member_Role(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)



