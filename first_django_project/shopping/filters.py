from django.contrib import admin
from django.db import models


class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('0', '< 100'),
            ('1', '100-200'),
            ('2', '201-300'),
            ('3', '301-400'),
            ('4', '400 <'),
        ]

    def queryset(self, request, queryset):
        print(self.value())
        if self.value() == '0':
            queryset = queryset.filter(price__lt=100)
        if self.value() == '1':
            queryset = queryset.filter(price__gte=100, price__lte=200)
        if self.value() == '2':
            queryset = queryset.filter(price__gte=201, price__lte=300)
        if self.value() == '3':
            queryset = queryset.filter(price__gte=301, price__lte=400)
        if self.value() == '4':
            queryset = queryset.filter(price__gte=401)

        return queryset

from django.contrib import admin


class AgeRangeFilter(admin.SimpleListFilter):
    title = 'Age range'
    parameter_name = 'age_range'

    def lookups(self, request, model_admin):
        return [
            ('0', '18'),
            ('1', '18-20'),
            ('2', '21-30'),
            ('3', '31-40'),
            ('4', '40 <'),
        ]

    def queryset(self, request, queryset):
        print(self.value())
        if self.value() == '0':
            queryset = queryset.filter(age__lt=18)
        if self.value() == '1':
            queryset = queryset.filter(age__gte=18, age__lte=20)
        if self.value() == '2':
            queryset = queryset.filter(age__gte=21, age__lte=30)
        if self.value() == '3':
            queryset = queryset.filter(age__gte=31, age__lte=40)
        if self.value() == '4':
            queryset = queryset.filter(age__gte=41)

        return queryset

class AgeRangeFilter2(admin.SimpleListFilter):
    title = 'Age range 2'
    parameter_name = 'age_range2'

    def lookups(self, request, model_admin):
        print(model_admin)
        queryset = model_admin.get_queryset(request)
        # min_value = min(queryset, key=lambda x: x.age).age
        # max_value = max(queryset, key=lambda x: x.age).age
        min_value = queryset.aggregate(min_value=models.Min('age'))['min_value']
        max_value = queryset.aggregate(max_value=models.Max('age'))['max_value']
        step = 10

        lookups = []
        for start in range(min_value, max_value + 1, step):
            end = start + step - 1
            lookup_value = f"{start}-{end}"
            lookup_label = f"{start} to {end}"
            lookups.append((lookup_value, lookup_label))

        return lookups

    def queryset(self, request, queryset):
        if self.value():
            start = self.value().split('-')[0]
            end = self.value().split('-')[1]
            return queryset.filter(age__gte=start, age__lte=end)
        return queryset