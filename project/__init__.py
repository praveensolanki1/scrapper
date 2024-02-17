from __future__ import absolute_import, unicode_literals
from .celery import app as new_app


__all__=['new_app']