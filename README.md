# SlowMovie-Kindle

Turn your Kindle into an E-ink picture frame that displays movies in a slow manner.

# Background

I first learned of this slow movie player + e ink concept from a Hackaday article [SlowMovie](https://github.com/TomWhitwell/SlowMovie). I also found the [Kindlefusion](https://github.com/diggedypomme/Kindlefusion) project where old kindles are used to display AI-generated picture frames. Hence I felt that by merging these 2 ideas together it could make for a good use of my old unused kindle lying around and collecting dust.

On top of that, with the shortage of Raspberry Pis combined with the lack of and expensive high resolution E-ink displays, this makes for a pretty feasible budget option as you can find 2nd-hand kindles for dirt cheap nowadays.

# Implementation

There is a couple options to implement SlowMovie-Kindle. Since different Kindles have different storage sizes, you could be limited by the size of the video file and frames you are able to load onto it. These solutions seek to help with that by storing and processing the frames on a seperate server / PC and automatically sending them to the Kindle. 

1. Kindle + Docker 
2. Kindle + Python Script
3. Kindle Only 

# Pre - Install

Make sure your Kindle is Jailbroken and running KUAL, MR Package Installer (MRPI) and USBnetwork. Ensure that SSH is also up and running. 

- [Only Hardware Jailbreak <= 5.15.1.1](https://www.mobileread.com/forums/showthread.php?t=346037)
- [Jailbreak <= 5.14.2](https://www.mobileread.com/forums/showthread.php?t=346037)
- [Tools - KUAL, MRPI, USBnetwork](https://www.mobileread.com/forums/showthread.php?t=225030)

Then follow the 'Installation' and 'How to Run' sections from the [Kindlefusion](https://github.com/diggedypomme/Kindlefusion) page. ( You can skip steps 4 and 5 in 'Installation' ) This project will be piggybacking off the webserver that runs on the Kindle that Kindlefusion provides.

# Main Install

## Kindle + Docker 

WIP

## Kindle + Python Script

WIP

## Kindle Only

WIP

# Usage

WIP

# License

WIP

# Credits

WIP

