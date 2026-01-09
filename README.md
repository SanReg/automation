# Ryne.AI Token Extractor

Automatically extract JWT tokens from logged-in ryne.ai sessions.

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Chrome WebDriver:
   - The script will use Chrome browser
   - Make sure Chrome is installed on your system

## Usage

### Basic Usage

Run the script:
```bash
python token_extractor.py
```

### Options

**Option 1: Manual Login (Recommended)**
- The script opens a Chrome browser
- You manually log in to ryne.ai
- Navigate around the site (dashboard, checks history, etc.)
- The script automatically captures the JWT token from network requests
- Token is saved to files

**Option 2: Auto-Login**
- Provide your email and password
- Script attempts to log in automatically
- Less reliable due to varying login page structures

## What It Does

1. ✅ Opens ryne.ai in a Chrome browser
2. ✅ Waits for you to log in (or attempts auto-login)
3. ✅ Monitors all network requests
4. ✅ Extracts the JWT token from Authorization headers
5. ✅ Saves token to multiple files:
   - `token.txt` - Current token
   - `token_backup_TIMESTAMP.txt` - Timestamped backup
   - `token.json` - Token with metadata
6. ✅ Optionally updates `index.html` with the new token

## Output Files

- **token.txt**: The current JWT token (Bearer included)
- **token_backup_YYYYMMDD_HHMMSS.txt**: Timestamped backup
- **token.json**: JSON file with token and metadata

## Automation

To run this automatically every 10 minutes, you can:

### Windows (Task Scheduler)
1. Open Task Scheduler
2. Create a new task
3. Set trigger to repeat every 10 minutes
4. Set action to run: `python C:\Users\Santosh\Desktop\RyneAI\token_extractor.py`

### Alternative: Python Script Loop
Create `auto_refresh_token.py`:
```python
import time
import subprocess

while True:
    print("Running token extractor...")
    subprocess.run(["python", "token_extractor.py"])
    print("Waiting 10 minutes...")
    time.sleep(600)  # 10 minutes
```

## Troubleshooting

**"chromedriver not found"**
- Install webdriver-manager: `pip install webdriver-manager`
- Or download ChromeDriver manually from https://chromedriver.chromium.org/

**"Token not found"**
- Make sure you're fully logged in
- Navigate to different pages in ryne.ai (dashboard, checks history)
- Wait a bit longer for requests to be made

**Browser doesn't open**
- Make sure Chrome is installed
- Try running as administrator

## Security Note

- Keep your token files secure
- Don't share them publicly
- Add `token*.txt` and `token.json` to `.gitignore` if using git

## Requirements

- Python 3.7+
- Chrome browser
- selenium-wire
- selenium
