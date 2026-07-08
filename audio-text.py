import whisper
import gradio as gr
model=whisper.load_model("base")
def speech_to_text(Audiofile):
  result=model.transcribe("AudioFile")
  return result
demo=gr.Interface(
      fn=speech_to_text,
      inputs=gr.Audio(type="filepath"),
      outputs=gr.Textbox(),
      title="speech_to_text"
  )
demo.launch()
