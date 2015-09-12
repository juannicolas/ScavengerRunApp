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

    def get_last_checkpoint(self):
        try:
            last_record = RecordTime.objects.filter(player=self).order_by('-check_in_time')[0]
            return last_record
        except IndexError:
            return None

class CheckPoint(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    place_name = models.CharField(verbose_name="Nombre Lugar", max_length=60)

    class Meta:
        verbose_name = "CheckPoint"
        verbose_name_plural = "CheckPoints"

    def __unicode__(self):
        return self.place_name


class RecordTime(models.Model):
    player = models.ForeignKey(Player, related_name='record_time')
    check_point = models.ForeignKey(CheckPoint)
    check_in_time = models.DateTimeField(verbose_name="CheckIn Time", auto_now=True)
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        verbose_name = "Tiempo"
        verbose_name_plural = "Tiempos"
        unique_together = ['player', 'check_point']

    def __unicode__(self):
        return unicode('%s-%s' % (self.player.mprid ,self.check_point.place_name ))

