"""
Ryne.AI JWT Token Extractor
This script automates token extraction from a logged-in ryne.ai session.
"""

import time
import json
from datetime import datetime
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RyneTokenExtractor:
    def __init__(self):
        self.token = None
        self.driver = None
        
    def setup_driver(self):
        """Setup Chrome driver with network interception"""
        chrome_options = Options()
        # Remove headless if you want to see the browser
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Setup selenium-wire options
        seleniumwire_options = {
            'disable_encoding': True  # Enable request/response interception
        }
        
        self.driver = webdriver.Chrome(
            options=chrome_options,
            seleniumwire_options=seleniumwire_options
        )
        
    def extract_token_from_requests(self):
        """Extract JWT token from network requests"""
        print("🔍 Scanning network requests for JWT token...")
        
        for request in self.driver.requests:
            # Look for requests to Supabase endpoints
            if 'supabase.co/rest/v1/' in request.url:
                if request.headers.get('Authorization'):
                    auth_header = request.headers.get('Authorization')
                    if auth_header and auth_header.startswith('Bearer '):
                        self.token = auth_header
                        print(f"✅ Token found from: {request.url}")
                        return True
        
        return False
    
    def login_and_extract(self, email=None, password=None):
        """
        Open ryne.ai and extract token
        If email/password provided, will attempt auto-login
        Otherwise, waits for manual login
        """
        try:
            self.setup_driver()
            
            if email and password:
                print("🌐 Opening ryne.ai signin page...")
                self.driver.get("https://ryne.ai/signin")
                
                # Wait for page load
                time.sleep(3)
                
                print("🔐 Attempting auto-login...")
                try:
                    from selenium.webdriver.common.keys import Keys
                    
                    # Look for email input
                    email_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[name='email']"))
                    )
                    email_input.clear()
                    email_input.send_keys(email)
                    time.sleep(1)
                    
                    # Look for password input
                    password_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='password'], input[name='password']")
                    password_input.clear()
                    password_input.send_keys(password)
                    time.sleep(1)
                    
                    # Try multiple methods to submit the form
                    try:
                        # Method 1: Press Enter key
                        password_input.send_keys(Keys.RETURN)
                        print("✅ Submitted form with Enter key")
                    except:
                        try:
                            # Method 2: Click submit button
                            submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                            submit_btn.click()
                            print("✅ Clicked submit button")
                        except:
                            # Method 3: Try finding button by text
                            buttons = self.driver.find_elements(By.TAG_NAME, "button")
                            for btn in buttons:
                                if 'sign' in btn.text.lower() or 'log' in btn.text.lower():
                                    btn.click()
                                    print("✅ Clicked login button by text")
                                    break
                    
                    print("⏳ Waiting for login to complete...")
                    time.sleep(5)
                    
                    # Navigate to dashboard to trigger API calls
                    print("📊 Navigating to dashboard...")
                    self.driver.get("https://ryne.ai/dashboard")
                    time.sleep(3)
                    
                except Exception as e:
                    print(f"⚠️ Auto-login failed: {e}")
                    print("Please log in manually...")
            else:
                print("🌐 Opening ryne.ai...")
                self.driver.get("https://www.ryne.ai")
                time.sleep(3)
                print("⏳ Please log in manually in the browser window...")
                print("   The script will wait for you to complete login...")
            
            # Wait for user to be logged in and navigate around
            print("⏳ Waiting for authenticated requests (60 seconds)...")
            print("   Navigate to different pages in ryne.ai to generate requests...")
            print("   Go to Dashboard → Checks History → Click on any check")
            
            # Wait and check for token periodically
            for i in range(60):
                time.sleep(1)
                if self.extract_token_from_requests():
                    break
                if i % 5 == 0:
                    print(f"   Still waiting... ({60-i}s remaining)")
            
            if self.token:
                print("\n✅ Successfully extracted JWT token!")
                return True
            else:
                print("\n❌ Could not find JWT token in requests")
                print("   Make sure you're logged in and have navigated to a page with data")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            if self.driver:
                print("\n🔒 Closing browser...")
                self.driver.quit()
    
    def save_token(self, filename="token.txt"):
        """Save token to file"""
        if not self.token:
            print("❌ No token to save")
            return False
        
        try:
            with open(filename, 'w') as f:
                f.write(self.token)
            print(f"💾 Token saved to {filename}")
            
            # Also save with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"token_backup_{timestamp}.txt"
            with open(backup_filename, 'w') as f:
                f.write(self.token)
            print(f"💾 Backup saved to {backup_filename}")
            
            # Save as JSON with metadata
            token_data = {
                "token": self.token,
                "extracted_at": datetime.now().isoformat(),
                "format": "Bearer JWT"
            }
            
            with open("token.json", 'w') as f:
                json.dump(token_data, f, indent=2)
            print(f"💾 Token metadata saved to token.json")
            
            return True
        except Exception as e:
            print(f"❌ Error saving token: {e}")
            return False
    
    def update_html_file(self, html_file="index.html"):
        """Update the HTML file with the new token"""
        if not self.token:
            print("❌ No token to update")
            return False
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Find and replace the token in localStorage initialization
            # Look for the pattern: let currentAuthToken = localStorage.getItem('ryneai_token') || 'Bearer ...'
            import re
            pattern = r"let currentAuthToken = localStorage\.getItem\('ryneai_token'\) \|\| 'Bearer [^']*';"
            replacement = f"let currentAuthToken = localStorage.getItem('ryneai_token') || '{self.token}';"
            
            new_content = re.sub(pattern, replacement, html_content)
            
            if new_content != html_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Updated {html_file} with new token")
                return True
            else:
                print("⚠️ Could not find token pattern in HTML file")
                return False
                
        except Exception as e:
            print(f"❌ Error updating HTML file: {e}")
            return False


def main():
    """Main function to run the token extractor"""
    print("=" * 60)
    print("🔑 Ryne.AI JWT Token Extractor")
    print("=" * 60)
    print()
    
    extractor = RyneTokenExtractor()
    
    # Auto-login with hardcoded credentials
    email = "laikojunior14@gmail.com"
    password = "LAIKO//WAFFLE25RYNE"
    
    print("🔐 Using auto-login with saved credentials...")
    print(f"📧 Email: {email}")
    print()
    
    # Extract token
    if extractor.login_and_extract(email, password):
        print()
        print("=" * 60)
        print("📋 EXTRACTED TOKEN:")
        print("=" * 60)
        print(extractor.token)
        print("=" * 60)
        print()
        
        # Save token
        extractor.save_token()
        
        # Automatically update HTML file
        print("\n🔄 Updating index.html with new token...")
        extractor.update_html_file()
        
        print()
        print("✅ All done! You can now use the dashboard with the fresh token.")
    else:
        print()
        print("❌ Failed to extract token. Please try again.")


if __name__ == "__main__":
    main()
