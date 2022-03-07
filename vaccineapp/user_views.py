from django.shortcuts import redirect, render

from vaccineapp.forms import UserRegister, ComplaintForm
from vaccineapp.models import VaccinationSchedule, User, Appointment, Complaint, ReportCard


def profile_view(request):
    u = request.user
    p = User.objects.filter(User=u)
    return render(request, 'User/profile_view.html', {'profileview': p})


def vaccinationSchedule_view(request):
    vs = VaccinationSchedule.objects.all()
    return render(request, 'User/vaccinationSchedule_view.html', {'vaccinationschedule': vs})


def appointment_view(request):
    u = User.objects.get(User = request.user)
    av = Appointment.objects.filter(User=u)
    return render(request, 'User/appointment_view.html', {'appointmentview': av})


def report_card_view(request):
    u = User.objects.get(User=request.user)
    r = ReportCard.objects.filter(Patient=u)
    return render(request, 'User/report_card.html', {'reportview': r})


def complaint_view(request):
    u = request.user
    c = Complaint.objects.filter(User=u)
    return render(request, 'User/complaint_reply.html', {'complaint': c})


def book_appointment(request, id):
    schedule = VaccinationSchedule.objects.get(id=id)
    u = User.objects.get(User=request.user)
    appointment = Appointment.objects.filter(User=u, Schedule=schedule)
    if appointment.exists():
        return redirect('vaccinationSchedule_view_user')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.User = u
            obj.Schedule = schedule
            obj.save()
            return redirect('appointment_view_status')
    return render(request, 'User/book_appointment.html', {'schedule': schedule})


def profile_update(request, id):
    n = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserRegister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserRegister(instance=n)
    return render(request, 'User/profile_update.html', {'form': form})


def register_complaint(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            form.save()
            return redirect('complaint_register')
    else:
        return render(request, 'User/complaint_register.html', {'form': form})
