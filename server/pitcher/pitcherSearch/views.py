from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer
from .utils import getPerplex,getPitch

from django.http import StreamingHttpResponse
import json
# from .getPitch import PitchGenerator
from django.http import JsonResponse
# Create your views here.

class ProductSearch(APIView):

    # # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    #get product details from db
    def get(self, request, *args, **kwargs):

        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #add product in db
    # def post(self, request, *args, **kwargs):
    #     result = getPerplex(request.data.get('name'))
    #     print(result)
    #     data = {
    #         'name': request.data.get('name'),
    #         'price': request.data.get('price'),
    #         'dimensions': request.data.get('dimensions'),
    #         'pros': request.data.get('pros'),
    #         'cons': request.data.get('cons'),
    #         'reviews': request.data.get('reviews'),
    #         'stars': request.data.get('stars')
    #     }

    #     serializer = ProductSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        product_name = request.data.get('name')

        async def async_generator():
                # Step 1: Get product details using Perplexity AI
                product_details = "{\"id\": \"abb76ce1-2872-45f1-a606-03e21f8b0fd9\", \"model\": \"llama-3.1-sonar-small-128k-online\", \"created\": 1724910832, \"usage\": {\"prompt_tokens\": 56, \"completion_tokens\": 506, \"total_tokens\": 562}, \"object\": \"chat.completion\", \"choices\": [{\"index\": 0, \"finish_reason\": \"stop\", \"message\": {\"role\": \"assistant\", \"content\": \"### Cost\\nThe TCL 55\\\" Class 4-Series 4K UHD Smart Roku TV is available for around $346.95 on Amazon, with occasional discounts that bring the price down to $274.00.\\n\\n### Dimensions\\n- **Weight:** 23 pounds\\n- **Dimensions:** 11.8 x 48.7 x 30.4 inches\\n\\n### Pros\\n1. **Stunning Picture Quality:** The TV delivers stunning 4K UHD picture quality with four times the resolution of Full HD, enhancing clarity and detail.\\n2. **HDR Technology:** High Dynamic Range (HDR) technology provides bright and accurate colors for a lifelike viewing experience.\\n3. **Easy Voice Control:** Works with popular voice assistants like Siri, Alexa, and Hey Google for seamless control.\\n4. **Simple, Personalized Home Screen:** Easy access to thousands of streaming channels, cable TV, gaming consoles, and other devices without complicated menus.\\n5. **Endless Entertainment:** Supports various content sources, including streaming services, cable/satellite subscriptions, and free over-the-air channels.\\n6. **Game Mode:** A dedicated Game Mode adjusts picture settings for an optimized fast-response gaming experience.\\n\\n### Cons\\n1. **HDR Limitations:** Some users have noted that the HDR performance is not as good as higher-end models, such as the TCL 6 Series.\\n2. **Brightness Issues:** Some users have reported brightness issues, particularly with the backlight, which can be resolved by adjusting the settings or replacing the backlights if necessary.\\n\\n### Reviews and Stars\\nThe TCL 55\\\" Class 4-Series 4K UHD Smart Roku TV generally receives positive reviews, but with some caveats regarding HDR performance and brightness.\\n\\n- **Amazon Rating:** Typically 4.2 out of 5 stars, with many users praising its picture quality, ease of use, and value for money.\\n- **Reddit Reviews:** Users on Reddit have mixed opinions, with some praising its performance for the price and others noting issues with HDR and brightness.\\n\\nOverall, the TCL 55\\\" Class 4-Series 4K UHD Smart Roku TV is a solid choice for those looking for a budget-friendly 4K UHD TV with a wide range of entertainment options, but it may not meet the expectations of those seeking superior HDR performance.\"}, \"delta\": {\"role\": \"assistant\", \"content\": \"\"}}]}"
                # product_details = getPerplex(product_name)
                yield json.dumps({
                    'step': 'product_details',
                    'data': product_details
                }) + '\n'

                pitches = getPitch(product_details)
                yield json.dumps(pitches, indent=4) + '\n'

        async def wrap_async_generator(gen):
            async for item in gen:
                yield item

            # Ensure the generator is awaited properly
        response = StreamingHttpResponse(wrap_async_generator(async_generator()), content_type='application/json')
        return response
