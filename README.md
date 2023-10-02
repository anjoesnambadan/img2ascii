# img2ascii
A python program to take an image from a path or webcam and display it using ascii in 8-bit color
The program first scales the input so that it can be displayed on a terminal window, and then performs a color transformation from 24 bit RGB to 3 bit color format and produces a color overlay.
Then it maps the pixels to a corresponding ASCII symbol using the brightness of the character. Finally it prints this new ASCII matrix in color using the color overlay generated in the second step.

# Sample Output
Original Image

![ascii-pineapple](https://github.com/anjoesnambadan/img2ascii/assets/108078934/83da4937-e491-4be9-ad69-955da6dc1358)

Terminal Output

![image](https://github.com/anjoesnambadan/img2ascii/assets/108078934/733a61cd-21ca-4d0c-88ec-6e7b28ebc230)
