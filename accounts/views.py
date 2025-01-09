from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import UploadedFile
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def authors_and_sellers(request):
    # Fetch users with 'public_visibility' set to True
    visible_users = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'authors_and_sellers.html', {'users': visible_users})

@login_required
def upload_books(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        visibility = request.POST['visibility']
        cost = request.POST.get('cost', None)
        year_published = request.POST['year_published']
        file = request.FILES['file']

        UploadedFile.objects.create(
            user=request.user,
            title=title,
            description=description,
            visibility=visibility,
            cost=cost,
            year_published=year_published,
            file=file
        )
        return redirect('uploaded_files')

    return render(request, 'upload_books.html', {'current_year': now().year})

@login_required
def uploaded_files(request):
    user_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'uploaded_files.html', {'files': user_files})
