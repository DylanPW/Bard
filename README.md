# Bard 
## Playlist Copy Assistant

A very basic script for copying the files specified in an *.m3u playlist to a specified directory. Features a qt5 based GUI using the fman build system. (https://build-system.fman.io/)

Many features are as of yet unimplemented and untested. What does work is;

- Loading a *.m3u playlist file with relative file paths (Absolute paths are not yet supported)
- Copying the playlist file and the relevant tracks to the specified directory. The folder structure specified in the original *.m3u file is maintained.
- Preview of the contents of the playlist on having a valid path entered.
- Status and Progressbars work

## Requirements:
Currently requires Python 3.6 due to fbs limitations.
Uses PyQt5 version 5.9.2

## Changelog:
### v0.1-pre

Very basic iteration of Bard, many features are as of yet unimplemented and untested. What does work is;

- Loading a *.m3u playlist file with relative file paths (Absolute paths are not yet supported)
- Copying the playlist file and the relevant tracks to the specified directory. The folder structure specified in the original *.m3u file is maintained.
- Preview of the contents of the playlist on having a valid path entered.
- Status and Progressbars work

Execute `Bard.exe` to run

## Credits: 
Logo used: Bard by John Bartolome from the Noun Project