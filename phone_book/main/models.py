from django.db import models


class Street(models.Model):
    st_id = models.AutoField(primary_key=True)
    st_val = models.CharField(max_length=100)

    def __str__(self):
        return self.st_val


class Nam(models.Model):
    name_id = models.AutoField(primary_key=True)
    name_val = models.CharField(max_length=100)

    def __str__(self):
        return self.name_val

    def get_abcolute_url(self):
        return '/name'


class Fam(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_val = models.CharField(max_length=100)

    def __str__(self):
        return self.s_val

    def get_abcolute_url(self):
        return '/surname'


class Otchestvo(models.Model):
    pat_id = models.AutoField(primary_key=True)
    pat_val = models.CharField(max_length=100)

    def __str__(self):
        return self.pat_val


class Main(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.ForeignKey(nam, on_delete=models.PROTECT, null=True)
    surname = models.ForeignKey(surname, on_delete=models.PROTECT, null=True)
    patronymic = models.ForeignKey(patronymic, on_delete=models.PROTECT, null=True)
    street = models.ForeignKey(street, on_delete=models.PROTECT, null=True)
    nb_hs = models.CharField(max_length=100, null=True)
    building = models.CharField(max_length=100, null=True)
    flat = models.CharField(max_length=100, null=True)
    ph_nb = models.CharField(max_length=100, null=True)
