from django.contrib import admin

# Register your models here.
from vaccineapp.models import Nurse, Hospital, User, Vaccine, VaccinationSchedule, Complaint, Appointment, ReportCard

admin.site.register(Nurse)
admin.site.register(Hospital)
admin.site.register(User)
admin.site.register(Vaccine)
admin.site.register(VaccinationSchedule)
admin.site.register(Complaint)
admin.site.register(Appointment)
admin.site.register(ReportCard)

