"""
Headless version of token extractor for cloud deployment
Uses environment variables for credentials
"""

import os
import time
import json
from datetime import datetime
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class RyneTokenExtractorHeadless:
    def __init__(self):
        self.token = None
        self.driver = None
        self.email = os.getenv('RYNE_EMAIL', 'laikojunior14@gmail.com')
        self.password = os.getenv('RYNE_PASSWORD', 'LAIKO//WAFFLE25RYNE')
        
    def setup_driver(self):
        """Setup Chrome driver in headless mode"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        
        seleniumwire_options = {
            'disable_encoding': True
        }
        
        self.driver = webdriver.Chrome(
            options=chrome_options,
            seleniumwire_options=seleniumwire_options
        )
        
    def extract_token_from_requests(self):
        """Extract JWT token and cookies from network requests"""
        for request in self.driver.requests:
            if 'supabase.co/rest/v1/' in request.url or 'ryne.ai' in request.url:
                # Extract JWT token
                if request.headers.get('Authorization'):
                    auth_header = request.headers.get('Authorization')
                    if auth_header and auth_header.startswith('Bearer '):
                        self.token = auth_header
                        print(f"✅ Token found from: {request.url}")
                
                # Extract cookies
                if request.headers.get('Cookie'):
                    self.cookies = request.headers.get('Cookie')
                    print(f"✅ Cookies found from: {request.url}")
                
                if self.token:
                    return True
        return False
    
    def login_and_extract(self):
        """Auto-login and extract token"""
        try:
            self.setup_driver()
            
            print("🌐 Opening ryne.ai signin page...")
            self.driver.get("https://ryne.ai/signin")
            time.sleep(3)
            
            print("🔐 Attempting auto-login...")
            
            # Fill email
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[name='email']"))
            )
            email_input.clear()
            email_input.send_keys(self.email)
            time.sleep(1)
            
            # Fill password
            password_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='password'], input[name='password']")
            password_input.clear()
            password_input.send_keys(self.password)
            time.sleep(1)
            
            # Submit form
            password_input.send_keys(Keys.RETURN)
            print("✅ Submitted form")
            
            print("⏳ Waiting for login to complete...")
            time.sleep(5)
            
            # Navigate to dashboard
            print("📊 Navigating to dashboard...")
            self.driver.get("https://ryne.ai/dashboard")
            time.sleep(5)
            
            # Wait and extract token
            print("🔍 Extracting token...")
            for i in range(30):
                if self.extract_token_from_requests():
                    return True
                time.sleep(1)
            
            print("❌ Could not find JWT token")
            return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
    
    def save_token(self, filename="token.txt"):
        """Save token and cookies to file"""
        if not self.token:
            return False
        
        try:
            # Save main token file
            with open(filename, 'w') as f:
                f.write(self.token)
            print(f"💾 Token saved to {filename}")
            
            # Save cookies if available
            if self.cookies:
                with open("Cookie.txt", 'w') as f:
                    f.write(self.cookies)
                print(f"💾 Cookies saved to Cookie.txt")
            
            # Save JSON with metadata
            token_data = {
                "token": self.token,
                "cookies": self.cookies if self.cookies else None,
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
            return False
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
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
    print("=" * 60)
    print("🔑 Ryne.AI JWT Token Extractor (Headless)")
    print("=" * 60)
    print()
    
    extractor = RyneTokenExtractorHeadless()
    
    if extractor.login_and_extract():
        print()
        print("=" * 60)
        print("✅ Token extracted successfully")
        print("=" * 60)
        
        extractor.save_token()
        extractor.update_html_file()
        
        print()
        print("✅ All done!")
    else:
        print()
        print("❌ Failed to extract token")
        exit(1)


if __name__ == "__main__":
    main()
