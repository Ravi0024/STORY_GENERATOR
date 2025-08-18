📝 Mad Libs Story Generator
This is a fun and interactive Mad Libs-style story generator built with Python Flask and HTML. Users fill in the blanks (like name, place, object, animal, and action), and the app generates a unique, whimsical story on the fly.

🚀 Features
-> Easy-to-use web interface with suggestion lists

-> Dynamic story generation based on user input

-> Flask-powered backend for form handling and rendering

-> Clean, beginner-friendly code structure

💡 Technologies Used
* Python 3

* Flask

* HTML5 with <datalist> input suggestions

📂 Project Structure
css
madlibs-story-generator/
├── app.py               # Flask app logic
└── templates/
    ├── form.html        # User input form
    └── story.html       # Story display page
    
▶️ How to Run Locally
1.Clone the repository:

bash

git clone https://github.com/Ravi0024/STORY_GENERATOR.git 

2.Create a virtual environment and install Flask:

bash

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install flask


3.Run the app:

bash

python app.py
