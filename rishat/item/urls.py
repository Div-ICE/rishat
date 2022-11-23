from django.urls import path

from .views import SuccessView, buy_item, get_item_page

app_name = 'item'

urlpatterns = [
    path('item/<int:id>/', get_item_page, name='item'),
    path('buy/<int:id>/', buy_item, name='buy'),
    path('success/', SuccessView.as_view(), name='success'),
]
