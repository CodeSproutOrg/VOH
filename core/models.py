import datetime
from django.db import models


class Post(models.Model):

    """ Model of post """

    title = models.CharField(max_length=20)
    post = models.TextField(null=False)
    time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return f'Post {self.title}'


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


class UserPost(models.Model):

    """ Model of users post """

    name = models.CharField(max_length=20)
    post = models.TextField(null=False)

    class Meta:
        verbose_name = 'User Post'
        verbose_name_plural = 'User Posts'

    def __str__(self):
        return f'Post of {self.name}'
