from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import models as tinymce_models

User = get_user_model()


class PreRegisteredStudent(models.Model):
    #     مشخصات فردی
    student_first_name = models.CharField(blank=True, null=True, max_length=30, verbose_name='نام*', )
    student_last_name = models.CharField(blank=True, null=True, max_length=30, verbose_name='نام خانوادگی*')
    student_picture = models.ImageField(blank=True, null=True, upload_to='registerPic/',
                                        verbose_name='عکس پرسنلی دانش آموز',
                                        help_text='حجم عکس شما نباید بیشتر از ۵۰۰کیلوبایت باشد')
    ss = models.CharField(max_length=10, blank=True, null=True, verbose_name='شماره شناسنامه*')
    ss_id = models.CharField(max_length=6, blank=True, null=True, verbose_name='سریال ۶رقمی ش.*')
    ss_numerical = models.CharField(max_length=2, blank=True, null=True, verbose_name='سری عددی ش.*')
    ss_alphabetical = models.CharField(blank=True, null=True, max_length=5, verbose_name='سری حروفی ش.*')
    export_place = models.CharField(blank=True, null=True, max_length=30, verbose_name='محل صدور')
    melli_code = models.CharField(max_length=10, blank=True, null=True, verbose_name='کد ملی*')
    birthday_day_choices = [(str(i), str(i)) for i in range(1, 32)]
    birth_day = models.CharField(blank=True, null=True, verbose_name='روز تولد', max_length=2,
                                 choices=birthday_day_choices,
                                 default='1')
    birthday_month_choices = [
        ('1', 'فروردین'),
        ('2', 'اردیبهشت'),
        ('3', 'خرداد'),
        ('4', 'تیر'),
        ('5', 'مرداد'),
        ('6', 'شهریور'),
        ('7', 'مهر'),
        ('8', 'آبان'),
        ('9', 'آذر'),
        ('10', 'دی'),
        ('11', 'بهمن'),
        ('12', 'اسفند'),
    ]
    birth_month = models.CharField(blank=True, null=True, verbose_name='ماه تولد', max_length=2,
                                   choices=birthday_month_choices,
                                   default='1')
    birthday_year_choices = [(str(i), str(i)) for i in range(1380, 1389)]
    birth_year = models.CharField(blank=True, null=True, verbose_name='سال تولد', max_length=4,
                                  choices=birthday_year_choices,
                                  default=1380)
    # birth_date = models.DateTimeField(verbose_name='تاریخ تولد')
    birth_place_state = models.CharField(blank=True, null=True, max_length=30, verbose_name='شهرستان محل تولد*')
    birth_place_town = models.CharField(blank=True, null=True, max_length=30, verbose_name='استان محل تولد*')
    birth_place_city = models.CharField(blank=True, null=True, max_length=30, verbose_name='شهر یا روستای محل تولد*')
    religion = models.CharField(blank=True, null=True, max_length=30, verbose_name='دین*')
    nationality = models.CharField(blank=True, null=True, max_length=30, verbose_name='ملیت*')
    physical_situation = models.CharField(blank=True, null=True,
                                          verbose_name='وضعیت جسمانی',
                                          max_length=30,
                                          choices=[
                                              ('سالم', 'سالم'),
                                              ('دارای معلولیت', 'دارای معلولیت')],
                                          default='سالم')
    left_handed = models.CharField(blank=True, null=True,
                                   verbose_name='چپ دست هستید؟',
                                   max_length=30,
                                   choices=[
                                       ('بلی', 'بلی'),
                                       ('خیر', 'خیر')],
                                   default='خیر')
    #     مشخصات خانوادگی
    father_first_name = models.CharField(blank=True, null=True, max_length=30, verbose_name='نام پدر*')
    father_edu = models.CharField(blank=True, null=True, max_length=30, verbose_name='تحصیلات پدر*')
    father_job = models.CharField(blank=True, null=True, max_length=50, verbose_name='شغل پدر*')
    father_job_place = models.TextField(blank=True, null=True, max_length=200, verbose_name='آدرس محل کار پدر*')
    father_job_phone = models.CharField(max_length=11, verbose_name='تلفن محل کار پدر', blank=True, null=True,
                                        help_text="مثال: ۰۲۱۸۸۳۲۹۱۸۲")
    mother_edu = models.CharField(blank=True, null=True, max_length=30, verbose_name='تحصیلات مادر*')
    mother_job = models.CharField(blank=True, null=True, max_length=50, verbose_name='شغل مادر*')
    mother_job_place = models.TextField(blank=True, null=True, max_length=50, verbose_name='آدرس محل کار مادر')
    mother_job_phone = models.CharField(blank=True, null=True, max_length=11, verbose_name='تلفن محل کار مادر',
                                        help_text="مثال: ۰۲۱۸۸۳۲۹۱۸۲")
    home_location = models.TextField(blank=True, null=True, max_length=200, verbose_name='آدرس منزل*')
    home_phone = models.CharField(blank=True, null=True, max_length=11, verbose_name='تلفن منزل*',
                                  help_text="مثال: ۰۲۱۸۸۳۲۹۱۸۲")
    home_situation = models.CharField(blank=True, null=True,
                                      verbose_name='وضعیت مسکن خانواده',
                                      max_length=30,
                                      choices=[
                                          ('اجاره ای', 'اجاره ای'),
                                          ('شخصی', 'شخصی'),
                                          ('سازمانی', 'سازمانی'),
                                          ('سایر', 'سایر')],
                                      default='اجاره ای')
    father_mail = models.EmailField(max_length=50, verbose_name='ایمیل پدر', blank=True, null=True)
    father_phone = models.CharField(blank=True, null=True, max_length=11, verbose_name='شماره موبایل پدر*',
                                    help_text="مثال: ۰۹۱۲۳۴۵۶۷۸۹")
    mother_mail = models.EmailField(blank=True, null=True, max_length=50, verbose_name='ایمیل مادر')
    mother_phone = models.CharField(blank=True, null=True, max_length=11, verbose_name='شماره موبایل مادر*',
                                    help_text="مثال: ۰۹۱۲۳۴۵۶۷۸۹")
    homemate = models.CharField(blank=True, null=True,
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
    student_own_place = models.CharField(blank=True, null=True,
                                         verbose_name='وضعیت مسکن دانش آموز در صورتی که برای تحصیل دور از خانواده زندگی می کند، چگونه است؟',
                                         max_length=30,
                                         choices=[
                                             ('خوابگاه دانش آموزی', 'خوابگاه دانش آموزی'),
                                             ('مسکن اجاره ای', 'مسکن اجاره ای'),
                                             ('منزل بستگان', 'منزل بستگان'),
                                         ])
    this_child_counter = models.IntegerField(blank=True, null=True, verbose_name='چندمین فرزند خانواده هستید؟*')
    family_members_counter = models.IntegerField(blank=True, null=True, verbose_name='تعداد اعضای خانواده*')
    student_have_reading_room = models.BooleanField(blank=True, null=True,
                                                    verbose_name='دانش آموز اتاق مستقل برای مطالعه دارد؟',
                                                    choices=[
                                                        (True, 'بلی'),
                                                        (False, 'خیر')],
                                                    )
    student_mail = models.EmailField(blank=True, null=True, max_length=50, verbose_name='ایمیل دانش آموز*')
    student_phone = models.CharField(blank=True, null=True, max_length=11, verbose_name='شماره موبایل دانش آموز*',
                                     help_text="مثال: ۰۹۱۲۳۴۵۶۷۸۹")
    #     وضعیت سال تحصیلی قبل
    last_year_edu = models.CharField(blank=True, null=True,
                                     verbose_name='وضعیت تحصیلی سال قبل',
                                     max_length=45,
                                     choices=[
                                         ('سال گذشته در پایه نهم تحصیل می کردم', 'سال گذشته در پایه نهم تحصیل می کردم'),
                                         ('سال گذشته در پایه دهم مردود شدم', 'سال گذشته در پایه دهم مردود شدم'),
                                         ('سال گذشته در نظام ترمی واحدی تحصیل کردم',
                                          'سال گذشته در نظام ترمی واحدی تحصیل کردم'),
                                         ('سال گذشته از پایه دهم ترک تحصیل کردم',
                                          'سال گذشته از پایه دهم ترک تحصیل کردم'),
                                         ('سال گذشته در هیچ واحد آموزشی تحصیل نکردم',
                                          'سال گذشته در هیچ واحد آموزشی تحصیل نکردم'),
                                         ('سال گذشته در پایه دهم قبول شده ام', 'سال گذشته در پایه دهم قبول شده ام'),
                                         ('سال گذشته در پایه یازدهم تحصیل کرده ام',
                                          'سال گذشته در پایه یازدهم تحصیل کرده ام'),
                                         ('سال گذشته در مدرسه بزرگسالان تحصیل کرده ام',
                                          'سال گذشته در مدرسه بزرگسالان تحصیل کرده ام')
                                     ],
                                     default='سال گذشته در پایه نهم تحصیل می کردم'
                                     )
    field_of_study = models.CharField(blank=True, null=True,
                                      verbose_name='رشته ی تحصیلی مورد علاقه*',
                                      max_length=20,
                                      choices=[
                                          ('ریاضی', 'ریاضی'),
                                          ('تجربی', 'تجربی')]
                                      )
    field_of_olympiad = models.CharField(blank=True, null=True,
                                         verbose_name='زمینه ی مورد علاقه در المپیاد های علمی',
                                         max_length=20,
                                         choices=[
                                             ('ریاضی', 'ریاضی'),
                                             ('فیزیک', 'فیزیک'),
                                             ('شیمی', 'شیمی'),
                                             ('نجوم', 'نجوم'),
                                             ('کامپیوتر', 'کامپیوتر'),
                                             ('زیست', 'زیست')]
                                         )
    field_of_pajohesh = models.CharField(blank=True, null=True,
                                         verbose_name='زمینه ی مورد علاقه برای فعالیت های پژوهشی',
                                         max_length=20,
                                         choices=[
                                             ('کامپیوتر', 'کامپیوتر'),
                                             ('رباتیک', 'رباتیک'),
                                             ('زیست', 'زیست'),
                                             ('شیمی', 'شیمی'),
                                             ('هنر و معماری', 'هنر و معماری')]
                                         )
    field_of_weakness = models.CharField(blank=True, null=True,
                                         verbose_name='اگر در درسی از دروس پایه ضعف خاصی دارید، ذکر کنید',
                                         max_length=50
                                         )
    grade_at_9th = models.FloatField(blank=True, null=True, verbose_name='معدل کل پایه نهم*')
    last_year_school_name = models.CharField(blank=True, null=True, max_length=30, verbose_name='نام مدرسه ی قبلی*',
                                             help_text='کد و نام مدرسه ی قبلی از روی کارنامه ی رایانه ای ثبت شود')
    last_year_school_code = models.CharField(max_length=10, blank=True, null=True,
                                             verbose_name='کد مدرسه ی قبلی')
    # ویژه دانش آموزان ایثارگر و شاهد
    shahed_in_all_schools = models.CharField(blank=True, null=True,
                                             verbose_name='ویژه ی ثبت نام شاهد',
                                             max_length=30,
                                             choices=[
                                                 ('فرزند شهید', 'فرزند شهید'),
                                                 ('فرزند مفقود الاثر', 'فرزند مفقود الاثر'),
                                                 ('فرزند جانباز بالای ۷۰درصد', 'فرزند جانباز بالای ۷۰درصد')],
                                             help_text='ارائه معرفی نامه از بنیاد شهید شهرستان یا اداره جانبازان ضروریست',
                                             )
    exceptional_student = models.CharField(
        verbose_name='ویژه ی ثبت نام استثنایی',
        max_length=30,
        choices=[
            ('ناشنوا', 'ناشنوا'),
            ('نیمه شنوا', 'نیمه شنوا'),
            ('نابینا', 'نابینا'),
            ('نیمه بینا', 'نیمه بینا'),
            ('معلول جسمی/حرکتی', 'معلول جسمی/حرکتی')],
        help_text='ارائه معرفی نامه از اداره یا مدیریت استثنایی استان ضروریست',
        blank=True, null=True)
    extra_note = models.TextField(
        verbose_name='اگر ملاحظات خاصی وجود دارد که باید به اطلاع مدرسه و مشاورین برسد، ذکر کنید', blank=True,
        null=True,
        max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profilePic', default="/profilePic/default.png")
    phone = models.CharField(max_length=30, blank=True, null=True)
    grade = models.CharField(choices=[('10', 'پایه ی دهم'),
                                      ('11', 'پایه ی یازدهم'),
                                      ('12', 'پایه ی دوازدهم')], max_length=2, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=50, default='دانش آموز')
    description = models.CharField(max_length=150, blank=True)
    financial_problem = models.BooleanField(default=False)

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
    group = models.CharField(max_length=8, choices=CHOICE, blank=True, null=True)
    mom_number = models.CharField(max_length=30, blank=True, null=True)
    dad_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (
            ("send_sms", "send_sms"),
            ('check_classes', 'check_classes')
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
