from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout 
from firebase_admin import auth
from django.contrib import messages
from mainapp import firestore
from mainapp.views import getUserInfo
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
def firestore_register(data):
    try:
    	user = auth.create_user(email = data['email'], password = data['password'])
    except ValueError:
    	return 'ValueError'
    except FirebaseError:
    	return 'FirebaseError'
    else:
    	firestore.db.collection('users').add(data)
    	return 'success' 

def registerPage(request):
	form = UserCreationForm()
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		
		if form.is_valid():
			username = form.cleaned_data.get('username')
			user_pass = form.cleaned_data.get('password1')
			email = request.POST.get('email')
			phone = request.POST.get('phone')
			data = {
					'username': username,
					'email': email,
					'phone': phone,
					'password': user_pass
				}
			form.save()
			firestore_register(data)
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form': form}
	return render(request, 'user/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		context = {}
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None and firestore_login(username, password) == 'succes':
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR Password is incorrect')
				return render(request, 'user/login.html', context)
		else:
			return render(request, 'user/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def firestore_login(login, password):
    user = firestore.db.collection('users').where('username', '==', login).get()
    if user:
        user = user[0]
        user = user.to_dict()
        legitPassword = user['password']
        if legitPassword == password:
            return 'succes'

        else:
            return 'wrong password'
    else:
        return 'wrong login'


def getUrlPrice(serviceName, offerId):
	print(serviceName)
	print(offerId)
	result = firestore.db.collection('services').where('name', '==', serviceName).get()
	print(result)
	data = result[0].to_dict()

	return data['imageUrl'], data['services'][offerId]['price']


def profile(request):
	user = getUserInfo(request.user.username)
	results = firestore.db.collection('appointments').where('userName', '==', user['username']).get()
	reservs = []
	key_list = list(dict_service_id.keys())
	val_list = list(dict_service_id.values())
	for result in results:
		result = result.to_dict()
		position = val_list.index(result['serviceId'])
		serviceName = key_list[position]
		result['serviceId'] = serviceName
		result['url'], result['price'] = getUrlPrice(serviceName, result['serviceInfoId'])
		reservs.append(result)
	data = {
		'reservs': reservs,
		'user': user
	}
	context={'data': data}
	return render(request, 'user/profile.html', context)