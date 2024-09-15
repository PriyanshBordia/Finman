from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health(_):
	return Response({"success": True})


@api_view(['GET'])
def api(request):
	return Response({"success": True, "data": request.user.username})

