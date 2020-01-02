import os
import ntpath
from pathlib import Path, PureWindowsPath, PurePath
import re
import shutil

def valid_m3u_playlist(filepath):
    """ validates if the playlist is an acceptable *.m3u playlist file

    Args:
        filepath (Path): The path to the playlist file

    Returns:
        bool : True if the file is valid, False otherwise  

    """
    if (Path(filepath).exists() and filepath.lower().endswith('.m3u')):
        return True
    return False

def load_m3u_playlist(filepath):
    """ loads a *.m3u playlist file

    Args:
        filepath (Path): The path to the playlist file

    Returns:
        playlist (string list): the list of paths to the audio files    
    """
    with open(filepath, "r") as file:
        playlist = []
        for line in file:
            if(not line.startswith('#')):
                playlist.append(line.rstrip())
    return playlist

def verify_files(playlist, playlistpath):
    """ verifies if the original files exist

    Args:
        playlist (string list): the list of paths to the audio files    

    Returns:
        playlist (string list): the list of file paths that exist
    """
    returnlist = []
    returnplaylist = []
    playlistpath = Path(playlistpath)
    for i in playlist:
        win_path = PureWindowsPath(i)
        f = playlistpath / win_path
        if(f.exists()):
            returnlist.append(f)
            returnplaylist.append(Path(win_path))
    return returnlist, returnplaylist

def get_folder(sourcepath):
    """ outputs the file names from a path

    Args:
        sourcepath (string): the path to the file

    Returns:
        string: the folder containing the file
    """
    return Path(sourcepath).parents[0]

def create_folders(playlist, destpath):
    """ creates the file structure required

    Args:
        sourcefile (Path list): List of the processed files in 
        destpath (string):

    """
    try:
        folders = []
        for file in playlist:
            temp = destpath / get_folder(file)
            if (temp not in folders):
                folders.append(temp)
        for folder in folders:
            if not (Path.exists(Path(folder))):
                folder.mkdir(parents=True, exist_ok=True)
        return True
    except:
        return False

def get_relative_folder(file, playlistloc):
    """ gets the file folder relative to the playlist location

    Args:
        file (string): path to the file
        playlistloc (string): path to the playlist file
    
    Returns:
        string: the relative path between the two locations
    """
    return get_folder(file).relative_to(playlistloc)

def get_relpath(path):
    """ gets the relative path without file

    Args:
        path (string): path to the file
            
    Returns:
        string: the relative path
    """
    return ntpath.split(path)[0]

def copy_playlist_file(playlist, destpath):
    """ Copies the playlist file to the chosen directory

    Args:
        playlist (string): Path to the playlist file
        destpath (string): Path to the destination folder
    """
    Path(destpath).mkdir(parents=True, exist_ok=True)
    shutil.copy2(playlist, destpath)

def copy_file(file, destpath, playlistfile):
    """ Copies the file to the destination folder

    Args:
        file (string): the path to the file to be copied
        destpath (string): Path to the destination folder
        playlistfile (string): Path to the playlist file
    """
    playlistloc = PurePath(get_folder(playlistfile))
    loc = get_folder(file).relative_to(playlistloc)
    shutil.copy2(file, destpath / loc)

def output_filename(filepath):
    """ outputs the file names from a path

    Args:
        filepath (string): the path to the file   

    Returns:
        filename (string): the filename  
    """
    return ntpath.split(filepath)[1]


def output_filenames_from_list(playlist):
    """ outputs the file names from a playlist

    Args:
        playlist (string list): the list of paths to the audio files    

    Returns:
        filenames (string list): the list of filenames   
    """

    filenames = []
    for filepath in playlist:
        filenames.append(output_filename(filepath))
    return filenames
