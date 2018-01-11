from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Baza(models.Model):
    numer_obrazka = models.IntegerField()

    @staticmethod
    def getInstance():
        if Baza.objects.count() > 0:
            return Baza.objects.all()[0]
        else:
            baza = Baza.objects.create(numer_obrazka=0)
            baza.save()
            return baza

    @staticmethod
    def nextNumerObrazka():
        baza = Baza.getInstance()
        baza.numer_obrazka += 1
        baza.save()
        return baza.numer_obrazka

    @staticmethod
    def resetNumerObrazka():
        baza = Baza.getInstance()
        baza.numer_obrazka = 0
        baza.save()
