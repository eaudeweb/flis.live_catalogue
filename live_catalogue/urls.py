from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import frame

from live_catalogue import views


admin.autodiscover()

settings_urls = [
    url(r'^categories/$',
        views.SettingsCategoriesView.as_view(),
        name='categories'),
    url(r'^categories/new/$',
        views.SettingsCategoriesAddView.as_view(),
        name='categories_add'),
    url(r'^categories/(?P<pk>.*)/edit$',
        views.SettingsCategoriesEditView.as_view(),
        name='categories_edit'),
    url(r'^categories/(?P<pk>.*)/delete$',
        views.SettingsCategoriesDeleteView.as_view(),
        name='categories_delete'),

    url(r'^topics/$',
        views.SettingsTopicsView.as_view(),
        name='topics'),
    url(r'^topics/new/$',
        views.SettingsTopicsAddView.as_view(),
        name='topics_add'),
    url(r'^topics/(?P<pk>.*)/edit$',
        views.SettingsTopicsEditView.as_view(),
        name='topics_edit'),
    url(r'^topics/(?P<pk>.*)/delete$',
        views.SettingsTopicsDeleteView.as_view(),
        name='topics_delete'),
    url(r'^(?P<setting_name>[^/]+)/update_order$',
        views.SettingsUpdateOrder.as_view(),
        name='update_order'),
]


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home',
        kwargs={'show': 'open'}),
    url(r'^closed/$', views.HomeView.as_view(), name='closed',
        kwargs={'show': 'closed'}),

    url(r'^need/add$', views.CatalogueEdit.as_view(),
        {'kind': 'need'}, name='catalogue_add'),
    url(r'^need/(?P<pk>\d+)/edit$', views.CatalogueEdit.as_view(),
        {'kind': 'need'}, name='catalogue_edit'),
    url(r'^need/(?P<pk>\d+)/delete$', views.CatalogueDelete.as_view(),
        {'kind': 'need'}, name='catalogue_delete'),
    url(r'^need/(?P<pk>\d+)$', views.CatalogueView.as_view(),
        {'kind': 'need'}, name='catalogue_view'),

    url(r'^offer/add$', views.CatalogueEdit.as_view(),
        {'kind': 'offer'}, name='catalogue_add'),
    url(r'^offer/(?P<pk>\d+)/edit$', views.CatalogueEdit.as_view(),
        {'kind': 'offer'}, name='catalogue_edit'),
    url(r'^offer/(?P<pk>\d+)/delete$', views.CatalogueDelete.as_view(),
        {'kind': 'offer'}, name='catalogue_delete'),
    url(r'^offer/(?P<pk>\d+)$', views.CatalogueView.as_view(),
        {'kind': 'offer'}, name='catalogue_view'),

    url(r'^catalogue/(?P<catalogue_id>\d+)/document/(?P<doc_id>\d+)',
        views.CatalogueDocumentDelete.as_view(),
        name='catalogue_document_delete'),

    url(r'my', views.MyEntries.as_view(), name='my_entries'),

    url(r'^settings/', include(settings_urls, namespace='settings')),

    url(r'^crashme/', views.CrashMe.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^select2/', include('django_select2.urls')),

    url(r'^notifications/',
        include('notifications.urls', namespace='notifications')),

    url(r'^_lastseencount/$', frame.utils.get_objects_from_last_seen_count),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
     static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
