from django.db import models
from django.utils import timezone
import datetime


class Client(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    client_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='client_logos/', default = 'client_logos/none/no-logo.png')

    def __str__(self):
        return self.client_name


class Campaign(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    CPC = 'cpc'
    CPM = 'cpm'
    CPV = 'cpv'
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        name = str(self.client_name) + " - " + self.campaign_name
        return name


class Publisher(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    publisher_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='publisher_logos/', default = 'publisher_logos/none/no-logo.png')

    def __str__(self):
        return self.publisher_name


class Placement(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    CPC = 'cpc'
    CPM = 'cpm'
    CPV = 'cpv'
    UNIT_CHOICES = (
        (CPC, 'CPC'),
        (CPM, 'CPM'),
        (CPV, 'CPV'),
    )
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    publisher_name = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    unit_type = models.CharField(default='cpc', choices=UNIT_CHOICES, max_length=3)
    units = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)
    budget_spent = models.IntegerField(default=0)
    units_delivered = models.IntegerField(default=0)
    diff = models.BooleanField(default=False)

    def __str__(self):
        return str(self.publisher_name)

    def time_perecent(self):
        rest = self.end_date - datetime.date.today()
        total = self.end_date - self.start_date
        return "{:.2}".format(1-(rest.total_seconds()/total.total_seconds()))

    def days_left(self):
        days_rest = self.end_date - datetime.date.today()
        return days_rest.days

    def unit_cost(self):
        if(self.unit_type == "cpm"):
            return self.budget/(self.units/1000)
        else:
            return self.budget/self.units

    def unit_actual_cost(self):
        if(self.unit_type == "cpm"):
            return self.budget_spent/(self.units_delivered/1000)
        else:
            return self.budget_spent/self.units_delivered
