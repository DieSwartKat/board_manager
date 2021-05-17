from django.db import models

# Create your models here.

class Role(models.Model):
    key = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.role}'

class Board(models.Model):
    board_name = models.CharField(max_length=250)
    board_id = models.CharField(max_length=250, unique=True)
    board_description = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.board_name

class Member(models.Model):
    trello_username = models.CharField(max_length=250)
    trello_member_id = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    trello_picture = models.URLField(max_length=250)

    def __str__(self) -> str:
        return self.trello_username


class Board_Member_Role(models.Model):
    db_roles = Role.objects.all()
    role_options = (('member', 'Member'),)
    for role in db_roles:
        pair = (role.key, role.role)
        role_options = (pair,) + role_options
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_options, default='member')

    def __str__(self) -> str:
        return f"{self.member.trello_username} | {self.board.board_name}"


