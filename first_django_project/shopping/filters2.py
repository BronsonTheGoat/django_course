from django.contrib import admin
from django.db import models


class IntegerRangeFilter(admin.SimpleListFilter):
    title = 'Integer range'
    parameter_name = None
    field_name = None
    step = 100

    def lookups(self, request, model_admin):
        if not self.field_name:
            return []

        queryset = model_admin.get_queryset(request)
        min_value = queryset.aggregate(min_value=models.Min(self.field_name))['min_value']
        print(min_value)
        max_value = queryset.aggregate(max_value=models.Max(self.field_name))['max_value']
        print(max_value)

        lookups = []
        for start in range(min_value, max_value + 1, self.step):
            end = start + self.step - 1
            filter_kwargs = {
                f'{self.field_name}__gte': start,
                f'{self.field_name}__lte': end
            }
            if not queryset.filter(**filter_kwargs):
                continue
            lookup_value = f"{start}-{end}"
            lookup_label = f"{start} to {end}"
            lookups.append((lookup_value, lookup_label))

        return lookups

    def queryset(self, request, queryset):
       if not self.field_name:
           return queryset

       if self.value():
           start = self.value().split('-')[0]
           end = self.value().split('-')[1]
           filter_kwargs = {
                f'{self.field_name}__gte': start,
                f'{self.field_name}__lte': end
           }
           print(filter_kwargs)
           return queryset.filter(**filter_kwargs)

       return queryset


class PriceRangeFilter(IntegerRangeFilter):
    title = 'Price range (new)'
    parameter_name = 'price_range2'
    field_name = 'price'
    step = 50


class AgeRangeFilter(IntegerRangeFilter):
    title = 'Age'
    parameter_name = 'age_range'
    field_name = 'age'
    step = 10
