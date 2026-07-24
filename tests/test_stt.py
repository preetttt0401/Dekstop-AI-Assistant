from speech.speech_to_text import SpeechToText

stt = SpeechToText()

audio_file = stt.record_audio()

text = stt.transcribe_audio(audio_file)

print("\nRecognized Text:")
print(text)