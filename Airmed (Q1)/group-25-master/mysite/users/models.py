from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    Gender = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class calorie_counter(models.Model):
    cal_amount = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


class weight_counter(models.Model):
    weight_amount = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


class exercise(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class cable_fly(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class inclined_db(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class bent_over_row(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


class bicep_curl(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class deadlift(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


class tricep_extension(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class pullup(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)


class skullcrushers(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class back_squat(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class lunge(models.Model):
    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class hip_thrust(models.Model):

    reps = models.PositiveIntegerField(default=0, blank=True)
    sets = models.PositiveIntegerField(default=0, blank=True)
    one_rep_max = models.PositiveIntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def datepublished(self):
        return self.date_posted.strftime('%B %d')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)