from django.contrib import admin
from django.urls import path, include
from Register import views as v

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include("Teacher.urls")),
	path('', include("Student.urls")),
	path('register/', v.register, name="register"),
	path("", include("django.contrib.auth.urls")),

]
