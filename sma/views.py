from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from sma.access_decorators_mixins import mentor_access_required, staff_access_required
from django.db import connection,transaction

# Create your views here.

def staffSignup(request):
    if request.method == "GET":
        return render(request, "sma/staff_signup.html", {})

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("email"),
                is_staff=True, role='staff'
            )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect(reverse("sma:homepage",))
        else:
            return render(
                request, "sma/staff_signup.html", {"errors": form.errors}
            )


def mentorSignup(request):
    if request.method == "GET":
        return render(request, "sma/mentor_signup.html", {})

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("email"),
                is_mentor=True, role="mentor",
            )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            login(request, user)
            return redirect(reverse("sma:homepage",))
        else:
            return render(
                request, "sma/mentor_signup.html", {"errors": form.errors}
            )


def mentorLogin(request):
    if request.method == "GET":
        return render(request, "sma/mentor_login.html", {})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password,)
            if user is None:
                return render(
                    request,
                    "sma/mentor_login.html",
                    {"errors": {"account_error": ["Invalid email or password"]}},
                )

            elif user is not None:
                if user.is_active and user.is_mentor:
                    login(request, user)
                    return HttpResponseRedirect(reverse("sma:homepage",))
                elif user.is_active and user.is_mentor is False:
                    return render(
                        request,
                        "sma/mentor_login.html",
                        {
                            "errors": {
                                "account_error": ["Email is not associated with Mentor"]
                            }
                        },
                    )

                else:
                    return HttpResponse(
                        "# your account is inactive contact admin for details user@example.com"
                    )

            else:
                pass
        else:
            return render(request, "sma/mentor_login.html", {"errors": form.errors})




def staffLogin(request):
    if request.method == "GET":
        return render(request, "sma/staff_login.html", {})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password,)
            if user is None:
                return render(
                    request,
                    "sma/staff_login.html",
                    {"errors": {"account_error": ["Invalid email or password"]}},
                )

            elif user is not None:
                if user.is_active and user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect(reverse("sma:homepage",))
                elif user.is_active and user.is_mentor is False:
                    return render(
                        request,
                        "sma/staff_login.html",
                        {
                            "errors": {
                                "account_error": ["Email is not associated with Staff"]
                            }
                        },
                    )

                else:
                    return HttpResponse(
                        "# your account is inactive contact admin for details user@example.com"
                    )

            else:
                pass
        else:
            return render(request, "sma/staff_login.html", {"errors": form.errors})


def change_password(request):
    form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.method == 'GET':
        return render(request, "sma/password_change_form.html", {"form": form})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(
                request, "sma/password_change_done.html", {}
            )
        return render(
            request, "sma/password_change_form.html", {"errors": form.errors}
        )



def homepage(request):
    #print('yessss')
    # return HttpResponse("test sma")
    return render(request, "sma/landing_page.html", {})


def user_logout(request):
    logout(request)
    return redirect(reverse("sma:homepage"))


def session_list(request):
    session = Session_Schedule.objects.filter(session_start_date__lte=timezone.now())
    return render(request, 'sma/session_list.html',
                 {'session_list': session})


def session_details(request,pk):
    cursor = connection.cursor()
    cursor.execute("Select DISTINCT student_first_name,student_last_name from sma_session_schedule ss\
    INNER join sma_student_group_mentor_assignment sgm\
    On ss.group_id=sgm.id\
    inner join sma_grade g\
    On sgm.grade_id=g.id\
    inner join sma_student s\
    On s.grade_id=g.id")
    row = cursor.fetchall()
    return render(request, 'sma/session_details.html',{'session_details': row})


