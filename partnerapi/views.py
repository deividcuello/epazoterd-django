from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Partner
from .serializers import PartnerSerializer
# from .permissions import HasRequiredPermissionForMethod

class PartnerApiView(APIView):
    
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    
    
    # permission_classes = [HasRequiredPermissionForMethod]
    # get_permission_required = 'permission_to_read_this'
    # put_permission_required = 'permission_to_update_this'
    # post_permission_required = 'permission_to_create_this'

    # 1. List all
    def get(self, request, *args, **kwargs):
        category = (request.GET.get('category'))
        id = (request.GET.get('id'))
        contain_word = (request.GET.get('contain'))
        isAdmin = request.GET.get('isAdmin')
 
        partner = Partner.objects.all().order_by('-created_at')

        partnerCount = partner.count()
        serializer = PartnerSerializer(partner, many=True)
        return Response({
            'partner': serializer.data,
            'count': partnerCount}, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
 
        data = {
            'cv_file': request.data.get('cv_file'), 
            'phone': request.data.get('phone'), 
            'message': request.data.get('message'), 
            'name': request.data.get('name'), 
            'user_pk': request.data.get('user_pk')
        }

        serializer = PartnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PartnerDetailApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # permission_classes = [HasRequiredPermissionForMethod]
    # get_permission_required = 'permission_to_read_this'
    # put_permission_required = 'permission_to_update_this'
    # post_permission_required = 'permission_to_create_this'
    
    def get_object(self, partner_id, user_id):

        try:
            return Partner.objects.get(id=partner_id)
        except Partner.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, partner_id, *args, **kwargs):
 
        partner_instance = self.get_object(partner_id, request.user.id)
        if not partner_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PartnerSerializer(partner_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        isCV = 'http://localhost:8000/media' in request.data.get('isCV')
        isAdmin = request.GET.get('isAdmin')
        
        partner_instance = self.get_object(partner_id, request.user.id)
        if not cpartner_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PartnerSerializer(instance = partner_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 4. Update
    def put(self, request, partner_id, *args, **kwargs):
        update_name = request.data.get('update_name')
        update_phone = request.data.get('update_phone')

        partner_instance = self.get_object(partner_id, request.user.id)

        if not partner_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if(update_name):
            data = {
                'name': " ".join(request.data.get('name').title().split())
            }
        elif(update_phone):
            data = {
                'phone': request.data.get('phone')
            }

        serializer = PartnerSerializer(instance = partner_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, partner_id, *args, **kwargs):

        partner_instance = self.get_object(partner_id, request.user.id)
        if not partner_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        partner_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
