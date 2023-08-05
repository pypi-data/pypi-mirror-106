"""Brousable router and views for django rest framework."""

from .router import APIRouter
from .views import BaseAPIView
from .mixins import GetMixin, PostMixin, PutMixin, PatchMixin, DeleteMixin
