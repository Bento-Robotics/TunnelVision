# TunnelVision *- Bento robotics Computer Vision*

Basically just simple CV stuff :)

---

## opencv-python in PyCharm

**For whatever reason PyCharm can't find cv2 when you import it.  
Your code will compile just fine, but code insight and autocomplete don't work.**  
*Here's the fix:*

Go to: `Settings -> Project: <name> -> Python Interpreter`  
Click on the `Python Interpreter:` drop-down box  
Click `Show All...`  
Click the `Show Interpreter Paths` button (looks like a folder tree)  

If you use a virtual environment (recommended):   
Add `<project_location>/venv/lib/python<ver>/site-packages/cv2`  
*(if it's not there try lib64)*

Else try:
Add `/lib64/python<ver>/site-packages/cv2`

> Replace `python<ver>` with your python version (in my case `python3.11`)

:warning: If neither exist you need to install `opencv-python` first! :warning:  
`pip install opencv-python`

<br>

**PyCharm should now update its database, and you'll be good to go!**  
*If it still doesn't work, hit `File -> Invalidate Caches...` to force-reload*

## :exclamation: opencv-python doesn't work on wayland!

[**You need to use X11**](https://github.com/opencv/opencv-python/issues/729)  
Or you can run it in a container :D
