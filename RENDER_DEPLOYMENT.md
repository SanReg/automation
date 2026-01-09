# 🚀 Deploy to Render - Complete Guide

## Why Render?
- ✅ **FREE** tier available
- ✅ Easy setup (simpler than Heroku)
- ✅ Built-in cron jobs
- ✅ Automatic deployments from GitHub
- ✅ No credit card required for free tier

---

## 📋 Step-by-Step Deployment

### 1. Prepare Your Code

First, make sure you have a GitHub account and your code is ready:

```bash
cd "C:\Users\Santosh\Desktop\RyneAI"

# Initialize git if not already done
git init
git add .
git commit -m "Initial commit - Token refresh automation"
git branch -M main
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., `ryne-token-refresher`)
3. Push your code:

```bash
git remote add origin https://github.com/YOUR-USERNAME/ryne-token-refresher.git
git push -u origin main
```

### 3. Deploy to Render

#### Option A: Using render.yaml (Automatic)

1. Go to https://render.com and sign up (free)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml`
5. Add environment variables:
   - `RYNE_EMAIL`: `laikojunior14@gmail.com`
   - `RYNE_PASSWORD`: `LAIKO//WAFFLE25RYNE`
6. Click **"Apply"**

✅ Done! Your token refresher will run every 10 minutes automatically.

#### Option B: Manual Setup

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Cron Job"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `ryne-token-refresher`
   - **Schedule**: `*/10 * * * *` (every 10 minutes)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python token_extractor_headless.py`
   - **Environment**: Python 3
5. Add Environment Variables:
   - Click **"Environment"** tab
   - Add `RYNE_EMAIL` = `laikojunior14@gmail.com`
   - Add `RYNE_PASSWORD` = `LAIKO//WAFFLE25RYNE`
6. Click **"Create Cron Job"**

---

## 🔧 Render Configuration Files

Your project already includes:
- ✅ `render.yaml` - Automatic deployment configuration
- ✅ `token_extractor_headless.py` - Cloud-ready script
- ✅ `requirements.txt` - Python dependencies

---

## 📊 Monitor Your Deployment

1. Go to Render Dashboard
2. Click on your cron job
3. View logs to see token refresh activity
4. Check "Events" tab for execution history

---

## 💰 Pricing

**Free Tier Includes:**
- 750 hours/month of cron job execution
- Perfect for running every 10 minutes
- No credit card required

**Paid Plans:**
- Starter: $7/month (if you need more)
- Professional: $25/month

---

## 🔄 Update Your Deployment

Whenever you push to GitHub, Render will auto-deploy:

```bash
git add .
git commit -m "Update token refresh logic"
git push
```

Render automatically deploys the changes! 🎉

---

## 🐛 Troubleshooting

### Chrome/ChromeDriver Issues
The project uses `selenium-wire` which handles Chrome automatically on Render's infrastructure.

### Token Not Updating
1. Check Render logs for errors
2. Verify environment variables are set correctly
3. Make sure the cron schedule is correct: `*/10 * * * *`

### Need Help?
Check Render logs:
- Dashboard → Your Cron Job → Logs tab

---

## 🌐 Deploy Dashboard (Optional)

Want to host the HTML dashboard too?

### Option 1: Render Static Site
1. Click **"New +"** → **"Static Site"**
2. Connect same GitHub repo
3. **Publish Directory**: `.` (root)
4. Deploy!

Your dashboard will be live at: `https://your-site.onrender.com`

### Option 2: GitHub Pages (FREE)
1. Go to your GitHub repo
2. Settings → Pages
3. Source: `main` branch
4. Save

Dashboard live at: `https://YOUR-USERNAME.github.io/ryne-token-refresher/`

---

## ✅ Final Checklist

- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] Cron job deployed
- [ ] Environment variables added
- [ ] First run successful (check logs)
- [ ] Verify token file is updating

---

## 📝 Example Render Dashboard

After deployment, you'll see:
```
✅ Cron Job: ryne-token-refresher
⏰ Schedule: Every 10 minutes
🟢 Status: Active
📊 Last run: Success (2 minutes ago)
```

---

## 🎯 Next Steps

1. Monitor first few runs in Render dashboard
2. Check logs to ensure tokens are refreshing
3. Open your dashboard HTML to see fresh data
4. Relax - it's all automated! ☕

---

Need help? Check Render's docs: https://render.com/docs/cronjobs
