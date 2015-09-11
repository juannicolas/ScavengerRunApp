from django.db import models


class Player(models.Model):
    mpr_id = models.CharField(verbose_name="MPR ID", max_length=3, unique=True)
    full_name = models.CharField(verbose_name="Nombre Completo", max_length=200)
    phone = models.CharField(verbose_name="Telefono", max_length=10)
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __unicode__(self):
        return self.id_player


class CheckPoint(models.Model):
    place_name = models.CharField(verbose_name="Nombre Lugar", max_length=60, unique=True)

    class Meta:
        verbose_name = "CheckPoint"
        verbose_name_plural = "CheckPoints"

    def __unicode__(self):
        return self.place_name


class RecordTime(models.Model):
    mpr_id = models.ForeignKey(Player)
    place_name_id = models.CharField(verbose_name="Check Point ID", max_length=1)
    check_in_time = models.TimeField(verbose_name="CheckIn Time", auto_now=True)

    class Meta:
        verbose_name = "Tiempo"
        verbose_name_plural = "Tiempos"

    def __unicode__(self):
        return unicode(self.mpr_id)

