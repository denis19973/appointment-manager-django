from rest_framework.decorators import api_view
from swingtime.models import Event, Occurrence
from rest_framework.response import Response
import json


@api_view(['GET'])
def get_appointment_data(request):
    occurences = Occurrence.objects.all()
    events = Event.objects.all()
    data = {}
    for e in events:
        list_occurences = []
        filter_occurences = occurences.filter(event_id=e.pk)
        for o in filter_occurences:
            dict_occurences = {}
            dict_occurences['start_time'] = str(o.start_time)
            dict_occurences['end_time'] = str(o.start_time)
            dict_occurences['id'] = o.pk
            list_occurences.append(dict_occurences)

        data[e.email] = list_occurences
    return Response(json.dumps(data))
