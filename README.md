# Bard ![Bard](32.png "logo")
## Playlist Copy Assistant

A very basic script for copying the files specified in an *.m3u playlist to a specified directory. Features a qt5 based GUI using the fman build system. (https://build-system.fman.io/)

Many features are as of yet unimplemented and untested. What does work is;

- Loading a *.m3u playlist file with relative file paths (Absolute paths are not yet supported)
- Copying the playlist file and the relevant tracks to the specified directory. The folder structure specified in the original *.m3u file is maintained.
- Preview of the contents of the playlist on having a valid path entered.
- Status and Progressbars work
- Copying playlists with both absolute and relative paths to chosen directory works (at least with *.flac(s))
- Copying all selected tracks to a single playlist title folder.

Execute `Bard.exe` to run

## Requirements:
Requires Python 3.6 due to fbs limitations.
Uses PyQt5 version 5.9.2

Run `pip install -r requirements.txt` to install the requisite version of PyQt5

## Changelog:

### 0.3-pre
- Fixed bug with absolute paths and changed backend to convert to relative playlists automatically.
- Added merging all tracks to a single folder titled as the name of playlist (renaming playlist to come in future update)
- Added merging all tracks to a the same folder as the playlist

### 0.2-pre

- Added support for absolute paths and improved stability
- Added proper icon

### 0.1-pre

Very basic iteration of Bard, many features are as of yet unimplemented and untested. What does work is;

- Loading a *.m3u playlist file with relative file paths (Absolute paths are not yet supported)
- Copying the playlist file and the relevant tracks to the specified directory. The folder structure specified in the original *.m3u file is maintained.
- Preview of the contents of the playlist on having a valid path entered.
- Status and Progressbars work
- Copying of relative playlists to chosen directory works (at least with *.flac(s))

## Bugs:

- Having a playlist consisting of either a mixture of absolute and relative paths or absolute paths targetting multiple disks will not copy successfully and will stop at the verifying playlist step.

## Credits: 
Icon made by [smalllikeart](https://www.flaticon.com/authors/smalllikeart) from [www.flaticon.com](https://www.flaticon.com/)