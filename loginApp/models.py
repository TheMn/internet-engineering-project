from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import models as tinymce_models

User = get_user_model()


class PreRegisteredStudent(models.Model):
    #     مشخصات فردی
    student_first_name = models.CharField(max_length=30, verbose_name='نام')
    student_last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    student_picture = models.ImageField(upload_to='registerPic/', blank=True, verbose_name='عکس پرسنلی دانش آموز',
                                        help_text='حجم عکس شما نباید بیشتر از ۵۰۰کیلوبایت باشد')
    ss = models.IntegerField(verbose_name='شماره شناسنامه')
    ss_id = models.IntegerField(verbose_name='سریال ۶رقمی شناسنامه')
    ss_numerical = models.IntegerField(verbose_name='سری عددی شناسنامه')
    ss_alphabetical = models.CharField(max_length=5, verbose_name='سری حروفی شناسنامه')
    export_place = models.CharField(max_length=30, verbose_name='محل صدور', blank=True)
    melli_code = models.IntegerField(verbose_name='کد ملی')
    birth_date = models.DateTimeField(verbose_name='تاریخ تولد')
    birth_place_state = models.CharField(max_length=30, verbose_name='شهرستان محل تولد')
    birth_place_town = models.CharField(max_length=30, verbose_name='استان محل تولد')
    birth_place_city = models.CharField(max_length=30, verbose_name='شهر یا روستای محل تولد')
    religion = models.CharField(max_length=30, verbose_name='دین')
    nationality = models.CharField(max_length=30, verbose_name='ملیت')
    physical_situation = models.CharField(
        verbose_name='وضعیت جسمانی',
        max_length=30,
        choices=[
            ('سالم', 'سالم'),
            ('دارای معلولیت', 'دارای معلولیت')],
        default='سالم')
    left_handed = models.CharField(
        verbose_name='چپ دست هستید؟',
        max_length=30,
        choices=[
            ('بلی', 'بلی'),
            ('خیر', 'خیر')],
        default='خیر')
    #     مشخصات خانوادگی
    father_first_name = models.CharField(max_length=30, verbose_name='نام پدر')
    father_edu = models.CharField(max_length=30, verbose_name='تحصیلات پدر')
    father_job = models.CharField(max_length=50, verbose_name='شغل پدر')
    father_job_place = models.CharField(max_length=50, verbose_name='محل کار پدر')
    father_job_phone = models.CharField(max_length=11, verbose_name='تلفن محل کار پدر', blank=True)
    mother_edu = models.CharField(max_length=30, verbose_name='تحصیلات مادر')
    mother_job = models.CharField(max_length=50, verbose_name='شغل مادر')
    mother_job_place = models.CharField(max_length=50, verbose_name='محل کار مادر')
    mother_job_phone = models.CharField(max_length=11, verbose_name='تلفن محل کار مادر', blank=True)
    home_location = models.TextField(max_length=200, verbose_name='آدرس منزل')
    home_phone = models.CharField(max_length=11, verbose_name='تلفن منزل')
    home_situation = models.CharField(
        verbose_name='وضعیت مسکن خانواده',
        max_length=30,
        choices=[
            ('اجاره ای', 'اجاره ای'),
            ('شخصی', 'شخصی'),
            ('سازمانی', 'سازمانی'),
            ('سایر', 'سایر')],
        default='اجاره ای')
    father_mail = models.EmailField(max_length=50, verbose_name='ایمیل پدر', blank=True)
    father_phone = models.CharField(max_length=11, verbose_name='شماره موبایل پدر')
    mother_mail = models.EmailField(max_length=50, verbose_name='ایمیل مادر', blank=True)
    mother_phone = models.CharField(max_length=11, verbose_name='شماره موبایل مادر')
    homemate = models.CharField(
        verbose_name='در خانواده با چه کسانی زندگی می کنید؟',
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
        verbose_name='وضعیت مسکن دانش آموز در صورتی که برای تحصیل دور از خانواده زندگی می کند، چگونه است؟',
        max_length=30,
        choices=[
            ('خوابگاه دانش آموزی', 'خوابگاه دانش آموزی'),
            ('مسکن اجاره ای', 'مسکن اجاره ای'),
            ('منزل بستگان', 'منزل بستگان'),
        ])
    this_child_counter = models.IntegerField(verbose_name='دانش آموز چندمین فرزند خانواده است؟')
    family_members_counter = models.IntegerField(verbose_name='تعداد افراد خانواده')
    student_have_reading_room = models.BooleanField(
        verbose_name='دانش آموز اتاق مستقل برای مطالعه دارد؟',
        choices=[
            (True, 'بلی'),
            (False, 'خیر')],
    )
    student_mail = models.EmailField(max_length=50, verbose_name='ایمیل دانش آموز')
    student_phone = models.CharField(max_length=11, verbose_name='شماره موبایل دانش آموز')
    #     وضعیت سال تحصیلی قبل
    last_year_edu = models.CharField(
        verbose_name='وضعیت تحصیلی سال قبل',
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
        verbose_name='رشته ی تحصیلی مورد علاقه',
        max_length=20,
        choices=[
            ('ریاضی', 'ریاضی'),
            ('تجربی', 'تجربی')]
    )
    field_of_olympiad = models.CharField(
        verbose_name='زمینه ی مورد علاقه در المپیاد های علمی دانش آموزی',
        max_length=20,
        choices=[
            ('ریاضی', 'ریاضی'),
            ('فیزیک', 'فیزیک'),
            ('شیمی', 'شیمی'),
            ('نجوم', 'نجوم'),
            ('کامپیوتر', 'کامپیوتر'),
            ('زیست', 'زیست')],
        blank=True
    )
    field_of_pajohesh = models.CharField(
        verbose_name='زمینه ی مورد علاقه برای فعالیت های پژوهشی',
        max_length=20,
        choices=[
            ('کامپیوتر', 'کامپیوتر'),
            ('رباتیک', 'رباتیک'),
            ('زیست', 'زیست'),
            ('شیمی', 'شیمی'),
            ('هنر و معماری', 'هنر و معماری')],
        blank=True
    )
    field_of_weakness = models.CharField(
        verbose_name='اگر در درسی از دروس پایه ضعف خاصی دارید، ذکر کنید',
        max_length=50,
        blank=True
    )
    grade_at_9th = models.FloatField(verbose_name='معدل کل پایه نهم')
    last_year_school_name = models.CharField(max_length=30, verbose_name='نام مدرسه ی قبلی')
    last_year_school_code = models.IntegerField(
        verbose_name='کد مدرسه ی قبلی',
        help_text='کد و نام مدرسه ی قبلی از روی کارنامه ی رایانه ای ثبت شود', blank=True)
    # ویژه دانش آموزان ایثارگر و شاهد
    shahed_in_all_schools = models.CharField(
        verbose_name='ویژه ی ثبت نام شاهد',
        max_length=30,
        choices=[
            ('فرزند شهید', 'فرزند شهید'),
            ('فرزند مفقود الاثر', 'فرزند مفقود الاثر'),
            ('فرزند جانباز بالای ۷۰درصد', 'فرزند جانباز بالای ۷۰درصد')],
        help_text='ارائه معرفی نامه از بنیاد شهید شهرستان یا اداره جانبازان ضروری است',
        blank=True)
    exceptional_student = models.CharField(
        verbose_name='ویژه ی ثبت نام استثنایی',
        max_length=30,
        choices=[
            ('ناشنوا', 'ناشنوا'),
            ('نیمه شنوا', 'نیمه شنوا'),
            ('نابینا', 'نابینا'),
            ('نیمه بینا', 'نیمه بینا'),
            ('معلول جسمی/حرکتی', 'معلول جسمی/حرکتی')],
        help_text='برای دانش آموزان دارای معلولیت که در مدارس عادی تحصیل می کنند، ارائه ی معرفی نامه از اداره یا مدیریت استثنایی استان ضروریست',
        blank=True)
    extra_note = models.CharField(
        verbose_name='اگر ملاحظات خاصی وجود دارد که باید به اطلاع مدرسه و مشاورین برسد، ذکر کنید', blank=True,
        max_length=100)
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
