from django.shortcuts import redirect, render

from vaccineapp.forms import HospitalForm, VaccineForm, AppointmentForm, ReportForm
from vaccineapp.models import Nurse, User, Hospital, Vaccine, Appointment, ReportCard, Complaint


def nurse_view(request):
    n = Nurse.objects.all()
    return render(request, 'Admin/nurse_view.html', {'nurse': n})


def user_view(request):
    u = User.objects.all()
    return render(request, 'Admin/user_view.html', {'user': u})


def hospital_view(request):
    h = Hospital.objects.all()
    return render(request, 'Admin/hospital_view.html', {'hospital': h})


def vaccine_view(request):
    v = Vaccine.objects.all()
    return render(request, 'Admin/vaccine_view.html', {'vaccine': v})


def complaint_view(request):
    c = Complaint.objects.all()
    return render(request, 'Admin/complaint_view.html', {'complaint': c})


def appointment_view(request):
    a = Appointment.objects.all()
    return render(request, 'Admin/appointment_view.html', {'appointment': a})


def report_view(request):
    r = ReportCard.objects.all()
    return render(request, 'Admin/report_view.html', {'report': r})


def hospital_add(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_add')
    else:
        return render(request, 'Admin/hospital_add.html', {'form': form})


def vaccine_add(request):
    form = VaccineForm()
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccine_add')
    else:
        return render(request, 'Admin/vaccine_add.html', {'form': form})


def report_add(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_view')
    else:
        return render(request, 'Admin/report_add.html', {'form': form})


def nurse_delete(request,id):
    n = Nurse.objects.get(id=id)
    n.delete()
    return redirect('nurse_view')


def user_delete(request,id):
    n = User.objects.get(id=id)
    n.delete()
    return redirect('user_view')


def hospital_delete(request,id):
    n = Hospital.objects.get(id=id)
    n.delete()
    return redirect('hospital_view')


def vaccine_delete(request,id):
    n = Vaccine.objects.get(id=id)
    n.delete()
    return redirect('vaccine_view')


def appointment_delete(request,id):
    n = Appointment.objects.get(id=id)
    n.delete()
    return redirect('appointment_view')


def report_delete(request,id):
    n = ReportCard.objects.get(id=id)
    n.delete()
    return redirect('report_view')


def complaint_delete(request,id):
    n = Complaint.objects.get(id=id)
    n.delete()
    return redirect('complaint_view')


def hospital_update(request, id):
    n = Hospital.objects.get(id=id)
    if request.method == 'POST':
        form = HospitalForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('hospital_view')
    else:
        form = HospitalForm(instance=n)
    return render(request, 'Admin/hospital_update.html', {'form': form})


def vaccine_update(request, id):
    n = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        form = VaccineForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('vaccine_view')
    else:
        form = VaccineForm(instance=n)
    return render(request, 'Admin/vaccine_update.html', {'form': form})


def complaint_reply(request, id):
    c = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        c.Reply = r
        c.save()
        return redirect('complaint_view')
    return render(request, 'Admin/complaint_reply.html', {'complaint': c})


def confirm_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.Status = 1
    a.save()
    return redirect('appointment_view')


def reject_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.Status = 2
    a.save()
    return redirect('appointment_view')
