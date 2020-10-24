from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from chat_app.consumer import ChatConsumer
from django.conf.urls import url


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^chats/(?P<username>[\w.@+-]+)$",ChatConsumer ),
                ]
                
            )
        )
    )
})