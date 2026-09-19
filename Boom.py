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
    "🚨 CRITICAL SECURITY BREACH: Active session hijacking detected from an unrecognized location. All current sessions have been force-terminated.",

"⚠️ DATA EXFILTRATION ALERT: High-volume data transfer detected from your cloud storage. Lock your account instantly.",

"🛑 RANSOMWARE SUSPECTED: Unauthorized encryption activity detected on linked file systems. Disconnect network access immediately.",

"💳 FINANCIAL COMPROMISE: API key leak detected. Unauthorized attempt to access attached payment methods blocked.",

"👤 IDENTITY TAKE-OVER: Primary recovery phone number and backup email were changed from an unknown IP address.",

"👁️ EXPLOIT DETECTED: Zero-day credential dump match found. Your master key hash is circulating in an active paste.",

"🔒 UNAUTHORIZED OVERRIDE: Administrator privileges granted to an external IP. System lockout imminent.",

"☣️ MALWARE INFECTION: Remote Access Trojan (RAT) activity confirmed on your active device session.",

"📲 MFA BYPASS DETECTED: SIM-swap attempt detected on your registered phone line. Authenticator access compromised.",

"🌐 DNS POISONING: Web traffic redirected to a malicious mirror server. Cease all input immediately.",
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
