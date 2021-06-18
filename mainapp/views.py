from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth
from firebase_admin.firestore import SERVER_TIMESTAMP
from django.contrib import messages
from . import firestore
from datetime import datetime
from dateutil.parser import parse
# Create your views here.

dict_user_id = {
	'aaitenov': 'pUQDenwKnQeB5YPPbv0u',
}
dict_service_id = {
	'thegarage.kz': '2Qq0FOp3FECeCW3AjRrv',
	'The LOFT barbershop': 'SIDGcFcEp8euJbub7eKD',
	'AvtoPokras.kz': 'i172PRXIRUBJwwTWgSpD',
	'Gata': 'jAv3SGwy5m3q7CjDLpk5',
}
def home(request):
	context = {}
	if request.method != "POST":
		results = firestore.db.collection('services').get()
		services = []
		for result in results:
			services.append(result.to_dict())
		context = {'services': services}

	return render(request, 'main/home.html', context)

def search(request):
	if request.method == "POST":
		services = []
		search_word = request.POST.get('search')
		results = firestore.db.collection("services").order_by("name").where("name", ">=", search_word.upper()).where("name", "<=", search_word.lower() + "\uf8ff").get()	
		for result in results:
			result = result.to_dict()
			result['type'] = 'search'
			services.append(result)
		context = {'services': services}
		print(services[0]['type'])
		return render(request, 'main/home.html', context)

def getUserInfo(user):
	results = firestore.db.collection('users').where('username', '==', user).get()
	result = results[0].to_dict()
	return result

def getserviceInfo(service, offer):
	result = firestore.db.collection('services').where('name', '==', service).get()
	result = result[0].to_dict()
	newList = result['services']
	i = 0
	while i < len(newList):
		if newList[i]['name'] == offer:
			return i, result['location']
		i += 1


def service(request, serviceName):
	if request.method == "POST":
		user = getUserInfo(request.user.username)
		username = user['username']
		phone = user['phone']
		serviceN = request.POST.get('service')
		offer = request.POST.get('offer')
		offerId, location = getserviceInfo(serviceN, offer)
		date = request.POST.get('date')
		data = {
			'dateTime': parse(date),
			'serviceId': dict_service_id[serviceN],
			'serviceInfoId': offerId,
			'serviceLocation': location,
			'serviceName': offer,
			'userId': dict_user_id[username],
			'userName': username,
			'userPhone': phone
		}
		firestore.db.collection('appointments').add(data)
		return redirect('home')
	result3 = firestore.db.collection('services').document()
	result1 = firestore.db.collection('services').where('name', '==', serviceName).get()
	result2 = firestore.db.collection('categories').get()
	cat = []
	for result in result2:
		cat.append(result.to_dict())
	i = 0
	while i < len(cat):
		lists = cat[i]['services']
		for list in lists:
			if serviceName in list.values():
				category = cat[i]['name']
				break
		i += 1

	
	result1 = result1[0].to_dict()
	result1['category'] = category
	context = {'service': result1}
	return render(request, 'main/service.html', context)