from django.shortcuts import render

clients = [
	{
		'profile_pic': 'https://www.thefamouspeople.com/profiles/images/emma-watson-8.jpg',
		'name': 'Emma Watson',
		'address': 'Lucap, Alaminos City, Pangasinan',
		'contact_no': '09155316311',
		'gender': 'Female'
	},
	{
		'profile_pic': 'https://www.thefamouspeople.com/profiles/images/emma-watson-8.jpg',
		'name': 'Emma Watson',
		'address': 'Lucap, Alaminos City, Pangasinanadfasdfasdfasdfasdfadfasdfasdfasdfadfadfadfadsfadsf',
		'contact_no': '09155316311',
		'gender': 'Female'
	},
	{
		'profile_pic': 'https://www.thefamouspeople.com/profiles/images/emma-watson-8.jpg',
		'name': 'Emma Watson',
		'address': 'Lucap, Alaminos City, Pangasinan',
		'contact_no': '09155316311',
		'gender': 'Female'
	},
	{
		'profile_pic': 'https://www.thefamouspeople.com/profiles/images/emma-watson-8.jpg',
		'name': 'Emma Watson',
		'address': 'Lucap, Alaminos City, Pangasinan',
		'contact_no': '09155316311',
		'gender': 'Female'
	},
	{
		'profile_pic': 'https://www.thefamouspeople.com/profiles/images/emma-watson-8.jpg',
		'name': 'Emma Watson',
		'address': 'Lucap, Alaminos City, Pangasinan',
		'contact_no': '09155316311',
		'gender': 'Female'
	},
	{
		'profile_pic': 'https://www.thefamouspeople.com/profiles/images/emma-watson-8.jpg',
		'name': 'john michael fernandezasdfadfadsfasdf',
		'address': 'Lucap, Alaminos City, Pangasinan',
		'contact_no': '09155316311',
		'gender': 'Female'
	}
]

def home(request):
	context = {
		'clients': clients,
	}
	return render(request, 'clients/home.html', context)
