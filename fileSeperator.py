import os
from pathlib import Path

SUBCATEGORIES = {
    'DOCUMENTS': ['.pdf', '.txt', '.doc', '.rtf', '.pptx', '.docx', '.odt'],
    'AUDIO': ['.mp3', '.m4b', '.m4a', '.webvtt', '.cea-608/708', '.dfxp', '.sami', '.scc', '.srt', '.ttml', '.3gpp'],
    'VIDEOS': ['.mov', '.avi', '.mp4', '.3gp', '.ogg', '.oga', '.ogv', '.ogx', '.wmv', '.webm', '.flv', '.avi', '.QuickTime', '.hdv', '.mxf', '.mpeg-2', '.ts', '.wav', '.lfx', '.gfx', '.vob'],
    'IMAGES': ['.jpg', '.jpeg', '.raw', '.png', '.tiff', '.gif'],
    'PROGRAMMING FILES': ['.htm', '.html', '.cpp', '.c', '.py', '.css', '.java']
}

def find_category(file_extension):
    for category, extensions in SUBCATEGORIES.items():
        if file_extension in extensions:
            return category
    return 'MISC'

def organize_directory():
    for item in os.scandir():
        if item.is_file():
            file_path = Path(item)
            file_extension = file_path.suffix.lower()
            category = find_category(file_extension)
            directory_path = Path(category)
            if not directory_path.is_dir():
                directory_path.mkdir()
            new_file_path = directory_path.joinpath(file_path.name)
            file_path.rename(new_file_path)

if __name__ == "__main__":
    organize_directory()
