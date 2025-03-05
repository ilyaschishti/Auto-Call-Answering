import os
import time

def get_call_state():
    """Check phone call state using ADB dumpsys command"""
    output = os.popen("adb shell dumpsys telephony.registry").read()
    
    # Look for 'mCallState=1' (ringing) or 'mCallState=2' (ongoing call)
    if "mCallState=1" in output:
        return "RINGING"
    elif "mCallState=2" in output:
        return "ONGOING"
    else:
        return "IDLE"

def answer_call():
    """Answer the call using ADB after a delay"""
    print("📞 Incoming call detected! Waiting for 3 seconds before answering...")
    time.sleep(3)  # Wait for 3 seconds before picking up
    os.system("adb shell input keyevent KEYCODE_CALL")
    print("✅ Call answered!")

def main():
    print("🔄 Auto Call Answering Started...")

    while True:
        call_state = get_call_state()
        
        if call_state == "RINGING":
            answer_call()

        time.sleep(2)  # Check for calls every 2 seconds

if __name__ == "__main__":
    main()
