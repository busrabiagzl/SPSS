from django.db import models



class Calisanlar(models.Model):
    ad=models.CharField(max_length=30)
    soyad=models.CharField(max_length=30)
    kullanici_adi=models.CharField(max_length=10)
    sifre=models.CharField(max_length=30)
    calisma_turu=models.CharField(max_length= 30)
    departman=models.CharField(max_length=30)
    def __str__ (self):
        return '{} {}'.format(self.ad, self.soyad)


class Yoneticiler(models.Model):
    ad=models.CharField(max_length=30)
    soyad=models.CharField(max_length=30)
    kullanici_adi = models.CharField(max_length=10)
    sifre=models.CharField(max_length=30)
    calisma_turu = models.CharField(max_length=30)
    departman = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.ad, self.soyad)

class Mekanlar(models.Model):
    mekan_ismi=models.CharField('mekan ismi', max_length=120)
    mekan_adresi=models.CharField(max_length=300)
    def __str__(self):
        return '{}'.format(self.mekan_ismi)

class Planlar(models.Model):
    plan_tarihi = models.DateField('plan tarihi')
    giris_saati = models.TimeField('Giriş Saati' )
    sure = models.DurationField('Süre')
    cikis_saati = models.TimeField('Çıkış Saati')
    plan_gunu = models.CharField(max_length=30)
    mekan=models.ForeignKey(Mekanlar , on_delete=models.CASCADE)
    yonetici=models.ManyToManyField(Yoneticiler)
    calisan=models.ManyToManyField(Calisanlar)
    def __str__ (self):
        return '{}'.format(self.plan_tarihi)



