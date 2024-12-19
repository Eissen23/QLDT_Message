from django.shortcuts import render
from rest_framework.response import Response
from .models import MessageNotification
from .serializers import MessageNotificationSerializer
import traceback
import requests
from rest_framework.views import APIView
from rest_framework import status
import random, string

CHECK_URL = "https://127.0.0.1:8000/auth/user/Verify"

def check_legit(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(CHECK_URL, headers=headers)
        if response.status == 200:
            return {"legit":True, "role": response.data['is_teacher']}
        else:
            return {"legit":False, "role": False} 
    except Exception as e:
        traceback.print_exc(e)
        
def generate_random_string(length=8):
    chars = string.ascii_letters + string.digits
    rand_chars = ''.join(random.choices(chars,k=length))
    return rand_chars
        
# Create your views here.
class MessageSender(APIView):
    serializer_class = MessageNotificationSerializer
    def post(self,request):
        try:
            data = request.data
            # Block nay ko can thiet khi co authorization
            access_token = data['token']
            '''
            result_legit = check_legit(access_token)
            if result_legit['legit']:
                
            {Block for check legit here}
            '''
            # Thay thế với thông tin user trong authorization
            sender_id  = data['sender_id']
            # Block này cứ tiếp tục như thường
            receiver_id = data['user_id']
            type = data['type']
            related_id = data['related_id']
            message = data['message']
            is_read = False
            
            message_id = generate_random_string()
            msgstr = MessageNotification(message_id=message_id,sender_id=sender_id, receiver_id=receiver_id, type=type, related_id=related_id, message=message,is_read=is_read)
            msgstr.save()
            return Response({'code':1000, 'msg':"OK"}, status=status.HTTP_201_CREATED)    
                    
        except Exception as e:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request):
        try:
            data = request.data
            # Block nay ko can thiet khi co authorization
            access_token = data['token']
            '''
            result_legit = check_legit(access_token)
            if result_legit['legit']:
                
            {Block for check legit here}
            '''
            # Thay thế với thông tin user trong authorization
            receiver = data['receiver']
            # Block này cứ tiếp tục như thường
            index = int(data['index'])
            count = int(data['count'])
            received_notifs = MessageNotification.objects.filter(receiver_id = receiver)[index:index + count]
            received_notifs = MessageNotificationSerializer(received_notifs, many = True)    
            
                
            return Response({'code':100,'msg':'OK','list': received_notifs.data}) 
        except Exception as e:
            traceback.print_exc()
            return Response({'error': 'Some exeption happened'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
