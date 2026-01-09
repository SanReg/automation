"""
Automated Token Refresh Service
Runs token_extractor.py every 10 minutes automatically
"""

import time
import subprocess
import os
from datetime import datetime

def run_token_extractor():
    """Run the token extractor script"""
    try:
        print(f"\n{'='*60}")
        print(f"🔄 Running token extraction at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        # Run the token extractor
        result = subprocess.run(
            ["python", "token_extractor.py"],
            capture_output=True,
            text=True,
            timeout=120  # 2 minute timeout
        )
        
        if result.returncode == 0:
            print("✅ Token extraction successful")
            print(result.stdout)
        else:
            print("❌ Token extraction failed")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⚠️ Token extraction timed out (took more than 2 minutes)")
    except Exception as e:
        print(f"❌ Error running token extractor: {e}")

def main():
    """Main loop to run token extraction every 10 minutes"""
    print("🚀 Automated Token Refresh Service Started")
    print("=" * 60)
    print("⏰ Will refresh token every 10 minutes")
    print("⚠️ Keep this window open")
    print("🛑 Press Ctrl+C to stop")
    print("=" * 60)
    
    interval_minutes = 10
    interval_seconds = interval_minutes * 60
    
    while True:
        try:
            # Run token extraction
            run_token_extractor()
            
            # Wait for next run
            next_run = datetime.now().timestamp() + interval_seconds
            next_run_time = datetime.fromtimestamp(next_run).strftime('%H:%M:%S')
            
            print(f"\n⏳ Next token refresh at: {next_run_time}")
            print(f"💤 Sleeping for {interval_minutes} minutes...\n")
            
            time.sleep(interval_seconds)
            
        except KeyboardInterrupt:
            print("\n\n🛑 Stopping automated token refresh service...")
            print("✅ Service stopped gracefully")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("⏳ Will retry in 1 minute...")
            time.sleep(60)

if __name__ == "__main__":
    # Check if token_extractor.py exists
    if not os.path.exists("token_extractor.py"):
        print("❌ Error: token_extractor.py not found in current directory")
        print("   Please run this script from the RyneAI directory")
        exit(1)
    
    main()
