from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=225, unique=True)

class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    uid = models.ForeignKey(University, on_delete=models.CASCADE)

class Program(models.Model):
    name = models.CharField(max_length=255)
    sid = models.ForeignKey(School, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=255)
    pid = models.ForeignKey(Program, on_delete=models.CASCADE)
    year = models.IntegerField()

class Lecturer(models.Model):
    name = models.CharField(max_length=255)

class CourseLecturer(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    lid = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

class Files(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=500)
    filehash = models.CharField(max_length=64, unique=True)
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=70, unique=True)
    password = models.CharField(max_length=128)

class Query(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    query = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.query +" : "+self.answer

class UserQuery(models.Model):
    sid = models.ForeignKey(User, on_delete=models.CASCADE)
    qid = models.ForeignKey(Query, on_delete=models.CASCADE)

class Chat(models.Model):
    sid = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUsed = models.DateField(auto_now=True)

class ChatMessage(models.Model):
    Sender_choices = [
        ('student', 'Student'),
        ('ai', 'AI')
    ]
    chid = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10, choices=Sender_choices)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ChatReference(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)