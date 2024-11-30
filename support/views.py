from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from customer.models import ServiceRequest, RequestComment
from .forms import RequestCommentForm  # Form for adding comments
from django.contrib.auth.decorators import user_passes_test


def is_support(user):
    return user.is_authenticated and user.groups.filter(name='Support').exists()

@login_required
@user_passes_test(is_support)
def manage_requests(request):
    """
    View to display all service requests for support representatives.
    """
    requests = ServiceRequest.objects.all()  # Fetch all service requests
    return render(request, 'support/manage_requests.html', {'requests': requests})


@login_required
@user_passes_test(is_support)
def request_detail(request, request_id):
    """
    View to display details of a specific service request and allow comments.
    """
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    comments = service_request.comments.all()  # Fetch related comments

    # Handle comment submission
    if request.method == 'POST':
        form = RequestCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.service_request = service_request
            comment.created_by = request.user
            comment.save()
            return redirect('request_detail', request_id=request_id)
    else:
        form = RequestCommentForm()

    return render(request, 'support/request_detail.html', {
        'service_request': service_request,
        'comments': comments,
        'form': form,
    })


@login_required
@user_passes_test(is_support)
def update_request_status(request, request_id):
    """
    View to update the status of a service request.
    """
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        service_request.status = new_status
        if new_status == 'resolved':
            service_request.resolved_at = timezone.now()
        service_request.save()
        return redirect('request_detail', request_id=request_id)

    return render(request, 'support/update_status.html', {'service_request': service_request})

