import speech_recognition as sr
import pyttsx3
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjustable speech speed
engine.setProperty('volume', 0.9)  # Volume level

# Simulated haptic feedback (in a real app, this would trigger device vibration)
def haptic_feedback(pattern):
    if pattern == "select":
        print("Haptic: Short buzz")
    elif pattern == "error":
        print("Haptic: Long buzz")
    elif pattern == "loading":
        print("Haptic: Rhythmic pulse")

# Speak text and provide haptic feedback
def speak(text, haptic=None):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()
    if haptic:
        haptic_feedback(haptic)

# Listen for voice commands
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command heard: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.", "error")
        return None
    except sr.RequestError:
        speak("Network error. Please try again.", "error")
        return None

# Simulated notifications data
notifications = [
    "Message from John at 2 PM: 'See you tomorrow.'",
    "Email from Work at 1 PM: 'Meeting rescheduled.'",
    "Reminder at 3 PM: 'Doctor appointment.'"
]

# Main app logic
def visionaid_app():
    speak("Welcome to VisionAid. Say 'check notifications' to start.", "select")
    
    while True:
        command = listen_for_command()
        
        if command:
            if "check notifications" in command:
                if notifications:
                    speak(f"You have {len(notifications)} new notifications. Say 'next' to hear the first one.", "select")
                else:
                    speak("No new notifications.", "select")
            
            elif "next" in command:
                if notifications:
                    current_notification = notifications.pop(0)
                    speak(f"Notification: {current_notification} Say 'reply' to respond, or 'next' for the next one.", "select")
                else:
                    speak("No more notifications.", "select")
            
            elif "reply" in command:
                speak("Recording reply now. Speak after the beep.", "select")
                time.sleep(1)  # Simulate beep delay
                print("Beep!")
                reply = listen_for_command()
                if reply:
                    speak(f"Reply recorded: {reply}. Say 'send' to confirm.", "select")
            
            elif "send" in command:
                speak("Message sent.", "select")
            
            elif "exit" in command:
                speak("Goodbye.", "select")
                break
            
            else:
                speak("Command not recognized. Try 'check notifications' or 'exit'.", "error")

# Run the app
if __name__ == "__main__":
    try:
        visionaid_app()
    except KeyboardInterrupt:
        speak("Shutting down.", "select")