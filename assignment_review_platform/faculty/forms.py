from django import forms
from assignments.models import Assignment, Feedback

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'course', 'due_date']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
    
    status = forms.ChoiceField(choices=[
        ('accepted', 'Accept Submission'),
        ('needs_modification', 'Request Modifications')
    ])