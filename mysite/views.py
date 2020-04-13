from django.shortcuts import render
from django.views.generic import TemplateView
from webProject.models import Calisanlar
from webProject.models import Yoneticiler
from webProject.models import Planlar
from webProject.models import Mekanlar

def tum_planlar(request):
    plan_list= Planlar.object.all()
    context = {'plan_list' : plan_list}
    return render(request, 'gecmis_goruntuleme.html', context )
def gecmis_shift(request):
    plan_list= Planlar.object.all()
    context = {'plan_list' : plan_list}
    return render(request, 'gecmis_shift.html', context )
def plan_detay(request, plan_no):
    plan = Planlar.object.get(plan_no=plan_no)
    context = {'plan': plan}
    return render(request, 'calisma_plani_goruntuleme.html', context)

def mekan_detay(request, mekan_no):
    mekan = Mekanlar.object.get(mekan_no=mekan_no)
    context = {'mekan': mekan}
    return render(request, 'mekan_goruntuleme.html', context)
def tum_mekanlar(request):
    mekan_list = Mekanlar.object.all()
    context = {'mekan_list': mekan_list}
    return render(request, 'mekanlar.html', context)

def tum_calisanlar(request):
    yonetici_list = Yoneticiler.object.all()
    context = {'calisan_list': yonetici_list}
    return render(request, 'calisanlar.html', context)
def calisan_detay(request, calisan_no):
    calisan = Calisanlar.object.get(calisan_no=calisan_no)
    context ={'calisan': calisan}
    return render(request, 'calisan_detay.html', context)

def tum_yoneticiler(request):
    yonetici_list = Yoneticiler.object.all()
    context = {'yonetici_list': yonetici_list}
    return render(request, 'yoneticiler.html', context)
def yonetici_detay(request, yonetici_no):
    yonetici = Yoneticiler.object.get(yonetici_no=yonetici_no)
    context ={'yonetici': yonetici}
    return render(request, 'yonetici_detay.html', context)

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class GirisSayfasi(TemplateView):
    def get(self,request, *args,**kwargs):
        return  render(request, 'giris_sayfasi.html', context=None)

class ProfilSayfasi(TemplateView):
    def get(self,request, *args,**kwargs):
        return  render(request, 'profil_ekrani.html', context=None)

class CalismaPlani(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'calisma_plani_goruntuleme.html', context=None)

class GecmisCalismaPlani(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'gecmis_goruntuleme.html', context=None)

class GecmisShift(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'gecmis_shift.html', context=None)

class İstekYap(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'istek_yap.html', context=None)

class DegisiklikTalebi(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'degisiklik_talebi.html', context=None)

class MesajKutusu(TemplateView):
        def get(self, request, *args, **kwargs):
            return render(request, 'chat.html', context=None)


class IstekYapSec(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'istek_yap_sec.html', context=None)
