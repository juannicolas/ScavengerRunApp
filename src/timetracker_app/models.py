from django.db import models


class Player(models.Model):
    id_player = models.CharField(verbose_name="MPR ID", max_length=6, primary_key=True, editable=True)
    full_name = models.CharField(verbose_name="Nombre Completo", max_length=200, editable=True)
    phone = models.CharField(verbose_name="Telefono", unique=True, max_length=10, editable=True)
    email = models.EmailField(verbose_name="Email", editable=True)

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __unicode__(self):
        return self.id_player


class CheckPoint(models.Model):
    id = models.IntegerField(verbose_name="ID", unique=True, editable=False, primary_key=True)
    place_name = models.CharField(verbose_name="Nombre Lugar", max_length=60, editable=True, default=True, unique=True)

    class Meta:
        verbose_name = "CheckPoint"
        verbose_name_plural = "CheckPoints"

    def __unicode__(self):
        return self.place_name


class RecordTime(models.Model):
    mpr_id = models.CharField(verbose_name="MPRID", max_length=6, editable=True)
    place_name_id = models.CharField(verbose_name="Check Point ID", max_length=1)
    check_in_time = models.TimeField(verbose_name="CheckIn Time", auto_now=True)

    class Meta:
        verbose_name = "Tiempo"
        verbose_name_plural = "Tiempos"

    def __unicode__(self):
        return self.mpr_id

