import pyrebase
config = {
    "apiKey": "AIzaSyB_jnpsPaxKs3xEhs-AbknZJXjcK-M4IeU",
    "authDomain": "water-meter-235712.firebaseapp.com",
    "databaseURL": "https://water-meter-235712.firebaseio.com",
    "projectId": "water-meter-235712",
    "storageBucket": "water-meter-235712.appspot.com",
    "messagingSenderId": "67042893322"   
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

alldata = db.child("room").get()
text_file = open('data_for_ocr.txt','w')

for data in alldata.each():
    print(data.key()) # Morty
    print(data.val())
    text_file.write('{} {}\n'.format(data.key(), data.val()))
text_file.close()
