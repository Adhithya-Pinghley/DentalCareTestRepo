from django.db import models
from Cryptodome.Hash import SHA256
from codecs import encode,decode
from django.utils import timezone


class Doctor(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    contactNumber = models.CharField(unique = True, max_length = 10)
    email = models.EmailField(unique = True, max_length = 255)
    specialization = models.CharField(max_length = 100)
    passwordHash = models.CharField(max_length = 64)
    emailHash = models.CharField(max_length = 64)

    def __str__(self):
        return "Name : " + self.name + " Address : " + self.address + " Contact : " + self.contactNumber + " Email : " + self.email + " Specialization : " + self.specialization

class Patient(models.Model):
    name = models.CharField(unique = True, max_length = 30)
    address = models.CharField(max_length = 100)
    contactNumber = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 255)
    rollNumber = models.CharField(max_length = 8)
    passwordHash = models.CharField(max_length = 64)
    emailHash = models.CharField(max_length = 64)

    def __str__(self):
        return "Name : " + self.name + " Address : " + self.address + " Contact : " + self.contactNumber + " Email : " + self.email

class Medicine(models.Model):
    MedicineName = models.CharField(max_length= 200)
    beforeAfter = models.CharField(max_length= 200)
    Morning = models.CharField(max_length= 200)
    Afternoon = models.CharField(max_length= 200)
    Night   = models.CharField(max_length= 200)

    def __str__(self):
        return "\nMedicineName :" + str(self.MedicineName) + "\nBeforeAfter :" + str(self.beforeAfter) + "\nMorning :" + str(self.Morning) + "\nAfternoon :" + str(self.Afternoon) + "\nNight :" + str(self.Night) + "\n\n"


class Prescription(models.Model):
    prescriptionText = models.CharField(max_length = 2000, default = "")
    prescribingDoctor = models.CharField(max_length= 2000, default= "")
    prescribingPatient = models.CharField(max_length= 2000, default= "")
    doctor = models.ForeignKey(Doctor, related_name = "doctorRecords", on_delete = models.CASCADE)
    patient = models.ForeignKey(Patient, related_name = "patientRecords", on_delete = models.CASCADE)
    # beforeafter = models.CharField(max_length= 10)
    medicine    = models.ManyToManyField(to= Medicine)
    # MornAftNight = models.CharField(max_length=10)
    NoOfDays = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    isNew = models.BooleanField(default = True)
    isCompleted = models.BooleanField(default = False)
    symptoms = models.CharField(max_length = 2000)

    def __str__(self):
        return "\nDoctor :" + str(self.doctor) + "\n\nPatient :" + str(self.patient) + "\n\nPrescription : \n\n" + self.prescriptionText  + "\nNoOfDays :" + str(self.NoOfDays) + "\n\n" #+ "\nMedicine :" + str(self.medicine)

class Appointment(models.Model):
    # id = models.AutoField(primary_key=True)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    subject = models.CharField(max_length=2000)
    notes = models.TextField()
    doctorPres = models.ForeignKey(Doctor, related_name = "doctorPrescRecords", on_delete = models.CASCADE)
    patientPres = models.ForeignKey(Patient, related_name = "patientPrescRecords", on_delete = models.CASCADE)
    appointmentpatient = models.CharField(max_length=2000, default = "")
    appointmentdoctor  = models.CharField(max_length=2000, default= "")
    AppointmentTimeStamp = models.DateTimeField(auto_now_add = True)#auto_now_add = True 

    def __str__(self):
        return "\nDoctorId :" + str(self.doctorPres) + "\nPatientId :" + str(self.patientPres) + "\nDoctor :" + str(self.appointmentdoctor) + "\n\nPatient" + str(self.appointmentpatient) +"\n\nDate :"+ str(self.date) + "\n\nTime :" + str(self.time) + "\n\nSubject :" + str(self.subject) + "\n\nnotes :" + str(self.notes) + "\n\n"
    
def passwordHasher(userPassword):
    """Function to return the hash of the password using SHA-256. Input is the password of the user in string."""
    userPassword = userPassword
    SHA256Engine = SHA256.new()
    userPassword = userPassword.encode()
    SHA256Engine.update(userPassword)
    passwordHash = SHA256Engine.digest()
    passwordHash = encode(passwordHash, 'hex')
    passwordHash = decode(passwordHash, 'utf-8')
    return passwordHash


def emailHasher(userEmail):
    """Function to return the hash of the email using SHA-256. Input is the email of the user in string."""
    userEmail = userEmail
    SHA256Engine = SHA256.new()
    userEmail = userEmail.encode()
    SHA256Engine.update(userEmail)
    emailHash = SHA256Engine.digest()
    emailHash = encode(emailHash, 'hex')
    emailHash = decode(emailHash, 'utf-8')
    return emailHash
    
