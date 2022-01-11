from progress.models import Commercial
from progress.serializers import CommercialSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from uuid import uuid4


def get_session_id(request):
    if 'HTTP_DIQ_COMMERCIAL_SESSION_ID' in request.META:
        session_id = request.META['HTTP_DIQ_COMMERCIAL_SESSION_ID']
    elif 'session_id' in request.data:
        session_id = request.data.get('session_id')
    elif 'session_id' in request.query_params:
        session_id = request.query_params.get('session_id')
    else:
        raise exceptions.ParseError('Session Id is not provided!')

    return session_id


class RetrieveCreateUpdateMe(APIView):

    def get(self, request):
        session_id = get_session_id(request)

        try:
            commercial = Commercial.objects.get(session_id=session_id)
            serializer = CommercialSerializer(commercial)
            return Response(serializer.data)
        except Commercial.DoesNotExist:
            return Http404('Commercial does not exist')

    def post(self, request):
        session_id = get_session_id(request)

        try:
            Commercial.objects.get(session_id=session_id)
            return Response(session_id)
        except Commercial.DoesNotExist:
            session_id = str(uuid4())
            serializer = CommercialSerializer(data={'session_id': session_id})
            if serializer.is_valid():
                serializer.save()
                return Response(session_id)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        session_id = get_session_id(request)

        try:
            commercial = Commercial.objects.get(session_id=session_id)
            serializer = CommercialSerializer(commercial, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Commercial.DoesNotExist:
            raise Http404('Commercial does not exist')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
