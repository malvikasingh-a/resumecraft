from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout # <--- Add this line
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Resume


# 1. The Home Page
def home(request):
    return render(request, 'index.html')

# 2. The Login Page
def login_view(request):
    if request.method == 'POST':
        # Get data
        username_data = request.POST.get('username')
        password_data = request.POST.get('password')

        # --- DEBUGGING PRINTS (Watch your Terminal!) ---
        print(f"DEBUG: Trying to login with Username: '{username_data}' and Password: '{password_data}'")
        
        # Check if user actually exists in DB
        user_check = User.objects.filter(username=username_data).first()
        if user_check:
            print(f"DEBUG: User found in database! (ID: {user_check.id})")
        else:
            print("DEBUG: User NOT found in database.")
        # -----------------------------------------------

        # Check credentials
        user = authenticate(request, username=username_data, password=password_data)

        if user is not None:
            print("DEBUG: Authentication Successful!")
            login(request, user)
            return redirect('dashboard')
        else:
            print("DEBUG: Authentication FAILED.")
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, 'login.html')

# 3. The Signup Page
def signup_view(request):
    if request.method == 'POST':
        # 1. Get data from the HTML form
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 2. Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # 3. Create the user in the database
        # We use email as the username for simplicity
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = fullname
        user.save()

        # 4. Success! Send them to login page
        messages.success(request, "Account created! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

# 4. The Dashboard
# Make sure this is at the top of the file:
# from .models import Resume 

@login_required(login_url='login')
def dashboard(request):
    # 1. Get user's resumes
    user_resumes = Resume.objects.filter(user=request.user)
    
    # 2. Send them to the HTML
    context = {'resumes': user_resumes}
    return render(request, 'dashboard.html', context)

# 5. The Editor
@login_required(login_url='login')
def editor(request, id):
    resume = get_object_or_404(Resume, id=id, user=request.user)
    
    # 1. Handle the SAVE action
    if request.method == 'POST':
        resume.full_name = request.POST.get('full_name')
        resume.job_title = request.POST.get('job_title')
        resume.email = request.POST.get('email')
        resume.phone = request.POST.get('phone')
        resume.summary = request.POST.get('summary')
        resume.skills = request.POST.get('skills')
        
        resume.save()
        messages.success(request, "Resume saved successfully!")
        return redirect('editor', id=resume.id) # Reload the page

    context = {
        'resume': resume
    }
    return render(request, 'editor.html', context)

# 6. Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def create_resume(request):
    # Create a blank resume for the user
    new_resume = Resume.objects.create(user=request.user, title="Untitled Resume")
    # Redirect them to the editor for this new resume
    return redirect('editor', id=new_resume.id)

@login_required(login_url='login')
def delete_resume(request, id):
    # 1. Find the resume (and ensure it belongs to the logged-in user)
    resume = get_object_or_404(Resume, id=id, user=request.user)
    
    # 2. Delete it
    resume.delete()
    
    # 3. Message and Redirect
    messages.success(request, "Resume deleted successfully!")
    return redirect('dashboard')