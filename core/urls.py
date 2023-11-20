
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version='v1',
#         description="Your API description",
#         terms_of_service="https://www.yourapp.com/terms/",
#         contact=openapi.Contact(email="contact@yourapp.com"),
#         license=openapi.License(name="Your License"),
#     ),
#     public=True,
# )

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
#          name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
#          name='schema-redoc'),
#     # ... your other app URLs ...
# ]



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name = 'home'),
    path('page/', page, name = 'page'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),

    path('recipes/', recipes, name = 'recipes'),
    path('delete_recipe/<id>/', delete_recipe, name = 'delete_recipe'),
    path('update_recipe/<slug>/', update_recipe, name = 'update_recipe'),

    path('login/', login_page, name = 'login_page'),
    path('logout/', logout_page, name = 'logout_page'), 
    path('register/', register_page, name = 'register_page'),

    path('students/', get_students, name = 'get_students'),
    path('get_markssss/<student_id>', get_marks, name = 'get_mark'),

    path('send_email/', send_email, name = 'send_email'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('get_data/', getData, name = 'getData'),
    path('post_data/', postData, name = 'postData'),


    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    # name='schema-info')
    
    # path('openapi', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …",
    #     version="1.0.0"
    # ), name='openapi-schema'),

    # path('swagger/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()