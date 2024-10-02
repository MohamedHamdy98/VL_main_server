import streamlit as st
import requests

CHANGE_BG_API = "http://localhost:8000"
FACE_SWAP_API = "http://localhost:5000"
TRANSLATION_API = "http://localhost:5001"
LIP_SYNC_API =  "http://localhost:5004"

def post_change_bg(target_url, background_url):
    url = f"{CHANGE_BG_API}/change_background"
    data = {'target_url': target_url, 'background_url': background_url}
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()

def post_face_swap(video_url, source_url):
    url = f"{FACE_SWAP_API}/face_swap"
    data = {'video_url': video_url, 'source_url': source_url}
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()

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
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()

def post_lip_sync(face_url, audio_url, pads):
    url = f"{LIP_SYNC_API}/lip_sync"
    data = {'face_url': face_url, 'audio_url': audio_url, 'pads': pads}
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()

st.title("Video Processing Tool")

# Operation 1: Change Background
st.header("Change Background")
target_video = st.text_input("Target Video URL")
background_image = st.text_input("Background Image URL")
if st.button("Change Background"):
    result = post_change_bg(target_video, background_image)
    st.write("Output Paths:")
    st.write(result)

# Operation 2: Face Swap
st.header("Face Swap")
video_url = st.text_input("Video URL for Face Swap")
source_image = st.text_input("Source Image URL")
if st.button("Face Swap"):
    result = post_face_swap(video_url, source_image)
    st.write("Output Paths:")
    st.write(result)

# Operation 3: Translation
st.header("Translation")
prompt = st.text_input("Translation Prompt")
language = st.text_input("Source Language")
trans_lang = st.text_input("Target Language")
audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav"])
mic_file = st.file_uploader("Upload Microphone File", type=["mp3", "wav"])
use_mic = st.checkbox("Use Microphone")
voice_cleanup = st.checkbox("Voice Cleanup")
no_lang_auto_detect = st.checkbox("No Language Auto Detect")

if st.button("Translate"):
    audio_file_path = audio_file.name if audio_file else ""
    mic_file_path = mic_file.name if mic_file else ""
    result = post_translation(prompt, language, trans_lang, audio_file_path, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect)
    st.write("Translation Output Path:")
    st.write(result)

# Operation 4: Lip Sync
st.header("Lip Sync")
face_video_url = st.text_input("Face Video URL")
audio_url = st.text_input("Audio URL")
pads = st.text_input("Padding Values (comma-separated)", "0,0,0")
if st.button("Lip Sync"):
    pads_list = list(map(int, pads.split(',')))
    result = post_lip_sync(face_video_url, audio_url, pads_list)
    st.write("Lip Sync Output Path:")
    st.write(result)

# # Operation 5: Combined Operations (Face Swap, Change Background, and Translation)
# st.header("Combined Operations")
# if st.button("Face Swap, Change Background and Translate"):
#     face_swap_bg_trans_result = faceSwap_changeBg_translation_lipSync(video_url, source_image, background_image, prompt, language, trans_lang, audio_file_path, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect, pads_list)
#     st.write("Combined Operation Output Path:")
#     st.write(face_swap_bg_trans_result)
