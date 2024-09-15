from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.models import Submission
from .models import Feedback

@login_required
def dashboard(request):
    pending_reviews = Submission.objects.filter(status='pending').order_by('submitted_at')
    return render(request, 'faculty/dashboard.html', {'pending_reviews': pending_reviews})

@login_required
def review_submission(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        status = request.POST.get('status')
        Feedback.objects.create(submission=submission, faculty=request.user, comment=comment)
        submission.status = status
        submission.save()
        return redirect('faculty:dashboard')
    return render(request, 'faculty/review_submission.html', {'submission': submission})