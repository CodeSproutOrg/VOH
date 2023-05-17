import datetime
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """ Model of post """

    title = models.CharField(max_length=50, verbose_name='Title of post')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    post = models.TextField(null=False, verbose_name='Text of post')
    time = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Time')

    class Meta:
        verbose_name = 'Post'

    def get_absolute_url(self):
        return reverse('blog', kwargs={'post_slug': self.slug })

    def __str__(self):
        return f'{self.title}'


class Link(models.Model):
    """ Model of link """

    Collaborative_Divorce_Resources = 'Collaborative Divorce Resources'
    Collaborative_CoParenting_Mediation_Resources = 'Collaborative Co-Parenting Mediation Resources'
    Assessments_and_Screeners = 'Assessments and Screeners'
    Consultation_and_Therapy_Services = 'Consultation and Therapy Services'
    CoParenting_Mediation_Program = 'Co-Parenting Mediation Program'

    LINKS_OPTIONS = [
        (Collaborative_Divorce_Resources, Collaborative_Divorce_Resources),
        (Collaborative_CoParenting_Mediation_Resources, Collaborative_CoParenting_Mediation_Resources),
        (Assessments_and_Screeners, Assessments_and_Screeners),
        (Consultation_and_Therapy_Services, Consultation_and_Therapy_Services),
        (CoParenting_Mediation_Program, CoParenting_Mediation_Program)
    ]

    title = models.CharField(max_length=50, choices=LINKS_OPTIONS, verbose_name='Title name')
    url_title = models.CharField(max_length=100, verbose_name='Link title')
    url = models.CharField(max_length=100, verbose_name='Url of link')

    class Meta:
        verbose_name = 'Link'

    def __str__(self):
        return f'Link {self.url_title}'

class VideoLink(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title of video')
    url = models.CharField(max_length=80, verbose_name='Link of video')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Video link'

    def get_absolute_url(self):
        return reverse('videos', kwargs={'video_slug': self.slug })

    def __str__(self):
        return self.title

class UserPost(models.Model):
    """ Model of users post """

    ABUSE_FROM_CPS_DCFS = [
        ('Substantiated', 'Substantiated abuse from CPS/DCFS'),
        ('Unsubstantiated', 'Unsubstantiated abuse from CPS/DCFS')
    ]
    CONFIRMED_PARENTAL_ALIENATION = [('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')]
    YES_NO = [('Yes', 'Yes'), ('No', 'No')]

    name = models.CharField(max_length=20, blank=True, verbose_name='Your Name')
    case = models.TextField(verbose_name='Your Case')
    abuse_from_CPS_DCFS = models.CharField(max_length=36, default='Substantiated abuse from CPS/DCFS',
                                           choices=ABUSE_FROM_CPS_DCFS, verbose_name='abuse from CPS/DCFS')
    parental_alienation = models.CharField(max_length=10, default='Yes', verbose_name='Parental Alienation Degree',
                                           choices=CONFIRMED_PARENTAL_ALIENATION)
    allegations = models.CharField(max_length=5, choices=YES_NO, default='No',
                                   verbose_name='Parental Alienation Allegations')
    falsified = models.CharField(max_length=5, choices=YES_NO, default='No',
                                 verbose_name='falsified of parental alienation')
    duration = models.TextField(verbose_name='duration')
    money = models.TextField(verbose_name='money')
    left_broken = models.TextField(verbose_name='Left / Broken')
    abuse_criteria = models.TextField(verbose_name='abuse criteria')
    result = models.TextField(verbose_name='result')

    class Meta:
        verbose_name = 'User Post'
        verbose_name_plural = 'User Posts'

    def __str__(self):
        return f'Post of {self.name}'


class File(models.Model):
    """ Model of file """

    name = models.CharField(max_length=255, verbose_name='Name of file')
    path = models.FileField(upload_to='', null=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.name
