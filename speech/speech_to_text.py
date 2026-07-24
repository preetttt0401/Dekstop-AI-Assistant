import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

from utils.config import SAMPLE_RATE, WHISPER_MODEL
from utils.logger import logger


class SpeechToText:
    """
    Handles recording audio from the microphone and
    converting speech into text using Faster-Whisper.
    """

    def __init__(self):
        logger.info("Loading Faster-Whisper model...")

        self.model = WhisperModel(
            WHISPER_MODEL,
            device="cpu",
            compute_type="int8"
        )

        logger.info("Speech-to-Text module initialized.")

    def record_audio(self, filename="audio.wav", duration=5):
        """
        Record audio from the microphone.
        """

        logger.info("Recording started...")

        print("\n🎤 Speak now...\n")

        recording = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        write(filename, SAMPLE_RATE, recording)

        logger.info(f"Audio saved as {filename}")

        return filename

    def transcribe_audio(self, filename):
        """
        Convert audio into text.
        """

        logger.info("Transcribing audio...")

        segments, info = self.model.transcribe(
            filename,
            beam_size=5,
            vad_filter=True
        )

        text = ""

        for segment in segments:
            text += segment.text

        text = text.strip()

        logger.info(f"Recognized Text: {text}")

        return text

    def listen(self, duration=5):
        """
        Records audio and immediately converts it to text.
        """

        audio_file = self.record_audio(duration=duration)

        return self.transcribe_audio(audio_file)