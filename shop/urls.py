from django.urls import path
from . import views

urlpatterns=[
     path('',views.index,name='ShopHome'),
     path("about",views.about,name="About"),
     path("contact",views.contact,name="ContactMe"),
     path("tracker",views.tracker,name="Tracker"),
     path("search",views.search,name="Search"),
     path("products/<int:myid>",views.prodview,name="ProductView"),
     path("checkout",views.checkout,name="CheckOut"),

]
