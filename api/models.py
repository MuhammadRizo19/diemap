from django.db import models


class DieMap(models.Model):
    sapcode = models.CharField(max_length=100, unique=True)
    benkam = models.CharField(max_length=100)
    synced_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'die_map'
        ordering = ['sapcode']

    def __str__(self):
        return f"{self.sapcode} → {self.benkam}"
