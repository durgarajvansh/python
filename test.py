import os
from gtts import gTTS
myText='abhishek kothawala '
language = 'en'        
myProject = gTTS(text=myText,lang = language,slow=False)       
myProject.save('welcome.mp3')
os.system('welcome.mp3')
