from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'), 
   path('about/', views.about, name='about'),
   path('coins/', views.coins_index, name='index'),
   path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
   path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
   path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
   path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
   path('coins/<int:coin_id>/add_acquired/', views.add_acquired, name='add_acquired'),
   path('coins/<int:coin_id>/assoc_collector/<int:collector_id>/', views.assoc_collector, name='assoc_collector'),
   path('collectors/', views.CollectorList.as_view(), name='collectors_index'),
   path('collectors/<int:pk>/', views.CollectorDetail.as_view(), name='collectors_detail'),
   path('collectors/create/', views.CollectorCreate.as_view(), name='collectors_create'),
   path('collectors/<int:pk>/update/', views.CollectorUpdate.as_view(), name='collectors_update'),
   path('collectors/<int:pk>/delete/', views.CollectorDelete.as_view(), name='collectors_delete'),
]
