from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from customer.models import ServiceRequest  # Import the ServiceRequest model
from .forms import RequestCommentForm  # Import the form to handle comment submission


@login_required
def manage_requests(request):
    """
    View for support representatives to view all requests.
    """
    requests = ServiceRequest.objects.all()  # Get all service requests
    return render(request, 'support/manage_requests.html', {'requests': requests})


@login_required
def request_detail(request, request_id):
    """
    View to see the details of a specific service request and manage comments.
    """
    service_request = get_object_or_404(ServiceRequest, id=request_id)  # Fetch the specific service request or return 404
    comments = service_request.comments.all()  # Get all comments associated with this request

    # Handle adding a new comment
    if request.method == 'POST':
        form = RequestCommentForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():  # If the form is valid
            comment = form.save(commit=False)  # Do not save yet
            comment.service_request = service_request  # Associate the comment with the service request
            comment.created_by = request.user  # Set the user who created the comment
            comment.save()  # Save the comment
            return redirect('request_detail', request_id=request_id)  # Redirect to the same request detail page
    else:
        form = RequestCommentForm()  # Empty form for GET request

    return render(request, 'support/request_detail.html',
                  {'service_request': service_request, 'comments': comments, 'form': form})


@login_required
def update_request_status(request, request_id):
    """
    View to update the status of a service request.
    """
    service_request = get_object_or_404(ServiceRequest, id=request_id)  # Fetch the specific service request or return 404

    if request.method == 'POST':
        new_status = request.POST.get('status')  # Get the new status from POST data
        service_request.status = new_status  # Update the status of the request
        if new_status == 'Resolved':  # If the status is 'Resolved', set the resolved_at timestamp
            service_request.resolved_at = timezone.now()
        service_request.save()  # Save the updated service request
        return redirect('request_detail', request_id=request_id)  # Redirect to the request detail page

    return render(request, 'support/update_status.html', {'service_request': service_request})


def test(request):
    """
    Simple view for testing purposes to render the base template.
    """
    return render(request, 'base.html')
