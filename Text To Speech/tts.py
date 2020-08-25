import pyttsx3

engine = pyttsx3.init()

engine.say("Hello Kevin. I am Hades!")

engine.runAndWait()

voices = engine.getProperty('voices')

for voice in voices:
	#if voice.gender == "male":
		# to get the info. about various voices in our PC
	print("Voice:")
	print("ID: %s" %voice.id)
	print("Name: %s" %voice.name)
	print("Age: %s" %voice.age)
	print("Gender: %s" %voice.gender)
	print("Languages Known: %s" %voice.languages)