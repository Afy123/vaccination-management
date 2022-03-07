from django.shortcuts import render, redirect

from vaccineapp.forms import VaccinationScheduleForm, ComplaintForm
from vaccineapp.models import User, Hospital, Vaccine, Complaint, VaccinationSchedule, Appointment


def user_view(request):
    u = User.objects.all()
    return render(request, 'Nurse/user_view.html', {'user': u})


def hospital_view(request):
    h = Hospital.objects.all()
    return render(request, 'Nurse/hospital_view.html', {'hospital': h})


def vaccine_view(request):
    v = Vaccine.objects.all()
    return render(request, 'Nurse/vaccine_view.html', {'vaccine': v})


def complaint_view(request):
    u = request.user
    c = Complaint.objects.filter(User=u)
    return render(request, 'Nurse/complaint_view.html', {'complaint': c})


def vaccinationSchedule_view(request):
    vs = VaccinationSchedule.objects.all()
    return render(request, 'Nurse/vaccinationschedule_view.html', {'vaccinationschedule': vs})


def vaccinationschedule_add(request):
    form = VaccinationScheduleForm()
    if request.method == 'POST':
        form = VaccinationScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccinationSchedule_add_nurse')
    else:
        return render(request, 'Nurse/vaccinationschedule_add.html', {'form': form})


def complaint_add(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.User = u
            form.save()
            return redirect('complaint_add_nurse')
    else:
        return render(request, 'Nurse/complaint_add.html', {'form': form})


def vaccinationSchedule_delete(request, id):
    n = VaccinationSchedule.objects.get(id=id)
    n.delete()
    return redirect('vaccinationSchedule_view_nurse')


def vaccinationSchedule_update(request, id):
    n = VaccinationSchedule.objects.get(id=id)
    if request.method == 'POST':
        form = VaccinationScheduleForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('vaccinationSchedule_view_nurse')
    else:
        form = VaccinationScheduleForm(instance=n)
    return render(request, 'Nurse/vaccinationSchedule_update.html', {'form': form})


def appointment_status(request):
    a = Appointment.objects.filter(Status=1)
    return render(request, 'Nurse/appointment_status.html', {'appointment': a})


def mark_vaccinated(request, id):
    a = Appointment.objects.get(id=id)
    a.Vaccinated = True
    a.save()
    return redirect('appointment_status')


def unmark_vaccinated(request, id):
    a = Appointment.objects.get(id=id)
    a.Vaccinated = False
    a.save()
    return redirect('appointment_status')
