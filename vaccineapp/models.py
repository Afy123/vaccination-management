from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Hospital(models.Model):
    Name = models.CharField(max_length=200)
    Place = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Email = models.EmailField()

    def __str__(self):
        return f'{self.Name},{self.Place}'


class Nurse(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='nurse')
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Address = models.CharField(max_length=200)
    Hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.Name


class User(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='user')
    Name = models.CharField(max_length=200)
    Contact_No = PhoneNumberField(unique=True, null=False, blank=False)
    Address = models.CharField(max_length=200)
    Child_Name = models.CharField(max_length=200)
    Child_Age = models.IntegerField()
    Child_Gender = models.CharField(max_length=100)
    Recent_Vaccination = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.Name


class Vaccine(models.Model):
    Vaccine_Name = models.CharField(max_length=200)
    Vaccine_Type = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Approval_Status = models.IntegerField()

    def __str__(self):
        return self.Vaccine_Name


class VaccinationSchedule(models.Model):
    Hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Date = models.DateField()
    Start_Time = models.TimeField()
    End_Time = models.TimeField()


class Complaint(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=200)
    Complaint = models.TextField()
    Date = models.DateField()
    Reply = models.TextField(null=True, blank=True)


class Appointment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    Schedule = models.ForeignKey(VaccinationSchedule, on_delete=models.CASCADE)
    Status = models.IntegerField(default=0)
    Vaccine_Name = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, null=True, blank=True)
    Vaccinated = models.BooleanField(default=False)


class ReportCard(models.Model):
    Vaccine = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, related_name='vaccine')
    Patient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='patient')
