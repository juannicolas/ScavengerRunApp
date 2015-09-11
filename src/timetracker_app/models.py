from django.db import models


class Player(models.Model):
    mprid = models.CharField(verbose_name="MPR ID", max_length=3, primary_key=True, editable=True)
    full_name = models.CharField(verbose_name="Nombre Completo", max_length=200)
    phone = models.CharField(verbose_name="Telefono", max_length=10)
    email = models.EmailField(verbose_name="Email")

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"

    def __unicode__(self):
        return unicode(self.mprid)


class CheckPoint(models.Model):
    place_name = models.CharField(verbose_name="Nombre Lugar", max_length=60, unique=True)

    class Meta:
        verbose_name = "CheckPoint"
        verbose_name_plural = "CheckPoints"

    def __unicode__(self):
        return self.place_name


class RecordTime(models.Model):
    mprid = models.ForeignKey(Player)
    place_name = models.ForeignKey(CheckPoint)
    check_in_time = models.DateTimeField(verbose_name="CheckIn Time", auto_now=True)

    class Meta:
        verbose_name = "Tiempo"
        verbose_name_plural = "Tiempos"
        unique_together = ['mprid', 'place_name']

    def __unicode__(self):
        return unicode(self.mprid)

