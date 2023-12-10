# Image recognition

## Install instructions for Windows
* Install 64-bit version of Python 3.11.6 or 3.11.7<br>
* Add python.exe to your PATH-variable
* Install Visual studio code
* Create a virtual environment with one of two ways:
  * Write: python -m venv .venv 
  * Go to VS, press ctrl+alt-P, write Python: Create Virtual Environment
  * Select the interpreter: ctrl+alt-p -> Python: Select Interpreter -> choose the .venv-binary for python.exe
* Activate the virtual environment with <repo-folder>/Scripts/Activate.ps1 in a VS-codes powershell-terminal
* Install the dependencies in the terminal:<br>
  ```
  pip install tensorflow==2.14 requests notebook Pillow matplotlib numpy scikit-learn pandas torch seaborn
  ```

## Explanation of the project
<p>notebook2.ipynb is my scratch-book for testing the project. It's a bit rugged but proves the point. There are certainly improvements that could be made. It contains everything I did from downloading data, creating datasets, training and testing, including some graphs.</p>

#
A sequential list of my actions:
* I first downloaded metadata from OpenImages and plotted out the most common classes of pictures (e.g bus, car, skyscraper, etc). 
* I then choose which classes to use and created files containing the ImageID:s I needed.
* I downloaded the files and cut out the classes I needed from the pictures using the bounding boxes in the metadata.
* I resized the pictures and added padding to keep aspect ratio..
* I created datasets
* I tried a  many configurations on how to train the model, because I had trouble reaching a validation accurancy above my goal of 70%.
* I eventually achieved a test accurancy of 67,49% and felt that I could stop fine-tuning the model there.
* I plotted out some pictures with it's prediction certainty measured in percent, and also if the prediction was true or not.
* I also plotted some other graphs.

## Explanation of my model
I use a convolutation neural network. I'm adding random distortion to the training data such as random positioning, brightness, constract and rotation. I combine layers such as: Conv2D, MaxPooling, Flatten, Dense and Dropout. I use the Adam-optimizer and use an lr-scheduler to decrease the learning rate over time. 

## Retrospective
<p>First and foremost I believe my data is subpar, and my weak link. I believe it is because of the way I treated the data. Perhaps it was not good to add padding, but instead trying to cut out a perfect rectangle and resizing it. I also believe I need more data to train on. The model that produced the best result takes a lot of performance, it took me ~6 hours to train, but my PC is old and that's another bottleneck.<p>

<p>I also didn't succeed with using the dataset I saved to a file because something was wrong with the deserialization - it was not identical to the in-memory dataset I used to save to a file.</p>

<p>The state I leave this project in is quite messy. The notebook is not in a polished state full of commented code, lots of code snippets that are not run in the order the appear in on the file, with a huge need for refactoring.<br>
On the bright side the document still shows my progress quite clearly and should suffice to be used for evaluation.</p>

<p>I also was hoping to have time for a second project where I tried reinforcement learning on space invaders. I found some source code written in PyGame. I did not have time to start with that. I might however try it on my free-time, since I'm fascinated with the subject and want to try it. Only time will tell and with the holidays around the corner it's a very real possibility.</p>