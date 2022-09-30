from cryptography.fernet import Fernet
fname='test'
choice='e'
keygen='u'

def encrypt(a):
	intchoice=input('To use existing key file, press u, to generate new key, press g: ')
	if intchoice=='g':
		key = Fernet.generate_key()
		with open('thekey.key', 'wb') as k:
			k.write(key)
			print('Keyfile stored in working directory...')
	elif intchoice=='u':
		with open('thekey.key','rb') as k:
			key=k.read()
	with open(a,'rb') as f:
		contents = f.read()
	enc_cont = Fernet(key).encrypt(contents)
	with open(a,'wb') as f:
		f.write(enc_cont)

def decrypt(i):
	intchoice=input('To use existing key file, press u, to enter key code manually, press g: ')
	if intchoice=='g':
		key=input('ENTER KEY: ')
	elif intchoice=='u':
		with open('thekey.key', 'rb') as k:
			key=k.read()
	with open(i,'rb') as f:
		contents = f.read()
	dec_cont = Fernet(key).decrypt(contents)
	with open(i,'wb') as f:
		f.write(dec_cont)

def mainprog():
	fname=input('Enter filename with extension: ')
	choice=input('For encryption press e, for decryption press d: ')
	if choice=='e':
		encrypt(fname)
		print('DONE!')
	elif choice=='d':
		decrypt(fname)
		print('DONE!')
	else:
		print('Enter a valid choice!!!')

mainprog()
