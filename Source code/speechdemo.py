import azure.cognitiveservices.speech as speechsdk
import keys

speech_config = speechsdk.SpeechConfig(subscription=keys.speechKey, region=keys.region)
# Set up Azure Text-to-Speech language 
speech_config.speech_synthesis_language = keys.language
# Set up Azure Speech-to-Text language recognition
speech_config.speech_recognition_language =keys.language

# Set up the voice configuration
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def speech_to_text():
    # Set up the audio configuration
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Create a speech recognizer and start the recognition
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("I am listening")

    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "Sorry, I didn't catch that."
    elif result.reason == speechsdk.ResultReason.Canceled:
        return "Recognition canceled."


def text_to_speech(text):
    try:
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Text-to-speech conversion successful.")
            return True
        else:
            print(f"Error synthesizing audio: {result}")
            return False
    except Exception as ex:
        print(f"Error synthesizing audio: {ex}")
        return False
