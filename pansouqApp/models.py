from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
import os
from jalali_date.admin import AdminJalaliDateWidget

User = get_user_model()


class Pansouq(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='عنوان پن سوق')
    description = models.CharField(max_length=100, blank=False, null=False, verbose_name='شرح مختصر')
    running = models.BooleanField(default=True, verbose_name='در حال اجرا')

    def __str__(self):
        return self.title

    def get_souqs(self):
        return Souq.objects.filter(related_pansouq=self)

    def get_teams(self):
        return Team.objects.filter(related_pansouq=self)


class Souq(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='عنوان رقابت')
    related_pansouq = models.ForeignKey(Pansouq, on_delete=models.CASCADE, verbose_name='پن سوق مربوطه')
    start_date = jmodels.jDateTimeField(verbose_name='زمان شروع')
    end_date = jmodels.jDateTimeField(verbose_name='زمان پایان')
    running = models.BooleanField(verbose_name='در حال اجرا')

    class Meta:
        ordering = ('start_date', 'title')

    def __str__(self):
        return self.title

    def get_challenges(self):
        return Challenge.objects.filter(related_souq=self)


def challenge_upload_path(instance, filename):
    return os.path.join("pansouq-challenges", "%d" % instance.related_souq.id, "%s" % instance.creator.username,
                        filename)


class Challenge(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان چالش')
    related_souq = models.ForeignKey(Souq, on_delete=models.CASCADE, verbose_name='رقابت مربوطه')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='طراح')
    file = models.FileField(upload_to=challenge_upload_path, blank=True)

    class Meta:
        ordering = ('related_souq', 'title',)

    def __str__(self):
        return self.title

    def get_participants(self):
        return Participant.objects.filter(challenging_in=self)


# class ChallengeMember(models.Model):

class Team(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام تیم')
    related_pansouq = models.ForeignKey(Pansouq, on_delete=models.CASCADE, verbose_name='رقابت مربوطه')
    score = models.FloatField(default=0, verbose_name='امتیاز کل')

    class Meta:
        ordering = ('related_pansouq', '-score', 'title')

    def __str__(self):
        return self.title

    def add_score(self, point):
        self.score = self.score + point

    def get_members(self):
        return Participant.objects.filter(team=self)


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='تیم مربوطه')
    challenging_in = models.ForeignKey(Challenge, on_delete=models.CASCADE, verbose_name='در حال رقابت')

    class Meta:
        ordering = ('team', 'challenging_in')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Transaction(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name='شرکت کننده')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, verbose_name='چالش مربوطه')
    points = models.FloatField(verbose_name='امتیاز کسب شده')
    alpha_correctness = models.FloatField(verbose_name='نسبت درستی پاسخ',
                                          help_text='یک ضریب بین ۰ تا ۱ در نمره‌ی کسب شده تاثیر مستقیم خواهد داشت')
    beta_ranking = models.FloatField(verbose_name='درصد جبران گذشته',
                                     help_text='تیم‌هایی که در جدول امتیازات پایین تر هستند، فرصت جبران بیشتری دارند')
    time_received = jmodels.jDateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('time_received',)

    def __str__(self):
        return str(self.participant) + ': ' + str(self.challenge) + ', ' + str(
            self.points * self.alpha_correctness + self.beta_ranking)

    def save(self, *args, **kwargs):
        t = self.participant.team
        t.add_score(self.points * self.alpha_correctness + self.beta_ranking)
        t.save()
        super().save(*args, **kwargs)
