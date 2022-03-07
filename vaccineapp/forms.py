
from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField

from vaccineapp.models import Hospital, Vaccine, Appointment, ReportCard, Complaint, VaccinationSchedule, Login, Nurse, User


class LoginRegister(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class NurseRegister(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('Name', 'Contact_No', 'Email', 'Address', 'Hospital')

        def clean_phone(self):
            Contact_No = self.cleaned_data.get("Contact_No")
            z = PhoneNumberField.parse(Contact_No, "IN")
            if not PhoneNumberField.is_valid_number(z):
                raise forms.validationError("Number not in SG format")
            return Contact_No


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ('Name', 'Contact_No', 'Address', 'Child_Name', 'Child_Age', 'Child_Gender')

        def clean_phone(self):
            Contact_No = self.cleaned_data.get("Contact_No")
            z = PhoneNumberField.parse(Contact_No, "IN")
            if not PhoneNumberField.is_valid_number(z):
                raise forms.validationError("Number not in SG format")
            return Contact_No


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('Name', 'Place', 'Contact_No', 'Email')

        def clean_phone(self):
            Contact_No = self.cleaned_data.get("Contact_No")
            z = PhoneNumberField.parse(Contact_No, "IN")
            if not PhoneNumberField.is_valid_number(z):
                raise forms.validationError("Number not in SG format")
            return Contact_No


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('Vaccine_Name', 'Vaccine_Type', 'Description', 'Approval_Status')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('User', 'Schedule', 'Status', 'Vaccine_Name', 'Vaccinated')


class ReportForm(forms.ModelForm):
    class Meta:
        model = ReportCard
        fields = ('Vaccine', 'Patient')


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('Subject', 'Complaint', 'Date')


class VaccinationScheduleForm(forms.ModelForm):
    class Meta:
        model = VaccinationSchedule
        fields = ('Hospital', 'Date', 'Start_Time', 'End_Time')
