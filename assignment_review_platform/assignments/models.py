from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    version = models.FloatField(default=1.0)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('needs_modification', 'Needs Modification')
    ], default='pending')

class Feedback(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    value = models.FloatField()

# Create your models here.
