import requests
import gradio as gr

CHANGE_BG_API = "http://localhost:5005"
FACE_SWAP_API = "http://0.0.0.0:5000"
TRANSLATION_API = "http://0.0.0.0:5001"
LIP_SYNC_API = "http://0.0.0.0:5004"

# Google Drive video and image links
video_links = [
    "https://drive.google.com/file/d/1hdyAPIicqd7JR2R_k36aBx3XXBP6CdIp/view?usp=sharing",
    "https://drive.google.com/file/d/14vxcRAe9RFbw2bPQGQbAzzzmwJt2hcTH/view?usp=sharing"
]

image_links = [
    "https://drive.google.com/file/d/1vcJ0M8rWrDGeBvNLxFyXKtu8ql1imIsn/view?usp=sharing",
    "https://drive.google.com/file/d/1VzE-euWXdIJCrn-pIKZSHt3moJ1c6GLd/view?usp=sharing"
]

def get_direct_link(drive_link):
    # Extract the file ID from the Google Drive link
    file_id = drive_link.split('/d/')[1].split('/')[0]
    return f"https://drive.google.com/uc?id={file_id}"

# API call functions
def post_change_bg(target_url, background_url):
    url = f"{CHANGE_BG_API}/change_background"
    data = {'target_url': target_url, 'background_url': background_url}
    try:
        response = requests.post(url, data=data)
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

# Dropdown selection handling
def choose_video(video_url):
    direct_link = get_direct_link(video_url)  # Convert to direct link
    return direct_link, direct_link  # Return the URL for display

def choose_image(image_url):
    direct_link = get_direct_link(image_url)  # Convert to direct link
    return direct_link, direct_link  # Return the URL for display

# Gradio Interfaces
with gr.Blocks() as app:
    gr.Markdown("## Video Processing API")

    # Dropdown for Google Drive Video and Image Selection
    with gr.Tab("Google Drive Files"):
        gr.Markdown("### Select a Video from Google Drive")
        video_dropdown = gr.Dropdown(label="Videos", choices=video_links)
        video_output = gr.Textbox(label="Selected Video URL", interactive=False)
        video_display = gr.Video(label="Video Preview")  # Display for selected video
        video_button = gr.Button("Select Video")
        video_button.click(fn=choose_video, inputs=video_dropdown, outputs=[video_output, video_display])

        gr.Markdown("### Select an Image from Google Drive")
        image_dropdown = gr.Dropdown(label="Images", choices=image_links)
        image_output = gr.Textbox(label="Selected Image URL", interactive=False)
        image_display = gr.Image(label="Image Preview")  # Display for selected image
        image_button = gr.Button("Select Image")
        image_button.click(fn=choose_image, inputs=image_dropdown, outputs=[image_output, image_display])

    # Change Background Tab
    with gr.Tab("Change Background"):
        target_url = gr.Textbox(label="Target Video URL")
        background_url = gr.Textbox(label="Background Image URL")
        change_bg_btn = gr.Button("Change Background")
        change_bg_output = gr.JSON(label="Output")
        change_bg_btn.click(fn=post_change_bg, inputs=[target_url, background_url], outputs=change_bg_output)

    # Face Swap Tab
    with gr.Tab("Face Swap"):
        video_url = gr.Textbox(label="Video URL")
        source_url = gr.Textbox(label="Source Image URL")
        face_swap_btn = gr.Button("Swap Faces")
        face_swap_output = gr.JSON(label="Output")
        face_swap_btn.click(fn=post_face_swap, inputs=[video_url, source_url], outputs=face_swap_output)

    # Translation Tab
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

    # Lip Sync Tab
    with gr.Tab("Lip Sync"):
        face_video_url = gr.Textbox(label="Face Video URL")
        audio_url = gr.Textbox(label="Audio URL")
        pads = gr.Textbox(label="Pads (comma separated)")
        lip_sync_btn = gr.Button("Lip Sync")
        lip_sync_output = gr.JSON(label="Output")
        lip_sync_btn.click(fn=post_lip_sync, inputs=[face_video_url, audio_url, pads], outputs=lip_sync_output)

# Launch the app
app.launch()
