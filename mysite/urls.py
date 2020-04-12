from django.contrib import admin
from webProject import views
from django.urls import include
from django.urls import path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.HomePageView.as_view()),
    path('calisanlar/', views.tum_calisanlar),
    path('calisan/,<int:calisan_no>/', views.calisan_detay),
    path('yoneticiler/', views.tum_yoneticiler),
    path('yonetici/,<int:yonetici_no>/', views.yonetici_detay),
    path('planlar/', views.tum_planlar),
    path('plan/,<int:plan_no>/', views.plan_detay),
    path('mekanlar/', views.tum_mekanlar),
    path('mekan/,<int:mekan_no>/', views.mekan_detay),

    path('GirisSayfasi/', views.GirisSayfasi.as_view()),
    path('GirisSayfasi/ProfilSayfasi/', views.ProfilSayfasi.as_view()),
    path('GirisSayfasi/ProfilSayfasi/CalismaPlani/', views.CalismaPlani.as_view()),
    path('GirisSayfasi/ProfilSayfasi/CalismaPlani/GirisSayfasi/', views.GirisSayfasi.as_view()),
    path('GirisSayfasi/ProfilSayfasi/GecmisCalismaPlani/', views.GecmisCalismaPlani.as_view()),
    path('GirisSayfasi/ProfilSayfasi/İstekYap/', views.İstekYap.as_view()),
    path('GirisSayfasi/ProfilSayfasi/DegisiklikTalebi/', views.DegisiklikTalebi.as_view()),
    path('GirisSayfasi/ProfilSayfasi/MesajKutusu/', views.MesajKutusu.as_view()),
    path('GirisSayfasi/ProfilSayfasi/İstekYap/IstekYapSec/', views.IstekYapSec.as_view()),
    path('GirisSayfasi/ProfilSayfasi/CalismaPlani/GecmisShift/', views.GecmisShift.as_view()),


)
