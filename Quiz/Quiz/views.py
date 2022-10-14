from django.http import HttpResponse
from django.shortcuts import render
from quiz1.models import contestant, questionbank

x = contestant.objects.raw('SELECT id,uid,email,pwd FROM quiz1_contestant')
emails = []
passwords = []
uids = []
for i in x:
    emails.append(i.email)
    passwords.append(i.pwd)
    uids.append(i.uid)

def index(request):
    return render(request, 'index.html')


def signup(request):
    uid = request.POST.get('uid')
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    if uid not in uids:
        if email not in emails:
            savingdata = contestant(uid = uid ,email=email, pwd=password)
            savingdata.save()
            return HttpResponse("Registered")
        else:
            return HttpResponse("Already Exist!!")
    else:
        return HttpResponse("UID taken!")


def login(request):
    return render(request, 'login.html')


def logch(request):
    email = request.POST.get('email')
    password = request.POST.get('pwd')

    if email not in emails:
        return HttpResponse("Wrong Credentials!!")
    else:
        if password not in passwords:
            return HttpResponse("Wrong Credentials!!")
        else:
            emails.remove(email)
            emails.append(email)
            return render(request, 'participant_admin.html')


def adm(request):
    return render(request, 'adm.html')


def add(request):
    question = request.POST.get('question')
    opt1 = request.POST.get('opt1')
    opt2 = request.POST.get('opt2')
    opt3 = request.POST.get('opt3')
    opt4 = request.POST.get('opt4')
    corr_opt = request.POST.get('corr_opt')
    Savingdata = questionbank(questions=question, opt1=opt1, opt2=opt2, opt3=opt3, opt4=opt4, corr_opt=corr_opt)
    Savingdata.save()
    return HttpResponse("Question added!")

def showquestions(request):
    r=questionbank.objects.all()
    content={"message":r}
    return render(request,"showquestions.html",content)

def dele(request):
    question = request.POST.get('question')
    questionbank.objects.filter(questions = question).delete()
    return HttpResponse("Question deleted!")

def user(request):
    q = questionbank.objects.all()
    r = contestant.objects.all().order_by('-score')
    content = {"message": q,"message2":r}
    return render(request,'user.html',content)


def calc(request):
    i = questionbank.objects.all()
    score = 0
    for j in i:
        ans = request.POST.get(j.questions)
        if j.corr_opt == ans:
            score = score + 1
        else:
            pass
    contestant.objects.filter(email = emails[-1]).update(score = score)
    r = contestant.objects.all().order_by('-score')
    content = {"message": i,"message2":r}
    return render(request,'public_leaderboard.html',content)

def public_leaderboard(request):
    r = contestant.objects.all().order_by('-score')
    content = { "message2": r}
    return render(request, 'public_leaderboard.html')



