from django.db import models
from django.contrib.auth.models import User
from student.models import Submission

class Feedback(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)