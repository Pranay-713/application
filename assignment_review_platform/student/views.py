from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Assignment, Submission

@login_required
def dashboard(request):
    upcoming_assignments = Assignment.objects.all().order_by('due_date')[:5]
    recent_submissions = Submission.objects.filter(student=request.user).order_by('-submitted_at')[:5]
    return render(request, 'student/dashboard.html', {
        'upcoming_assignments': upcoming_assignments,
        'recent_submissions': recent_submissions
    })

@login_required
def submit_assignment(request, assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            submission = Submission(assignment=assignment, student=request.user, file=file)
            submission.save()
            return redirect('student:dashboard')
    return render(request, 'student/submit_assignment.html', {'assignment': assignment})