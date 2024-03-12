"""
ASGI config for SherlocksEye project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from main.consumers import PracticeConsumer
import os
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SherlocksEye.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path('practice/', PracticeConsumer.as_asgi()),
    ])
})

