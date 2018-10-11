from django.db import models


# Create your models here.
class Language(models.Model):
    MACHINE_LANGUAGE = "ML"
    ASSEMBLY_LANGUAGE = "AL"
    HIGH_LEVEL_LANGUAGE = "HLL"
    LANGUAGE_CHOICES = (
        (MACHINE_LANGUAGE, "Machine Language"),
        (ASSEMBLY_LANGUAGE, "Assembly Language"),
        (HIGH_LEVEL_LANGUAGE, "High Level Language")
    )
    name = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    language_type = models.CharField(choices=LANGUAGE_CHOICES, max_length=100)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    sample_date = models.DateField()
    rating = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("language", "sample_date")

    def __unicode__(self):
        return "%s - %s %%" % (self.language, self.rating * 100)
