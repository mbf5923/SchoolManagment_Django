
from rest_framework.views import APIView, Response
from datetime import datetime
import hashlib


class Index(APIView):

    def get(self, request,**kwargs):
        tm = datetime.now().timestamp()
        x = hashlib.md5(str(tm).encode()).hexdigest()
        data = {
            'name': 'ali',
            'stamp': datetime.now().timestamp(),
            'hash': x
        }

        return Response(data=data)
