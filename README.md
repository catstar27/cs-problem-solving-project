# RT60 visualizer
## Project Description
The following code creates a GUI that 
allows the user to open an audio file to
visualize the RT60 of a room, known as the reverberation time.
This allows the user to see the amount of time it takes for the audio to "fade away" in a room when it ends.

## Purpose
The reason why such a program would be useful is the need for audio to be intelligible.
Measuring the reverberation in a room allows the user to decide if they should proceed with an audio based project based on
the quality of the acoustics in the room.

For example, if someone needed to find a location to record
audio of a guitar sample in high quality, they would need to find
a room best suited to the frequency guitars typically play at (150 to 500Hz)

## Instructions
When the user runs the main controller, the first step would be to 
select the audio file they wish to process. When that file is selected, an RT60 plot will be generated.

There will then be options to combine the low, mid, high frequencies into a single plot,
display the difference when the RT60 is reduced to 0.5 seconds, and 
further data plots related to the RT60 value.