# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import Type, Category


admin.site.register(Type)
admin.site.register(Category)
