# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Incident, PersonInvolved

admin.site.register(Incident)
admin.site.register(PersonInvolved)


