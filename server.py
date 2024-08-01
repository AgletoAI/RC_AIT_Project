from flask import Flask, request, send_from_directory
from pydub import AudioSegment
from speech_to_text import transcribe_audio
from chatbot import Chatbot
import os

app = Flask(__name__)
bot = Chatbot()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return {"error": "No file part"}, 400
    
    audio_file = request.files['file']
    
    if audio_file.filename == '':
        return {"error": "No selected file"}, 400

    # Save the file temporarily
    temp_filename = "temp_audio_file"
    audio_file.save(temp_filename)
    
    # Convert to WAV if necessary
    converted_filename = "converted_audio_file.wav"
    try:
        file_type = audio_file.content_type
        
        if file_type not in ["audio/wav", "audio/x-wav"]:
            # Load the audio file with pydub
            audio = AudioSegment.from_file(temp_filename)
            audio.export(converted_filename, format="wav")
        else:
            # Rename the file if it's already in WAV format
            os.rename(temp_filename, converted_filename)
        
        text = transcribe_audio(converted_filename)
        response = bot.respond(text)
        return {"text": response}
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        # Cleanup the temporary files
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        if os.path.exists(converted_filename):
            os.remove(converted_filename)

@app.route('/favicon.ico')
def favicon():
    return "", 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
