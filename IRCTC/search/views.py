from django.shortcuts import render
from search.forms import trainSearchForm
from search.models import StationList
from search.models import TrainList

def trainSearch(request):
    if request.method == "POST":
        form = trainSearchForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data["source"]
            destination = form.cleaned_data["destination"]
            
            try:
                station_source_instance = StationList.objects.get(station=source)
                station_source_code = station_source_instance.station_code
            except StationList.DoesNotExist:
                station_source_code = "None"  # Handle the case where source station doesn't exist

            try:
                station_destination_instance = StationList.objects.get(station=destination)
                station_destination_code = station_destination_instance.station_code
            except StationList.DoesNotExist:
                station_destination_code = "None"  # Handle the case where destination station doesn't exist
            
            #   print("source = "+station_source_code+" destination = "+station_destination_code)
            
            
            train_instances = TrainList.objects.filter(source_station_code=station_source_code, destination_station_code=station_destination_code)
            train_list = []

            # Iterate over each TrainList object
            for train_instance in train_instances:
                # Assuming train_no is unique and can be used as keys in the dictionary
                # You can adjust this according to your needs
                print (train_instance.station_name)
                dict = {
                    'train_no' : train_instance.train_no,
                    'train_name' : train_instance.train_name,
                    'station_name' : train_instance.station_name,
                    'arrival_time' : train_instance.arrival_time,
                    'departure_time' : train_instance.departure_time,
                    'distance' : train_instance.distance,
                }
                print(dict)
                train_list.append(dict)
           
    else:
        form = trainSearchForm()
        train_dict = {}
    return render(request,"search/train_search.html",{"form":form,"train_list":train_list})