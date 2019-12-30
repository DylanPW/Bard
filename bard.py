import playlistParser as p
import os
import ntpath
from pathlib import Path

def main():        
    filepath = Path(input("m3u playlist file location: "))
    destpath = Path(input("Destination Directory: "))
    relpath = ntpath.split(filepath)[0]
    playlist = p.load_m3u_playlist(filepath)    
    fullpath, playlist = p.verify_files(playlist, relpath)

    p.copy_file(fullpath, playlist, destpath, filepath)

if __name__=="__main__":
    main()