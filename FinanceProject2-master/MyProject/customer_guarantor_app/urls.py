from django.urls import path
from .import views

urlpatterns=[
    path('add_guarantor/', views.add_guarantor_view, name='addguarantor'),
    path('show_guarantor/<int:i>', views.show_guarantor_view, name='showguarantor'),
    #path('update_guarantor/<int:i>', views.update_guarantor_view.as_view(), name='updateguarantor'),
    #path('delete_guarantor/<int:i>', views.delete_guarantor_view.as_view(), name='deleteguarantor'),
]