from django.contrib import admin


class PublishedYearFilter(admin.SimpleListFilter):
    title = 'Published year range'
    parameter_name = 'published_year'

    def lookups(self, request, model_admin):
        return [
            ('0', '< 1900'),
            ('1', '1900-2000'),
            ('2', '2000 <'),
        ]

    def queryset(self, request, queryset):
        print(self.value())
        if self.value() == '0':
            queryset = queryset.filter(published_year__lt=1900)
        if self.value() == '1':
            queryset = queryset.filter(published_year__gte=1900, published_year__lte=2000)
        if self.value() == '2':
            queryset = queryset.filter(published_year__gte=2001)

        return queryset

from django.contrib import admin