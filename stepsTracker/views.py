from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Sum
from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView

# Create your views here.
from .forms import CreateStepsForm, UpdateStepForm
from .models import Step


# def home(request):
#     return render(request, 'stepsTracker/index.html')


# class CreateStepsView(CreateView):
#     model = Step
#     template_name = 'stepsTracker/createSteps.html'
#     # fields = "__all__"
#     form_class = CreateStepsForm
#
#     def form_valid(self, form):
#         profile = form.save(commit=False)
#         profile.user = self.request.user
#         profile.save()


def register(request):
    if request.method == "POST":
        team_name = request.POST["team_name"]
        lead_name = request.POST["lead_name"]
        username = str(request.POST["username"]).lower()
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        my_list = [team_name, lead_name, username, password1, password2]

        if "" in my_list:
            return render(
                request,
                "stepsTracker/register.html",
                {"error": "Fields can't be blank"},
            )

        if password1 == password2:
            try:
                user = User.objects.create_user(
                    username=username,
                    first_name=team_name,
                    last_name=lead_name,
                    password=password1,
                )
                user.save()
                messages.success(request, "You have registered successfully!")
                login(request, user)
                return redirect("add-steps")

            except ValueError:
                return render(
                    request,
                    "stepsTracker/register.html",
                    {"error": "Username can't be blank"},
                )

            except IntegrityError:
                return render(
                    request,
                    "stepsTracker/register.html",
                    {"error": "Username already taken. Please choose another one"},
                )
        else:
            return render(
                request,
                "stepsTracker/register.html",
                {"error": "Passwords did not match"},
            )

    else:
        return render(request, "stepsTracker/register.html")


def signin(request):
    if request.method == "POST":
        username = str(request.POST["username"]).lower()
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user:
            login(request, user)
            ifUserSteps = Step.objects.filter(user=user.id).values()
            if ifUserSteps:
                return redirect("home")
            else:
                return redirect("add-steps")
        else:
            messages.error(request, "Unable to verify username and password")
            return redirect("signin")

    return render(request, "stepsTracker/signin.html")


def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("/")


def addSteps(request):
    form = CreateStepsForm()

    if request.method == "POST":
        try:
            request.POST = request.POST.copy()
            form = CreateStepsForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, "You have added your steps successfully!")
            return redirect("home")
        except ValueError:
            return render(
                request,
                "stepsTracker/signin.html",
                {"error": "You need to login first"},
            )

    context = {"form": form}
    return render(request, "stepsTracker/createSteps.html", context)


class HomeView(ListView):
    model = Step
    template_name = "stepsTracker/index.html"
    ordering = ["-steps"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Step.objects.all()

        allSteps = []
        for item in context["qs"]:
            allSteps.append([int(item.steps), str(item)])

        top5 = sorted(allSteps, key=lambda x: -x[0])

        top5 = top5[:5]

        for i in range(5):
            top5[i][1] = User.objects.get(username=top5[i][1]).last_name

        context["top5"] = top5

        context["totalSteps"] = int(
            list(Step.objects.aggregate(Sum("steps")).values())[0]
        )

        top5 = sorted(top5, key=lambda x: x[1], reverse=False)

        context["first"] = top5[0]
        context["second"] = top5[1]
        context["third"] = top5[2]
        context["fourth"] = top5[3]
        context["fifth"] = top5[4]

        return context


class StepDetailView(DetailView):
    model = Step
    template_name = "stepsTracker/viewSteps.html"


class UpdateStepView(UpdateView):
    model = Step
    template_name = "stepsTracker/updateSteps.html"
    form_class = UpdateStepForm
