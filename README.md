# Youtube_Video_Downloader

This Python application provides a simple graphical user interface (GUI) for downloading YouTube videos and audio using `yt-dlp`. It allows users to select video resolutions, download audio-only, and track download progress.

## Features

* **Download YouTube Videos:** Downloads videos in various resolutions (highest, lowest, 1080p, 720p, etc.).
* **Audio-Only Downloads:** Extracts and downloads audio from YouTube videos.
* **Resolution Selection:** Allows users to choose the desired video resolution.
* **Progress Tracking:** Displays download progress with a progress bar and percentage indicator.
* **User-Friendly GUI:** Simple and intuitive graphical interface using Tkinter.
* **Cross-Platform:** Should work on any system with Python and Tkinter installed.
* **Uses yt-dlp:** Utilizes the robust and actively maintained yt-dlp library.

## Prerequisites

* Python 3.x
* `yt-dlp` (install with `pip install yt-dlp`)
* Tkinter (usually included with Python)

## Installation

1.  **Install `yt-dlp`:**

    ```bash
    pip install yt-dlp
    ```

2.  **Clone or download the repository:**

    ```bash
    git clone [repository URL]
    ```

3.  **Run the application:**

    ```bash
    python youtube_downloader_yt_dlp.py
    ```

## Usage

1.  Enter the YouTube video URL in the provided field.
2.  Select the desired video resolution from the dropdown menu.
3.  Check the "Audio Only" box if you want to download only the audio.
4.  Click the "Download" button.
5.  Choose the output directory where you want to save the downloaded file.
6.  The download progress will be displayed in the progress bar and percentage label.
7.  A status message will indicate the download status.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Description for GitHub

This Python application provides a user-friendly GUI for downloading YouTube videos and audio using the powerful `yt-dlp` library. It allows users to easily select video resolutions, download audio-only, and track download progress in real-time. This project aims to provide a reliable and convenient way to download YouTube content for personal use. It leverages the robustness of `yt-dlp` for efficient and up-to-date downloading capabilities, while providing a simple Tkinter interface for ease of use.
