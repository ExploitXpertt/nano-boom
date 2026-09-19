#!/usr/bin/env python3

import smtplib
import time
import random
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, init

init(autoreset=True)

# ==================== YOUR CREDENTIALS ====================
SENDER_EMAIL = "exploitxpertt@gmail.com"
SENDER_PASSWORD = "kzno magj qrsh aeih"
# ============================================================

# ==================== MESSAGE BODIES ====================
MESSAGE_BODIES = [
    "⚠️ Security Alert: Unauthorized access detected. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🔐 Your account has been compromised. Change password immediately. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"💀 This is a security test. No action needed. ExploitXpertt fuck You Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🎯 Important: Your login credentials were found in a data breach. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🌑 Your data has been secured. Thank you for your cooperation. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🔥 Our systems detected unusual activity from your IP. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"📡 This is an automated security notification. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"⚡ Action required: Verify your email address. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🕷️ A new device logged into your account. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🎭 Your privacy is important to us. Please review our policy. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🔓 Security update: Two-factor authentication now available. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"📀 Your account has been flagged for review. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"⚙️ System maintenance scheduled for tonight. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🎪 Welcome to our security awareness program. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🔮 We're here to help. Contact support if needed. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"✅ This is a test. No response required. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"📧 Your email is safe. This is a drill. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🔒 Security check: Please confirm your identity. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"⚠️ Phishing attempt detected. Stay vigilant. Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",

"🛡️ Your account is not Email Raaid By: Sofiya Neupane: Nosotros Academy: 10th Standard",
]

SUBJECTS = [
    "Security Alert",
    "Account Notification",
    "Important Security Update",
    "System Report",
    "Action Required",
    "Security Breach Alert",
    "Account Activity Report",
    "Security Test",
    "Notification from Security Team",
    "Alert: Unusual Activity"
]

def clear_screen():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print(f"""{Fore.MAGENTA}{Style.BRIGHT}

         ██████╗  ██████╗   ██████╗███╗   ███╗
         ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
         ██████╔╝██║   ██║██║   ██║██╔████╔██║
         ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
         ██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
         ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝                                
               ⚡ N A N O - B O O M ⚡             
             Email Testing | ExploitXpertt                 
                                                                     
{Style.RESET_ALL}""")
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!] Use only on YOUR OWN email!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[✓] Rate Limit: Auto-protected | Delay: 3-5 sec{Style.RESET_ALL}\n")

def send_email(server, recipient, subject, body):
    """Send a single email"""
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
        return True
    except Exception as e:
        return False

def main():
    banner()
    
    print(f"{Fore.CYAN}{Style.BRIGHT}[+] Gmail SMTP Ready{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] Logged in as: {SENDER_EMAIL}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    recipient = input(f"{Fore.CYAN}[>] Target email: {Style.RESET_ALL}").strip()
    
    print(f"{Fore.YELLOW}[!] Daily Gmail limit: 50-100 emails{Style.RESET_ALL}")
    count = int(input(f"{Fore.CYAN}[>] Number of emails: {Style.RESET_ALL}").strip())
    
    if count > 100:
        print(f"{Fore.YELLOW}[!] Gmail limit is 100 per day. Reducing to 100.{Style.RESET_ALL}")
        count = 100
    elif count > 50:
        print(f"{Fore.YELLOW}[⚠] Over 50 may trigger rate limit. Continue anyway? (y/n): {Style.RESET_ALL}", end="")
        if input().lower() != 'y':
            print(f"{Fore.GREEN}[+] Cancelled.{Style.RESET_ALL}")
            return
    
    print(f"\n{Fore.RED}{Style.BRIGHT}[!] Sending {count} emails to {recipient}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Auto-delay: 3-5 seconds (avoid rate limit){Style.RESET_ALL}\n")
    
    confirm = input(f"{Fore.RED}[?] This is YOUR OWN email? (yes/no): {Style.RESET_ALL}")
    if confirm.lower() != 'yes':
        print(f"{Fore.GREEN}[+] Cancelled.{Style.RESET_ALL}")
        return
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(f"{Fore.GREEN}[✓] SMTP Connected{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}[✗] Connection failed: {e}{Style.RESET_ALL}")
        return
    
    success = 0
    failed = 0
    rate_limit_hit = False
    
    for i in range(1, count + 1):
        subject = random.choice(SUBJECTS)
        body = random.choice(MESSAGE_BODIES)
        
        if send_email(server, recipient, f"{subject} [ID: {i}]", body):
            success += 1
            print(f"{Fore.GREEN}[✓] Email {i}/{count} sent{Style.RESET_ALL}")
        else:
            failed += 1
            print(f"{Fore.RED}[✗] Email {i}/{count} failed{Style.RESET_ALL}")
            
            # If multiple failures, likely rate limit
            if failed > 3:
                print(f"{Fore.YELLOW}[⚠] Rate limit detected! Stopping to avoid ban.{Style.RESET_ALL}")
                rate_limit_hit = True
                break
        
        # Dynamic delay (increase if getting close to limit)
        if i > 40:
            delay = 5
        else:
            delay = 3
        
        time.sleep(delay)
    
    server.quit()
    
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] COMPLETED: {success} sent, {failed} failed{Style.RESET_ALL}")
    
    if rate_limit_hit:
        print(f"{Fore.YELLOW}[⚠] Rate limit reached. Wait 24 hours before next test.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[✓] All emails sent successfully!{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Stopped{Style.RESET_ALL}")
