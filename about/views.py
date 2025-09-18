from django.contrib import messages
from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


# Create your views here.
def about_me(request):
    """
    View to render the About page with profile info and collaboration form.
    Handles collaboration form submission via POST.
    Renders the 'about/about.html' template with about info and form.
    """
    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond "
                "within 2 working days."
            )

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
