# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import Type, Category, Variety, Condition


admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Variety)
admin.site.register(Condition)
