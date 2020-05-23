from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()

# Create your models here.


def upload_location(instance, filename):
    return '%s/%s'%(instance.id, filename)
class MockTest(models.Model):
    name         = models.CharField(max_length=100)
    slug         = models.SlugField(unique=True)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    bio          = models.TextField(null= True, blank=True)
    is_free      = models.BooleanField()
    fee          = models.DecimalField(max_digits=10, decimal_places=2) 
    time_created = models.DateTimeField(auto_now=False,auto_now_add=True)
    time_start   = models.DateField(auto_now=False, auto_now_add=False, default='')
    speak_date   = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    registerations = models.ManyToManyField(User, blank=True, null=True, related_name='registerations')


    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("teacher:mock_view", kwargs={"slug": self.slug})

    def total_registers(self):
        return self.registerations.count()
    
    def is_registered(self,request):
        if self.registerations.filter(request.user.id).exists():
            return True

class Listening(models.Model):
    mocktest        =models.OneToOneField(MockTest, on_delete=models.CASCADE)
    audio           = models.FileField(upload_to = upload_location,)
    pdf             = models.FileField(upload_to = upload_location,)
    section1        = RichTextUploadingField()
    section2        = RichTextUploadingField()
    section3        = RichTextUploadingField()
    section4        = RichTextUploadingField()

class Reading(models.Model):
    mocktest        =models.OneToOneField(MockTest, on_delete=models.CASCADE)
    pdf             = models.FileField(upload_to = upload_location,)
    passage1        = RichTextUploadingField()
    passage2        = RichTextUploadingField()
    passage3        = RichTextUploadingField()

class Writing(models.Model):
    mocktest        =models.OneToOneField(MockTest, on_delete=models.CASCADE)
    pdf             = models.FileField(upload_to = upload_location,)
    task1           = RichTextUploadingField()
    task2           = RichTextUploadingField()
    image           = models.ImageField(upload_to = upload_location,null=True, blank=True,)

class Speaking(models.Model):
    mocktest        =models.OneToOneField(MockTest, on_delete=models.CASCADE)
    pdf             = models.FileField(upload_to = upload_location,)
    part1           = RichTextUploadingField()
    part2           = RichTextUploadingField()
    part3           = RichTextUploadingField()


class AnswerListening(models.Model):
    mocktest = models.OneToOneField(MockTest, on_delete=models.CASCADE)
    a1 = models.CharField(max_length=100)
    a2 = models.CharField(max_length=100)
    a3 = models.CharField(max_length=100)
    a4 = models.CharField(max_length=100)
    a5 = models.CharField(max_length=100)
    a6 = models.CharField(max_length=100)
    a7 = models.CharField(max_length=100)
    a8 = models.CharField(max_length=100)
    a9 = models.CharField(max_length=100)
    a10 = models.CharField(max_length=100)
    a11 = models.CharField(max_length=100)
    a12 = models.CharField(max_length=100)
    a13 = models.CharField(max_length=100)
    a14 = models.CharField(max_length=100)
    a15 = models.CharField(max_length=100)
    a16 = models.CharField(max_length=100)
    a17 = models.CharField(max_length=100)
    a18 = models.CharField(max_length=100)
    a19 = models.CharField(max_length=100)
    a20 = models.CharField(max_length=100)
    a21 = models.CharField(max_length=100)
    a22 = models.CharField(max_length=100)
    a23 = models.CharField(max_length=100)
    a24 = models.CharField(max_length=100)
    a25 = models.CharField(max_length=100)
    a26 = models.CharField(max_length=100)
    a27 = models.CharField(max_length=100)
    a28 = models.CharField(max_length=100)
    a29 = models.CharField(max_length=100)
    a30 = models.CharField(max_length=100)
    a31 = models.CharField(max_length=100)
    a32 = models.CharField(max_length=100)
    a33 = models.CharField(max_length=100)
    a34 = models.CharField(max_length=100)
    a35 = models.CharField(max_length=100)
    a36 = models.CharField(max_length=100)
    a37 = models.CharField(max_length=100)
    a38 = models.CharField(max_length=100)
    a39 = models.CharField(max_length=100)
    a40 = models.CharField(max_length=100)

class AnswerReading(models.Model):
    mocktest = models.OneToOneField(MockTest, on_delete=models.CASCADE)
    a1 = models.CharField(max_length=100)
    a2 = models.CharField(max_length=100)
    a3 = models.CharField(max_length=100)
    a4 = models.CharField(max_length=100)
    a5 = models.CharField(max_length=100)
    a6 = models.CharField(max_length=100)
    a7 = models.CharField(max_length=100)
    a8 = models.CharField(max_length=100)
    a9 = models.CharField(max_length=100)
    a10 = models.CharField(max_length=100)
    a11 = models.CharField(max_length=100)
    a12 = models.CharField(max_length=100)
    a13 = models.CharField(max_length=100)
    a14 = models.CharField(max_length=100)
    a15 = models.CharField(max_length=100)
    a16 = models.CharField(max_length=100)
    a17 = models.CharField(max_length=100)
    a18 = models.CharField(max_length=100)
    a19 = models.CharField(max_length=100)
    a20 = models.CharField(max_length=100)
    a21 = models.CharField(max_length=100)
    a22 = models.CharField(max_length=100)
    a23 = models.CharField(max_length=100)
    a24 = models.CharField(max_length=100)
    a25 = models.CharField(max_length=100)
    a26 = models.CharField(max_length=100)
    a27 = models.CharField(max_length=100)
    a28 = models.CharField(max_length=100)
    a29 = models.CharField(max_length=100)
    a30 = models.CharField(max_length=100)
    a31 = models.CharField(max_length=100)
    a32 = models.CharField(max_length=100)
    a33 = models.CharField(max_length=100)
    a34 = models.CharField(max_length=100)
    a35 = models.CharField(max_length=100)
    a36 = models.CharField(max_length=100)
    a37 = models.CharField(max_length=100)
    a38 = models.CharField(max_length=100)
    a39 = models.CharField(max_length=100)
    a40 = models.CharField(max_length=100)

class AnswerWritingChecked(models.Model):
    mocktest = models.ForeignKey(MockTest, on_delete=models.CASCADE)  
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    band = models.PositiveIntegerField()
    fedback = models.TextField()  

class AnswerSpeakingChecked(models.Model):
    mocktest = models.ForeignKey(MockTest, on_delete=models.CASCADE)  
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    band = models.PositiveIntegerField()
    fedback = models.TextField()  

class AnswerReadingChecked(models.Model):
    mocktest = models.ForeignKey(MockTest, on_delete=models.CASCADE)  
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    band = models.PositiveIntegerField()
    correct = models.PositiveIntegerField(default=0)

class AnswerListeningChecked(models.Model):
    mocktest = models.ForeignKey(MockTest, on_delete=models.CASCADE)  
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    band = models.PositiveIntegerField()
    correct = models.PositiveIntegerField(default=0)