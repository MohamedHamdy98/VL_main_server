import json
import requests

CHANGE_BG_API = "http://0.0.0.0:8000"
FACE_SWAP_API = "http://0.0.0.0:5000"
TRANSLATION_API = "http://0.0.0.0:5001"
LIP_SYNC_API =  "http://0.0.0.0:5004"

"""

operation 1 ==> create every tool alone

POST Functionality...

"""
def post_change_bg(target_url, background_url):
    url = f"{CHANGE_BG_API}/change_background"
    data = {
        'target_url': target_url,
        'background_url': background_url
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        data = response.json()
        video_input_path = data.get('video_input')
        image_back_path = data.get('image_back')
        output_path = data.get('output_path')
        print(f"Video Input Path: {video_input_path}")
        print(f"Image Background Path: {image_back_path}")
        print(f"Output Path: {output_path}")
        return video_input_path, image_back_path, output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during background change: {e}")

def post_face_swap(video_url, source_url):
    url = f"{FACE_SWAP_API}/face_swap"
    data = {
        'video_url': video_url,
        'source_url': source_url
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        data = response.json()
        video_input_path = data.get('video_input')
        image_input_path = data.get('image_input')
        output_path = data.get('output_path')
        print(f"Video Input Path: {video_input_path}")
        print(f"Image Input Path: {image_input_path}")
        print(f"Output Path: {output_path}")
        return video_input_path, image_input_path, output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during face swap: {e}")

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
        data = response.json()
        filename = data.get('filename')
        print(f"Filename: {filename}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during translation: {e}")

def post_lip_sync(face_url, audio_url, pads):
    url = f"{LIP_SYNC_API}/lip_sync"
    data = {
        'face_url': face_url,
        'audio_url': audio_url,
        'pads': pads
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        data = response.json()
        output_path = data.get('output_path')
        print(f"Output Path: {output_path}")
        return output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during lip sync: {e}")




def get_face_swap():
    # Fetch the paths directly from the change background service
    url = f"{FACE_SWAP_API}/get_path_face_swap"
    try:
        # Make a GET request to retrieve the paths
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        face_swap_video_input_path = data.get('video_input')
        face_swap_image_back_path = data.get('image_input')
        face_swap_output_path = data.get('output_path')
        
        # Print or use the file paths as needed
        print(f"Video Input Path: {face_swap_video_input_path}")
        print(f"Image Background Path: {face_swap_image_back_path}")
        print(f"Output Path: {face_swap_output_path}")
        
        # Return the paths for use in other operations
        return face_swap_video_input_path, face_swap_image_back_path, face_swap_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during background change: {e}")

def get_change_background():
    # Fetch the paths directly from the change background service
    url = f"{CHANGE_BG_API}/get_path_change_bg"
    try:
        # Make a GET request to retrieve the paths
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        change_background_video_input_path = data.get('video_input')
        change_background_image_back_path = data.get('image_back')
        change_background_output_path = data.get('output_path')
        
        # Print or use the file paths as needed
        print(f"Video Input Path: {change_background_video_input_path}")
        print(f"Image Background Path: {change_background_image_back_path}")
        print(f"Output Path: {change_background_output_path}")
        
        # Return the paths for use in other operations
        return change_background_video_input_path, change_background_image_back_path, change_background_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during background change: {e}")


def get_translation():
    # Fetch the paths directly from the change background service
    url = f"{TRANSLATION_API}/get_path_translated"
    try:
        # Make a GET request to retrieve the paths
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        translation_output_path = data.get('output_path')
        
        # Print or use the file paths as needed
        print(f"Output Path: {translation_output_path}")
        
        # Return the paths for use in other operations
        return translation_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during background change: {e}")

def get_lip_sync():
    url = f"{LIP_SYNC_API}/get_path_lip_sync"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('output_path')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching lip sync output path: {e}")

"""
operation 2 ==> create face swap and change background

"""
def face_swap_change_bg(video_url, source_url, background_url):
    # Step 1: Face Swap
    face_swap_result = post_face_swap(video_url, source_url)
    face_swap_output_path = get_face_swap()

    # Step 2: Change Background on the Face Swapped Video
    change_bg_result = post_change_bg(face_swap_output_path, background_url)
    change_bg_output_path = get_change_background()

    # Step 3: Return the output path of the video with changed background
    return change_bg_output_path

"""
operation 3 ==> Create Face Swap and Lip Sync

"""
def face_swap_lip_sync(video_url, source_url, audio_url, pads):
    # Step 1: Face Swap
    face_swap_result = post_face_swap(video_url, source_url)
    face_swap_output_path = get_face_swap()

    # Step 2: Lip Sync on the Face Swapped Video
    lip_sync_result = post_lip_sync(face_swap_output_path, audio_url, pads)
    lip_sync_output_path = get_lip_sync()

    # Step 3: Return the output path of the lip-synced video
    return lip_sync_output_path

"""
operation 4 ==> Create Face Swap, Change Background, and Translation

"""
def faceSwap_changeBg_translation(video_url, source_url, background_url, prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect):
    # Step 1: Face Swap
    face_swap_result = post_face_swap(video_url, source_url)
    face_swap_output_path = get_face_swap()

    # Step 2: Change Background
    change_bg_result = post_change_bg(face_swap_output_path, background_url)
    change_bg_output_path = get_change_background()

    # Step 3: Translation
    translation_result = post_translation(prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect)
    translation_output_path = get_translation()

    return change_bg_output_path, translation_output_path

""" 

operation 5 ==> create face_swap, change_background, translation and lip_sync

"""
def faceSwap_changeBg_translation_lipSync(video_url, source_url, background_url, prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect, pads):
    # Step 1: Face Swap
    video_input, image_input, face_swap_output_path = post_face_swap(video_url, source_url)

    # Step 2: Change Background on the Face Swapped Video
    video_input_bg, image_back_bg, change_bg_output_path = post_change_bg(face_swap_output_path, background_url)

    # Step 3: Perform Translation
    translation_filename = post_translation(prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect)
    translation_output_path = get_translation()

    # Step 4: Lip Sync with Translated Audio
    lip_sync_output_path = post_lip_sync(change_bg_output_path, translation_output_path, pads)

    return lip_sync_output_path
