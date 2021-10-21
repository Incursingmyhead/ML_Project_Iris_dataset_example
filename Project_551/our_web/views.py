from django.shortcuts import render
import pyrebase
import json
from KNN_Analysis import functions_pack as fp
from django.http import HttpResponse, HttpResponseRedirect

dic = dict()

# Create your views here.
def Data_pst(request):
    global dic
    df = fp.get_database_data()
    #print(df)
    #df = json.dumps(df)
    img_data = fp.getimagedata()
    if 'user_table.json' in dic:
        selected = 1
        url = "https://iris-storage-default-rtdb.firebaseio.com/"
        model = fp.model_building(url + dic['user_table.json'] + '.json')
    else:
        selected =  0
        model =None
    return render(request,"main_fw.html",{'data': df, 'imgdata':json.dumps(img_data),'user_model':selected,'build': model})
def get_data(request):
    global dic
    num_features = request.GET["features_extract"]
    final_table = fp.features_selector(num_features)
    resp, dic = fp.upload_user_table(final_table)
    if resp:
        #return HttpResponse("Completed.\n"+"You choose " + num_features + " features. \n" +"The features have sucessfully update to database.\n" +"The node id in database is " + dic['user_table.json'])
        return HttpResponseRedirect(redirect_to="/")

'''def check(request):
    return render(request,"check.html")'''

