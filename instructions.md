# Video Processing API Client

This module provides a client for interacting with various video processing APIs. It includes functionalities for changing backgrounds, swapping faces, translating audio, and lip-syncing videos. Each operation corresponds to a specific API endpoint and allows users to send requests and receive processed outputs.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
    - [post_change_bg](#post_change_bg)
    - [post_face_swap](#post_face_swap)
    - [post_translation](#post_translation)
    - [post_lip_sync](#post_lip_sync)
    - [get_face_swap](#get_face_swap)
    - [get_change_background](#get_change_background)
    - [get_translation](#get_translation)
    - [get_lip_sync](#get_lip_sync)
- [Example](#example)
- [Error Handling](#error-handling)

## Installation

Ensure you have the `requests` library installed to make API calls. You can install it using pip:

```bash
pip install requests
Usage
To use this module, import it into your Python script and call the functions with appropriate parameters. Make sure your video processing APIs are running and accessible at the specified endpoints.

Functions
post_change_bg(target_url, background_url)
Sends a request to change the background of a video.

Parameters:

target_url (str): URL of the video to change the background.
background_url (str): URL of the background image.
Returns:

tuple: Paths of the video input, image background, and output.
post_face_swap(video_url, source_url)
Sends a request to perform face swapping in a video.

Parameters:

video_url (str): URL of the video to swap faces in.
source_url (str): URL of the source image for face swapping.
Returns:

tuple: Paths of the video input, image input, and output.
post_translation(prompt, language, trans_lang, audio_file_pth, mic_file_path, use_mic, voice_cleanup, no_lang_auto_detect)
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
post_lip_sync(face_url, audio_url, pads)
Sends a request to perform lip-syncing with a given face and audio.

Parameters:

face_url (str): URL of the face video.
audio_url (str): URL of the audio file.
pads (list): List of padding values.
Returns:

str: Path of the output video.
get_face_swap()
Fetches paths related to the face swap operation.

Returns:

tuple: Paths of the video input, image background, and output.
get_change_background()
Fetches paths related to the change background operation.

Returns:

tuple: Paths of the video input, image background, and output.
get_translation()
Fetches the path related to the translation output.

Returns:

str: Path of the translation output.
get_lip_sync()
Fetches the path related to the lip sync output.

Returns:

str: Path of the lip sync output.
Example
Here's an example of how to use the functions defined in this module:

python
Copy code
# Change background
bg_video_url = "http://example.com/video.mp4"
bg_image_url = "http://example.com/background.jpg"
video_input, image_back, output_path = post_change_bg(bg_video_url, bg_image_url)

# Face swap
swap_video_url = "http://example.com/face_swap_video.mp4"
source_image_url = "http://example.com/source_image.jpg"
video_input, image_input, output_path = post_face_swap(swap_video_url, source_image_url)

# Translation
prompt_text = "Hello, how are you?"
source_lang = "en"
target_lang = "es"
audio_file_path = "path/to/audio/file"
mic_file_path = "path/to/mic/file"
use_mic = False
voice_cleanup = True
disable_lang_detect = True
translated_filename = post_translation(prompt_text, source_lang, target_lang, audio_file_path, mic_file_path, use_mic, voice_cleanup, disable_lang_detect)

# Lip sync
face_video_url = "http://example.com/face_video.mp4"
audio_file_url = "http://example.com/audio.mp3"
pads = [0, 0, 0, 0]  # Example padding values
lip_sync_output_path = post_lip_sync(face_video_url, audio_file_url, pads)

# Get paths
face_swap_paths = get_face_swap()
bg_change_paths = get_change_background()
translation_path = get_translation()
lip_sync_path = get_lip_sync()