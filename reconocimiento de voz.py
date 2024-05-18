import speech_recognition as sr

def Voice_recog():
    reconocedor = sr.Recognizer()
    microfono = sr.Microphone()
    try:
        print("di algo")
        
        with microfono as source:
            reconocedor.adjust_for_ambient_noise(source)
            audio = reconocedor.listen(source)
        
        return reconocedor.recognize_google(audio, language= 'ES')

    except sr.UnknownValueError:
      print('No entendí lo que dijiste')
    
    except sr.RequestError:
        print("Error, no pude conectarme al servicio")


print("dijiste: ", {Voice_recog})