import speech_recognition as sr 
from speak import speak



def speak_back(language):
	sample_rate = 48000
	#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
	#here.  
	#it is advisable to use powers of 2 such as 1024 or 2048 
	chunk_size = 2048
	#Initialize the recognizer 
	r = sr.Recognizer() 
	  

	#which device ID to specifically look for incase the microphone  
	#is not working, an error will pop up saying "device_id undefined" 
	with sr.Microphone(device_index = 11, sample_rate = sample_rate, chunk_size = chunk_size) as source: 
		#wait for a second to let the recognizer adjust the  
		#energy threshold based on the surrounding noise level 
		r.adjust_for_ambient_noise(source) 
		print ("Say Something")
		if language == 'en':
			speak("Say Something",language)
		elif language == 'no':
			speak('Si noe',language)
            
		#listens for the user's input 
		audio = r.listen(source) 
		  
	try:
		l = language
		text = r.recognize_google(audio, language=l) 
		print ("you said: " + text)
		speak(text,l)     
		#error occurs when google could not understand what was said   
	except sr.UnknownValueError: 
		print("Google Speech Recognition could not understand audio")
     
	except sr.RequestError as e: 
		print('kunne ikke hente reultater fra google')
		#print("Could not request results from Google  Speech Recognition service; {0}".format(e))


