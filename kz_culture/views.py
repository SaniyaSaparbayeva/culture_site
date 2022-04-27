from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    about = About.objects.all()
    return render(request, 'kz_culture/index.html', {'about': about})


def clothes(request):
    clothes = Culture.objects.all()
    return render(request, 'kz_culture/NationalClothes.html', {'clothes': clothes})

def games(request):
    games = NationalGames.objects.all()
    return render(request, 'kz_culture/NationalGames.html', {'games': games})


def cuisine(request):
    cuisine = Cuisine.objects.all()
    return render(request, 'kz_culture/Cuisine.html', {'cuisine': cuisine})


def traditions(request):
    traditions = Traditions.objects.all()
    return render(request, 'kz_culture/Traditions.html', {'traditions': traditions})


def display_images(request):
    # getting all the objects of hotel.
    allimages = Culture.objects.all()
    return render(request, 'NatinalClothes.html', {'images': allimages})





def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration')

    else:
        form = RegistrationForm()

    return render(request, 'kz_culture/registration.html', {'form': form})


def send_message(request):
    # send_mail("LAB 5",
    #           "This email sended from django!!!",
    #           "200103221@stu.sdu.edu.kz",
    #           ["saniyabolatkhan@gmail.com"],
    #           fail_silently=False,
    #           html_message="<b><i>Bold Italic text<i/></b>")
    #
    # return render(request, 'kz_culture/successfull.html')

    email = EmailMessage("LAB 5",
                         "This email sended from django!!!",
                         "200103221@stu.sdu.edu.kz",
                         ["saniyabolatkhan@gmail.com"],
                         )
    email.attach_file('C:/Users/MI/Desktop/django_proj/Қазақ_ұлттық_киімдері.jpg')
    email.send(fail_silently=False)
    return render(request, 'kz_culture/successfull.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        message = request.POST['message']
        if form.is_valid():
            send_mail("Hi, "+name+" "+surname,
                      "Thank you for contacting our company! We have received your request: *** "+message+"*** Expect a response!",
                      "200103221@stu.sdu.edu.kz",
                      [email],
                      fail_silently=False
                      )
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'kz_culture/contactForm.html', {'form': form})

def addPost(request):
    if request.method == 'POST':
        form = addPostForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = addPostForm()
    return render(request, 'kz_culture/addPost.html', {'form': form})


