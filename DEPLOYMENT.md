# Deployment Guide

## Option 1: GitHub Actions (Recommended - FREE)

### Setup:
1. Push your code to GitHub
2. Go to Settings → Secrets and variables → Actions
3. Add secrets:
   - `RYNE_EMAIL`: laikojunior14@gmail.com
   - `RYNE_PASSWORD`: LAIKO//WAFFLE25RYNE
4. The workflow will run automatically every 10 minutes
5. Tokens will be committed back to the repo

### Commands:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Advantages:
- ✅ Completely FREE
- ✅ No server maintenance
- ✅ Automatic scheduling
- ✅ Version control built-in

---

## Option 2: Railway (Easy Deployment)

### Setup:
1. Create account at https://railway.app
2. Install Railway CLI:
```bash
npm install -g @railway/cli
```
3. Deploy:
```bash
railway login
railway init
railway up
```
4. Add environment variables in Railway dashboard:
   - `RYNE_EMAIL`
   - `RYNE_PASSWORD`

### Cron Job:
Add to Railway settings or use a cron service to hit your endpoint every 10 minutes.

### Cost: ~$5/month

---

## Option 3: Heroku

### Setup:
1. Create Heroku account
2. Install Heroku CLI
3. Create `Procfile`:
```
worker: python auto_refresh_service.py
```
4. Deploy:
```bash
heroku login
heroku create ryne-token-refresher
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-google-chrome
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver
git push heroku main
heroku config:set RYNE_EMAIL=laikojunior14@gmail.com
heroku config:set RYNE_PASSWORD=LAIKO//WAFFLE25RYNE
heroku ps:scale worker=1
```

### Cost: ~$7/month

---

## Option 4: AWS EC2 (Full Control)

### Setup:
1. Launch Ubuntu EC2 instance (t2.micro - FREE tier)
2. SSH into instance
3. Install dependencies:
```bash
sudo apt update
sudo apt install -y python3-pip chromium-browser chromium-chromedriver
pip3 install -r requirements.txt
```
4. Setup cron job:
```bash
crontab -e
# Add this line:
*/10 * * * * cd /path/to/RyneAI && python3 token_extractor_headless.py
```

### Cost: FREE (first year with AWS Free Tier)

---

## Option 5: Google Cloud Run (Serverless)

### Setup:
1. Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "token_extractor_headless.py"]
```

2. Deploy:
```bash
gcloud run deploy ryne-token-refresher \
  --source . \
  --set-env-vars RYNE_EMAIL=laikojunior14@gmail.com,RYNE_PASSWORD=LAIKO//WAFFLE25RYNE
```

3. Use Google Cloud Scheduler to trigger every 10 minutes

### Cost: ~$1-2/month

---

## Option 6: Azure Container Instances

Similar to Google Cloud Run but on Azure platform.

---

## Recommended Setup: GitHub Actions

**Why?**
- ✅ FREE forever
- ✅ No maintenance
- ✅ Automatic git commits
- ✅ Easy to setup
- ✅ Built-in version control
- ✅ Can host HTML dashboard on GitHub Pages

### Quick Start:
```bash
# 1. Create GitHub repo
# 2. Push code
git init
git add .
git commit -m "Add token refresh automation"
git remote add origin https://github.com/yourusername/ryne-token-refresher.git
git push -u origin main

# 3. Add secrets in GitHub Settings
# 4. Enable GitHub Actions
# 5. Done! Tokens auto-refresh every 10 minutes
```

### Deploy Dashboard to GitHub Pages:
```bash
# In GitHub repo settings:
# - Go to Pages
# - Set source to main branch
# - Your dashboard will be live at: https://yourusername.github.io/ryne-token-refresher/
```

---

## Security Notes

- Never commit credentials directly in code
- Always use environment variables or secrets
- Add to `.gitignore`:
```
token*.txt
token*.json
*.log
```

## Monitoring

All options provide logs to monitor token refresh:
- **GitHub Actions**: Check Actions tab
- **Railway/Heroku**: Check logs in dashboard
- **AWS/GCP**: CloudWatch/Stackdriver logs
