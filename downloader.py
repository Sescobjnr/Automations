import yt_dlp
import sys
import os

def download_video(url, output_path='.'):
    """
    Downloads a video from a given URL using yt-dlp.
    """
    ydl_opts = {
        'format': 'best',  # Download best single file (avoids ffmpeg merge requirement)
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'), # Output filename template
        'noplaylist': True, # Download only single video
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print("\nDownload completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        # Check if the argument is a file
        if os.path.isfile(arg):
            print(f"Reading links from file: {arg}")
            try:
                with open(arg, 'r') as f:
                    links = [line.strip() for line in f if line.strip()]
                
                print(f"Found {len(links)} links to download.")
                
                for i, link in enumerate(links, 1):
                    print(f"\n--- Processing link {i}/{len(links)} ---")
                    download_video(link)
                    
                print("\nBatch download finished.")
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            # Treat argument as a single URL
            download_video(arg)
    else:
        print("Usage: python downloader.py <video_url_or_file_path>")
        # Optional: Interactive mode if no argument provided
        user_input = input("Enter the video URL or file path: ").strip()
        if user_input:
             if os.path.isfile(user_input):
                 # Handle file input in interactive mode too
                try:
                    with open(user_input, 'r') as f:
                        links = [line.strip() for line in f if line.strip()]
                    print(f"Found {len(links)} links to download.")
                    for i, link in enumerate(links, 1):
                        print(f"\n--- Processing link {i}/{len(links)} ---")
                        download_video(link)
                    print("\nBatch download finished.")
                except Exception as e:
                    print(f"Error reading file: {e}")
             else:
                download_video(user_input)
