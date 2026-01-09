# 🆓 FREE Deployment Guide - GitHub Actions

## ✅ 100% FREE Forever - No Credit Card Required!

---

## 🚀 Quick Setup (5 Minutes)

Your code is already pushed to GitHub at: `SanReg/automation`

### Step 1: Enable GitHub Actions (Already Done ✅)
The workflow file is already in your repo!

### Step 2: Add Secrets

1. Go to: https://github.com/SanReg/automation/settings/secrets/actions
2. Click **"New repository secret"**
3. Add these two secrets:

   **Secret 1:**
   - Name: `RYNE_EMAIL`
   - Value: `laikojunior14@gmail.com`

   **Secret 2:**
   - Name: `RYNE_PASSWORD`
   - Value: `LAIKO//WAFFLE25RYNE`

### Step 3: Enable Actions

1. Go to: https://github.com/SanReg/automation/actions
2. If you see "Enable Actions", click it
3. Done! ✅

---

## 🎯 What Happens Now?

- ✅ Tokens refresh **automatically every 10 minutes**
- ✅ Completely **FREE forever**
- ✅ No server needed
- ✅ No credit card needed
- ✅ Automatic commits to your repo
- ✅ Can manually trigger anytime

---

## 📊 View Logs

1. Go to: https://github.com/SanReg/automation/actions
2. Click on any workflow run
3. See the token refresh logs

---

## ⚡ Manual Trigger

Need a fresh token NOW?

1. Go to: https://github.com/SanReg/automation/actions
2. Click on "Auto Token Refresh"
3. Click "Run workflow" button
4. Click green "Run workflow"
5. Fresh token in ~30 seconds!

---

## 🌐 Host Dashboard for FREE

Want your HTML dashboard online too?

### Enable GitHub Pages:

1. Go to: https://github.com/SanReg/automation/settings/pages
2. Under "Source", select: **main** branch
3. Click **Save**
4. Your dashboard will be live at:
   - `https://sanreg.github.io/automation/`

✅ FREE hosting for your dashboard!

---

## 🔍 How It Works

```
Every 10 minutes:
1. GitHub Actions runs automatically
2. Logs into ryne.ai
3. Extracts fresh JWT token
4. Updates token.txt, token.json, index.html
5. Commits changes back to your repo
6. Your dashboard always has fresh token!
```

---

## 💰 Cost Breakdown

| Service | Cost |
|---------|------|
| GitHub Actions | **FREE** |
| Token Refresh | **FREE** |
| GitHub Pages | **FREE** |
| Total | **$0.00** |

GitHub gives you **2,000 minutes/month FREE**. Your script uses ~1 minute per run, so you're covered!

---

## ✅ Checklist

- [x] Code pushed to GitHub (SanReg/automation)
- [ ] Secrets added (RYNE_EMAIL, RYNE_PASSWORD)
- [ ] GitHub Actions enabled
- [ ] First workflow run successful
- [ ] GitHub Pages enabled (optional)

---

## 🎉 Next Steps

1. **Add the secrets** (most important!)
2. **Enable Actions** if disabled
3. **Wait 10 minutes** or trigger manually
4. **Check the Actions tab** to see it working
5. **Enjoy automatic token refresh!** ☕

---

## 🐛 Troubleshooting

**"Actions disabled"**
- Go to Settings → Actions → Enable

**"Secrets not found"**
- Double-check secret names: `RYNE_EMAIL` and `RYNE_PASSWORD`
- Make sure there are no extra spaces

**"Workflow not running"**
- Manually trigger it: Actions → Auto Token Refresh → Run workflow

**Need to see what's happening?**
- Go to Actions tab → Click on a run → View logs

---

## 📱 Get Notifications (Optional)

Want to know when token refreshes?

Add this to your workflow (in the file):
```yaml
    - name: Send notification
      run: echo "✅ Token refreshed at $(date)"
```

Or setup email notifications:
- Settings → Notifications → Actions

---

## 🔄 Update Frequency

Current: Every 10 minutes

Want different frequency? Edit `.github/workflows/token-refresh.yml`:
- Every 5 minutes: `*/5 * * * *`
- Every 15 minutes: `*/15 * * * *`
- Every hour: `0 * * * *`

---

## 🎊 That's It!

You now have:
- ✅ FREE automatic token refresh
- ✅ FREE dashboard hosting (if you enable Pages)
- ✅ No maintenance required
- ✅ No payment ever

**Total time to setup: 2 minutes**
**Total cost: $0.00 forever**

Enjoy! 🚀
