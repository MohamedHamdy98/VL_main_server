import requests
import gradio as gr

CHANGE_BG_API = "http://0.0.0.0:8000"
FACE_SWAP_API = "http://0.0.0.0:5000"
TRANSLATION_API = "http://0.0.0.0:5001"
LIP_SYNC_API = "http://0.0.0.0:5004"

def post_change_bg(target_url, background_url):
    url = f"{CHANGE_BG_API}/change_background"
    data = {'target_url': target_url, 'background_url': background_url}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def post_face_swap(video_url, source_url):
    url = f"{FACE_SWAP_API}/face_swap"
    data = {'video_url': video_url, 'source_url': source_url}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def post_translation(prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect):
    url = f"{TRANSLATION_API}/translate"
    data = {
        'prompt': prompt,
        'language': language,
        'trans_lang': trans_lang,
        'audio_file_pth': audio_file_pth,
        'mic_file_path': mic_file_path,
        'use_mic': use_mic,
        'voice_cleanup': voice_cleanup,
        'no_lang_auto_detect': no_lang_auto_detect
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def post_lip_sync(face_url, audio_url, pads):
    url = f"{LIP_SYNC_API}/lip_sync"
    data = {'face_url': face_url, 'audio_url': audio_url, 'pads': pads}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Gradio Interfaces
with gr.Blocks() as app:
    gr.Markdown("## Video Processing API")

    with gr.Tab("Change Background"):
        target_url = gr.Textbox(label="Target Video URL")
        background_url = gr.Textbox(label="Background Image URL")
        change_bg_btn = gr.Button("Change Background")
        change_bg_output = gr.JSON(label="Output")
        change_bg_btn.click(fn=post_change_bg, inputs=[target_url, background_url], outputs=change_bg_output)

    with gr.Tab("Face Swap"):
        video_url = gr.Textbox(label="Video URL")
        source_url = gr.Textbox(label="Source Image URL")
        face_swap_btn = gr.Button("Swap Faces")
        face_swap_output = gr.JSON(label="Output")
        face_swap_btn.click(fn=post_face_swap, inputs=[video_url, source_url], outputs=face_swap_output)

    with gr.Tab("Translation"):
        prompt = gr.Textbox(label="Text to Translate")
        language = gr.Textbox(label="Source Language")
        trans_lang = gr.Textbox(label="Target Language")
        audio_file_pth = gr.Textbox(label="Audio File Path")
        mic_file_path = gr.Textbox(label="Mic File Path")
        use_mic = gr.Checkbox(label="Use Mic")
        voice_cleanup = gr.Checkbox(label="Voice Cleanup")
        no_lang_auto_detect = gr.Checkbox(label="Disable Auto Language Detection")
        translate_btn = gr.Button("Translate")
        translate_output = gr.JSON(label="Output")
        translate_btn.click(fn=post_translation, inputs=[prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect], outputs=translate_output)

    with gr.Tab("Lip Sync"):
        face_video_url = gr.Textbox(label="Face Video URL")
        audio_url = gr.Textbox(label="Audio URL")
        pads = gr.Textbox(label="Pads (comma separated)")
        lip_sync_btn = gr.Button("Lip Sync")
        lip_sync_output = gr.JSON(label="Output")
        lip_sync_btn.click(fn=post_lip_sync, inputs=[face_video_url, audio_url, pads], outputs=lip_sync_output)

app.launch()
