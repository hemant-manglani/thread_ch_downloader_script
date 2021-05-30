# thread_ch_downloader_script
This repository will use to download video from the google thread drive channel each course vies.


### step 1 : clone the project.
### step 2 : create virtual environment using below command.

` python -m venv venv `

or, use your default python environment.

### step 3: Install all required library.

` pip install -r requirement.txt`

### step 4: Go to the below url and copy link of course that you want to download and past them into download_path text file line by line.

Direct videos contains link : True flag

URL : https://archive.thehated7.workers.dev/0:/Frontend%20Masters/Coercion%20in%20JavaScript/

hierarchy videos contains link up-to level one only: False flag

URL : https://archive.thehated7.workers.dev/0:/RBR%20Gate-2021/Data%20Structures/

### step 5: Go to main.py and make direct_videos_list flash TRUE/FALSE according to your step 4.

### step 6: change download videos default path in main,py by setting this variable default_download_dir.

#### Note: Make sure that folder not contains any files already(Folder is ok).

### step 7: Change chromedriver.exe path in main.py

NOTE: Currently I am using chromedriver.exe 90.* it's depend on your chrome browser. 

### step 8: All set ! just hit main.py 