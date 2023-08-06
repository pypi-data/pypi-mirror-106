# TPL_Accounting
---
Description: A TPL_Accounting pluggable package
---

Install the package:
```text
pip install TPL-Accounting
```
## Add these to your settings:
> _import:_
```text
import accounting
```
![](for_readme/import.png)
> _add apps and currency format:_
```text
INSTALLED_APPS = [] + accounting.get_apps()

ACCOUNTING_DEFAULT_CURRENCY = '৳'
```
![](for_readme/apps_currency.png)

> _Templates:_
![](for_readme/templates.png)

> _Static files:_
```text
"accounting/staticfiles"
```
![](for_readme/static.png)


## Include apps urls to your main urls.py:
```text
from accounting.apps.connect.login import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounting.apps.connect.urls')),
    path('accounting/', include('accounting.apps.books.urls')),
    path('people/', include('accounting.apps.people.urls')),
    path('reports/', include('accounting.apps.reports.urls')),

    # auth
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),

    # third party
    path("select2/", include("django_select2.urls")),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
```
![](for_readme/urls.png)