# 📞 Auto Call Answering with Python & ADB

This Python script automatically answers incoming calls on an Android device **after 3 seconds** using ADB (Android Debug Bridge).

---

## 🚀 Features

✔️ Detects incoming calls using `adb`  
✔️ Waits 3 seconds before picking up  
✔️ Answers calls automatically  
✔️ Runs in a loop for continuous monitoring

---

## 🛠️ Prerequisites

### ✅ Install ADB

1. Download [ADB Platform Tools](https://developer.android.com/studio/releases/platform-tools)
2. Extract and **add ADB to system PATH** (optional but recommended).
3. Verify ADB installation:
   ```bash
   adb --version
   ```

✅ Enable USB Debugging on Android
Settings → About Phone → Tap "Build Number" 7 times.
Go to Settings → Developer options → Enable USB Debugging.
Connect your phone via USB and run:

3️⃣ Run the Script
python main.py
