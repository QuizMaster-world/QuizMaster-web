[![License GPLv3](https://img.shields.io/badge/license-GPL_v3-green.svg)](http://www.gnu.org/licenses/gpl-3.0.html)

# QuizMaster-web

QuizMaster-web is a modern web adaptation of [QuizMaster](https://github.com/hermonochy/QuizMaster). Test your knowledge and learn new topics from your browser with an interactive, fast-paced quiz experience. Whether you're a student, educator, or quiz enthusiast, QuizMaster-web offers an engaging platform accessible from any device with a web browser.

## Usage

### Installation

**Prerequisites:**
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- pip (Python package manager)

1. Clone this repository via terminal:

```git clone https://github.com/hermonochy/QuizMaster-web```

2. Navigate to the directory:

```cd QuizMaster-web```

3. Create a virtual environment (optional but recommended):

```python3 -m venv venv```

4. Activate the virtual environment:

```source venv/bin/activate``` (On Windows: `venv\Scripts\activate`)

5. Install required packages:

```pip install -r requirements.txt```

### Running QuizMaster-web

To run QuizMaster-web, you need to start both the backend server and access the frontend.

**Start the backend server:**

```fastapi run main.py```

The backend will be accessible at `http://127.0.0.1:8000/`

**Open the Website**

Go to `qm.html` in the `client` folder and double click on it to open in the browser.