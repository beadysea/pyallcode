# Installating the Allcode API

## Local Installation

Download the Allcode API package wheel from Moodle to your downloads folder. Open your file explorer, navigate to your downloads folder and find the file:

> allcode-2.0.0-py3-none-any.whl

Right-click on the file and choose the copy path option.

Now navigate your project folder, right-click and choose the open in terminal option.

In the command prompt terminal, check your virtual environment is enabled. Your command prompt should be similar to the following:

 ```(.venv) C:\Users\[your_folder_path]>```

If you don't see (.venv) at the start of your file path, then enter the following command:

```.venv\scripts\activate.bat```

If you get the error ```The system cannot find the path specified.``` Then you haven't created a virtual environment for your project yet. To create a virtual environment type the command:

```python -m venv .venv```

Then try the command ```.venv\scripts\activate.bat``` again.

You should now see ```(.venv) C:\Users\[your_folder_path]>```

Install the allcode API to your project virtual environment by typing:
```pip install``` then use ctrl+v to paste the download path. Your command prompt line should look similar to:

```pip install "C:\Users\[Your Student ID]\Downloads\allcode-2.0.0-py3-none-any.whl```

press the return key. You should see a lot of installation text whizz past on your screen. Wait until the command prompt returns. Congratulations, you have just installed your first python library.
