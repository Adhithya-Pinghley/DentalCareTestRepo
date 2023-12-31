# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HealthcentreAppointment(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.TimeField()
    date = models.DateField()
    subject = models.CharField(max_length=2000)
    notes = models.TextField()
    doctorpres = models.ForeignKey('HealthcentreDoctor', models.DO_NOTHING, db_column='doctorPres_id')  # Field name made lowercase.
    patientpres = models.ForeignKey('HealthcentrePatient', models.DO_NOTHING, db_column='patientPres_id')  # Field name made lowercase.
    appointmentpatient = models.CharField(max_length=2000)
    appointmentdoctor = models.CharField(max_length=2000)
    appointmenttimestamp = models.DateTimeField(db_column='AppointmentTimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthCentre_appointment'


class HealthcentreDoctor(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    contactnumber = models.CharField(db_column='contactNumber', unique=True, max_length=10)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    specialization = models.CharField(max_length=100)
    passwordhash = models.CharField(db_column='passwordHash', max_length=64)  # Field name made lowercase.
    emailhash = models.CharField(db_column='emailHash', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthCentre_doctor'


class HealthcentreMedicine(models.Model):
    medicinename = models.CharField(db_column='MedicineName', max_length=200)  # Field name made lowercase.
    beforeafter = models.CharField(db_column='beforeAfter', max_length=200)  # Field name made lowercase.
    morning = models.CharField(db_column='Morning', max_length=200)  # Field name made lowercase.
    afternoon = models.CharField(db_column='Afternoon', max_length=200)  # Field name made lowercase.
    night = models.CharField(db_column='Night', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthCentre_medicine'


class HealthcentrePatient(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    contactnumber = models.CharField(db_column='contactNumber', max_length=10)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    passwordhash = models.CharField(db_column='passwordHash', max_length=64)  # Field name made lowercase.
    rollnumber = models.CharField(db_column='rollNumber', max_length=8)  # Field name made lowercase.
    emailhash = models.CharField(db_column='emailHash', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthCentre_patient'


class HealthcentrePrescription(models.Model):
    prescriptiontext = models.CharField(db_column='prescriptionText', max_length=2000)  # Field name made lowercase.
    doctor = models.ForeignKey(HealthcentreDoctor, models.DO_NOTHING)
    patient = models.ForeignKey(HealthcentrePatient, models.DO_NOTHING)
    timestamp = models.DateTimeField()
    isnew = models.BooleanField(db_column='isNew')  # Field name made lowercase.
    symptoms = models.CharField(max_length=2000)
    iscompleted = models.BooleanField(db_column='isCompleted')  # Field name made lowercase.
    prescribingdoctor = models.CharField(db_column='prescribingDoctor', max_length=2000)  # Field name made lowercase.
    prescribingpatient = models.CharField(db_column='prescribingPatient', max_length=2000)  # Field name made lowercase.
    noofdays = models.CharField(db_column='NoOfDays', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthCentre_prescription'


class HealthcentrePrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(HealthcentrePrescription, models.DO_NOTHING)
    medicine = models.ForeignKey(HealthcentreMedicine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'HealthCentre_prescription_medicine'
        unique_together = (('prescription', 'medicine'),)


class MedicalstoreMedicine(models.Model):
    name = models.CharField(unique=True, max_length=150)
    company = models.CharField(max_length=150)
    expirydate = models.DateField(db_column='expiryDate')  # Field name made lowercase.
    manufactureddate = models.DateField(db_column='manufacturedDate')  # Field name made lowercase.
    quantity = models.IntegerField()
    price = models.IntegerField()
    photoid = models.CharField(db_column='photoId', unique=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MedicalStore_medicine'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
