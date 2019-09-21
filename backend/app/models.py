from django.db import models


class NameModel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return f'{self.__class__.__name__} {self.name!r} (id={self.id!r})'


class Datasource(NameModel):
    pass


class Campaign(NameModel):
    pass


class DayStats(models.Model):
    date = models.DateField()
    datasource = models.ForeignKey(Datasource, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    clicks = models.IntegerField()
    impressions = models.IntegerField()

    class Meta:
        ordering = ['date', 'datasource', 'campaign']
        unique_together = ['date', 'datasource', 'campaign']

    def __str__(self):
        return f'{self.__class__.__name__} date={self.date!s}'
