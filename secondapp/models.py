from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()

    def __str__(self):
        return self.name
    
class ArmyShop(models.Model):
    # def __str__(self):
    #     return self.name
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()
    class Meta:
        db_table = 'army_shop'
        managed = False