from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import models as tinymce_models

User = get_user_model()


class PreRegisteredStudent(models.Model):
    #     مشخصات فردی
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    ss = models.IntegerField()
    ss_id = models.IntegerField()
    ss_numerical = models.IntegerField()
    ss_alphabetical = models.CharField(max_length=5)
    father_first_name = models.CharField(max_length=30)
    export_place = models.CharField(max_length=30)
    melli_code = models.IntegerField()
    birth_date = models.DateTimeField()
    birth_place_state = models.CharField(max_length=30)
    birth_place_town = models.CharField(max_length=30)
    birth_place_city = models.CharField(max_length=30)
    religion = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    physical_situation = models.CharField(
        max_length=30,
        choices=[
            ('سالم', 'سالم'),
            ('دارای معلولیت', 'دارای معلولیت')],
        default='سالم')
    left_handed = models.CharField(
        max_length=30,
        choices=[
            ('بلی', 'بلی'),
            ('خیر', 'خیر')],
        default='خیر')
    #     مشخصات خانوادگی
    father_edu = models.CharField(max_length=30)
    father_job = models.CharField(max_length=50)
    father_job_place = models.CharField(max_length=50)
    father_job_phone = models.CharField(max_length=11)
    mother_edu = models.CharField(max_length=30)
    mother_job = models.CharField(max_length=50)
    mother_job_place = models.CharField(max_length=50)
    mother_job_phone = models.CharField(max_length=11)
    home_location = models.TextField(max_length=200)
    home_phone = models.CharField(max_length=11)
    home_situation = models.CharField(
        max_length=30,
        choices=[
            ('اجاره ای', 'اجاره ای'),
            ('شخصی', 'شخصی'),
            ('سازمانی', 'سازمانی'),
            ('سایر', 'سایر')],
        default='اجاره ای')
    father_mail = models.EmailField(max_length=50)
    father_phone = models.CharField(max_length=11)
    mother_mail = models.EmailField(max_length=50)
    mother_phone = models.CharField(max_length=11)
    homemate = models.CharField(
        max_length=30,
        choices=[
            ('پدر و مادر', 'پدر و مادر'),
            ('پدر و مادرخوانده', 'پدر و مادرخوانده'),
            ('مادر و پدرخوانده', 'مادر و پدرخوانده'),
            ('پدر', 'پدر'),
            ('مادر', 'مادر'),
            ('مادربزرگ و یا پدربزرگ', 'مادربزرگ و یا پدربزرگ'),
            ('سایر بستگان', 'سایر بستگان')],
        default='پدر و مادر')
    student_own_place = models.CharField(
        max_length=30,
        choices=[
            ('خوابگاه دانش آموزی', 'خوابگاه دانش آموزی'),
            ('مسکن اجاره ای', 'مسکن اجاره ای'),
            ('منزل بستگان', 'منزل بستگان'),
        ])
    this_child_counter = models.IntegerField()
    family_members_counter = models.IntegerField()
    student_have_reading_room = models.BooleanField(
        choices=[
            (True, 'بلی'),
            (False, 'خیر')],
    )
    student_mail = models.EmailField(max_length=50)
    student_phone = models.CharField(max_length=11)
    #     وضعیت سال تحصیلی قبل
    last_year_edu = models.CharField(
        max_length=45,
        choices=[
            ('سال گذشته در پایه نهم تحصیل می کردم', 'سال گذشته در پایه نهم تحصیل می کردم'),
            ('سال گذشته در پایه دهم مردود شدم', 'سال گذشته در پایه دهم مردود شدم'),
            ('سال گذشته در نظام ترمی واحدی تحصیل کردم', 'سال گذشته در نظام ترمی واحدی تحصیل کردم'),
            ('سال گذشته از پایه دهم ترک تحصیل کردم', 'سال گذشته از پایه دهم ترک تحصیل کردم'),
            ('سال گذشته در هیچ واحد آموزشی تحصیل نکردم', 'سال گذشته در هیچ واحد آموزشی تحصیل نکردم'),
            ('سال گذشته در پایه دهم قبول شده ام', 'سال گذشته در پایه دهم قبول شده ام'),
            ('سال گذشته در پایه یازدهم تحصیل کرده ام', 'سال گذشته در پایه یازدهم تحصیل کرده ام'),
            ('سال گذشته در مدرسه بزرگسالان تحصیل کرده ام', 'سال گذشته در مدرسه بزرگسالان تحصیل کرده ام')
        ],
        default='سال گذشته در پایه نهم تحصیل می کردم'
    )
    field_of_study = models.CharField(
        max_length=20,
        choices=[
            ('ریاضی', 'ریاضی'),
            ('تجربی', 'تجربی')]
    )
    grade_at_9th = models.FloatField()
    last_year_school_name = models.CharField(max_length=30)
    last_year_school_code = models.IntegerField(
        help_text='کد و نام مدرسه ی قبلی از روی کارنامه ی رایانه ای ثبت شود')
    # ویژه دانش آموزان ایثارگر و شاهد
    shahed_in_all_schools = models.CharField(
        max_length=30,
        choices=[
            ('فرزند شهید', 'فرزند شهید'),
            ('فرزند مفقود الاثر', 'فرزند مفقود الاثر'),
            ('فرزند جانباز بالای ۷۰درصد', 'فرزند جانباز بالای ۷۰درصد')],
        help_text='ارائه معرفی نامه از بنیاد شهید شهرستان یا اداره جانبازان ضروری است')
    exceptional_student = models.CharField(
        max_length=30,
        choices=[
            ('ناشنوا', 'ناشنوا'),
            ('نیمه شنوا', 'نیمه شنوا'),
            ('نابینا', 'نابینا'),
            ('نیمه بینا', 'نیمه بینا'),
            ('معلول جسمی/حرکتی', 'معلول جسمی/حرکتی')],
        help_text='برای دانش آموزان دارای معلولیت که در مدارس عادی تحصیل می کنند، ارائه ی معرفی نامه از اداره یا مدیریت استثنایی استان ضروریست')
    date_added = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profilePic', default="/profilePic/default.png")
    phone = models.CharField(max_length=30, blank=True)
    grade = models.CharField(choices=[('10', 'پایه ی دهم'),
                                      ('11', 'پایه ی یازدهم'),
                                      ('12', 'پایه ی دوازدهم')], max_length=2, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=50, default='دانش آموز')
    description = tinymce_models.HTMLField()

    CHOICE = [
        ('math', 'ریاضی'),
        ('phys', 'فیزیک'),
        ('chem', 'شیمی'),
        ('bio', 'زیست'),
        ('comp', 'کامپیوتر'),
        ('eng', 'زبان'),
        ('far', 'فارسی'),
        ('other', 'سایر'),
    ]
    group = models.CharField(max_length=8, choices=CHOICE, blank=True)
    mom_number = models.CharField(max_length=30, blank=True, null=True)
    dad_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (
            ("send_sms", "send_sms"),
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=False)
    subject = models.CharField(max_length=50, blank=True)
    body = models.TextField(max_length=500, blank=False)
    seen = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)
