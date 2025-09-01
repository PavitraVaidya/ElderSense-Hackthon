import smtplib
from email.mime.text import MIMEText

SENDER_EMAIL = "user-email@gmail.com"
SENDER_PASSWORD = "user password"   # paste your app password
CAREGIVER_EMAIL = "caretaker-email@gmail.com"         # replace with caregiver email

def send_emergency_email(user="Grandma"):
    subject = "🚨 Emergency Alert"
    body = f"{user} needs immediate help! Please check on them."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = CAREGIVER_EMAIL

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, CAREGIVER_EMAIL, msg.as_string())
        server.quit()
        print("✅ Emergency Email Sent!")
    except Exception as e:
        print("❌ Error sending email:", e)