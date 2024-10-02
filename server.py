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
    """
    Sends a request to change the background of a video.

    Parameters:
        target_url (str): URL of the video to change the background.
        background_url (str): URL of the background image.

    Returns:
        tuple: Paths of the video input, image background, and output.
    """
    url = f"{CHANGE_BG_API}/change_background"
    data = {
        'target_url': target_url,
        'background_url': background_url
    }
    try:
        response = requests.post(url, json=data)  # Send POST request
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response
        video_input_path = data.get('video_input')
        image_back_path = data.get('image_back')
        output_path = data.get('output_path')
        
        # Log the paths for debugging purposes
        print(f"Video Input Path: {video_input_path}")
        print(f"Image Background Path: {image_back_path}")
        print(f"Output Path: {output_path}")
        
        return video_input_path, image_back_path, output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during background change: {e}")  # Handle request errors


def post_face_swap(video_url, source_url):
    """
    Sends a request to perform face swapping in a video.

    Parameters:
        video_url (str): URL of the video to swap faces in.
        source_url (str): URL of the source image for face swapping.

    Returns:
        tuple: Paths of the video input, image input, and output.
    """
    url = f"{FACE_SWAP_API}/face_swap"
    data = {
        'video_url': video_url,
        'source_url': source_url
    }
    try:
        response = requests.post(url, json=data)  # Send POST request
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response
        video_input_path = data.get('video_input')
        image_input_path = data.get('image_input')
        output_path = data.get('output_path')
        
        # Log the paths for debugging purposes
        print(f"Video Input Path: {video_input_path}")
        print(f"Image Input Path: {image_input_path}")
        print(f"Output Path: {output_path}")
        
        return video_input_path, image_input_path, output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during face swap: {e}")  # Handle request errors


def post_translation(prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect):
    """
    Sends a request to translate audio and text.

    Parameters:
        prompt (str): The text to translate.
        language (str): The source language.
        trans_lang (str): The target language.
        audio_file_pth (str): Path to the audio file.
        mic_file_path (str): Path to the microphone file.
        use_mic (bool): Whether to use the microphone.
        voice_cleanup (bool): Whether to clean up the voice.
        no_lang_auto_detect (bool): Disable automatic language detection.

    Returns:
        str: Filename of the translated output.
    """
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
        response = requests.post(url, json=data)  # Send POST request
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response
        filename = data.get('filename')
        
        # Log the filename for debugging purposes
        print(f"Filename: {filename}")
        
        return filename
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during translation: {e}")  # Handle request errors


def post_lip_sync(face_url, audio_url, pads):
    """
    Sends a request to perform lip-syncing with a given face and audio.

    Parameters:
        face_url (str): URL of the face video.
        audio_url (str): URL of the audio file.
        pads (list): List of padding values.

    Returns:
        str: Path of the output video.
    """
    url = f"{LIP_SYNC_API}/lip_sync"
    data = {
        'face_url': face_url,
        'audio_url': audio_url,
        'pads': pads
    }
    try:
        response = requests.post(url, json=data)  # Send POST request
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse the JSON response
        output_path = data.get('output_path')
        
        # Log the output path for debugging purposes
        print(f"Output Path: {output_path}")
        
        return output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during lip sync: {e}")  # Handle request errors

""" 

GET Functionality...

"""
def get_face_swap():
    """
    Fetches paths related to the face swap operation.

    Returns:
        tuple: Paths of the video input, image background, and output.
    """
    # Fetch the paths directly from the face swap service
    url = f"{FACE_SWAP_API}/get_path_face_swap"
    try:
        response = requests.get(url)  # Send GET request
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        data = response.json()
        face_swap_video_input_path = data.get('video_input')
        face_swap_image_back_path = data.get('image_input')
        face_swap_output_path = data.get('output_path')
        
        # Log the paths for debugging purposes
        print(f"Video Input Path: {face_swap_video_input_path}")
        print(f"Image Background Path: {face_swap_image_back_path}")
        print(f"Output Path: {face_swap_output_path}")
        
        return face_swap_video_input_path, face_swap_image_back_path, face_swap_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during face swap retrieval: {e}")  # Handle request errors

def get_change_background():
    """
    Fetches paths related to the change background operation.

    Returns:
        tuple: Paths of the video input, image background, and output.
    """
    # Fetch the paths directly from the change background service
    url = f"{CHANGE_BG_API}/get_path_change_bg"
    try:
        response = requests.get(url)  # Send GET request
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        data = response.json()
        change_background_video_input_path = data.get('video_input')
        change_background_image_back_path = data.get('image_back')
        change_background_output_path = data.get('output_path')
        
        # Log the paths for debugging purposes
        print(f"Video Input Path: {change_background_video_input_path}")
        print(f"Image Background Path: {change_background_image_back_path}")
        print(f"Output Path: {change_background_output_path}")
        
        return change_background_video_input_path, change_background_image_back_path, change_background_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during change background retrieval: {e}")  # Handle request errors


def get_translation():
    """
    Fetches the path related to the translation output.

    Returns:
        str: Path of the translation output.
    """
    # Fetch the paths directly from the translation service
    url = f"{TRANSLATION_API}/get_path_translated"
    try:
        response = requests.get(url)  # Send GET request
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        data = response.json()
        translation_output_path = data.get('output_path')
        
        # Log the output path for debugging purposes
        print(f"Output Path: {translation_output_path}")
        
        return translation_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during translation retrieval: {e}")  # Handle request errors

def get_lip_sync():
    """
    Fetches the path related to the lip sync output.

    Returns:
        str: Path of the lip sync output.
    """
    # Fetch the paths directly from the lip sync service
    url = f"{LIP_SYNC_API}/get_path_lip_sync"
    try:
        response = requests.get(url)  # Send GET request
        response.raise_for_status()  # Raise an error for bad responses
        
        # Parse the JSON response
        data = response.json()
        lip_sync_output_path = data.get('output_path')
        
        # Log the output path for debugging purposes
        print(f"Output Path: {lip_sync_output_path}")
        
        return lip_sync_output_path
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during lip sync retrieval: {e}")  # Handle request errors


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


if __name__ == "__main__":
    # Example usage of the functions
    # Adjust the following calls based on your actual data and requirements

    # Change background
    target_video_url = "http://example.com/video.mp4"
    background_image_url = "http://example.com/background.jpg"
    post_change_bg(target_video_url, background_image_url)

    # Face swap
    video_url_for_face_swap = "http://example.com/face_swap_video.mp4"
    source_image_url = "http://example.com/source_image.jpg"
    post_face_swap(video_url_for_face_swap, source_image_url)

    # Translation
    prompt_text = "Hello, how are you?"
    source_language = "en"
    target_language = "es"
    audio_path = "path/to/audio/file"
    mic_path = "path/to/mic/file"
    use_mic = False
    voice_cleanup = True
    disable_lang_detect = True
    post_translation(prompt_text, source_language, target_language, audio_path, mic_path, use_mic, voice_cleanup, disable_lang_detect)

    # Lip sync
    face_video_url = "http://example.com/face_video.mp4"
    audio_file_url = "http://example.com/audio.mp3"
    pads = [0, 0, 0, 0]  # Example padding values
    post_lip_sync(face_video_url, audio_file_url, pads)

    # Get paths
    get_face_swap()
    get_change_background()
    get_translation()
    get_lip_sync()