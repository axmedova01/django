from django.db import models

class Fam(models.Model):
    id_fam = models.AutoField(primary_key=True)
    fam = models.CharField(max_length=50)

    def __str__(self):
        return self.fam

class Nam(models.Model):
    id_name = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Otchestvo(models.Model):
    id_otch = models.AutoField(primary_key=True)
    otch = models.CharField(max_length=100)
    def __str__(self):
        return self.otch

class Street(models.Model):
    id_street = models.AutoField(primary_key=True)
    street = models.CharField(max_length=150)
    def __str__(self):
        return self.street

class Main(models.Model):
    id = models.AutoField(primary_key=True)
    fam = models.ForeignKey(Fam, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(Nam, on_delete=models.CASCADE, null=True)
    otch = models.ForeignKey(Otchestvo, on_delete=models.CASCADE, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, null=True)
    bldn = models.CharField(max_length=15)
    bldn_k = models.CharField(max_length=15)
    appr = models.PositiveSmallIntegerField()
    tel = models.CharField(max_length=25)

