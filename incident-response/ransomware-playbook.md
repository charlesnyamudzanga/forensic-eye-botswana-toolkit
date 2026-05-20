# 🚨 Ransomware Incident Response Playbook
## Forensic Eye Botswana Toolkit | Incident Response Series

**Version:** 1.0  
**Author:** Forensic Eye Botswana (Pty) Ltd  
**Region:** Botswana & SADC  
**Last Updated:** May 2026  

---

> *"No Agenda. No Filter. Just The World As It Is."* — Forensic Eye Botswana

---

## 📋 Overview

Ransomware is one of the fastest-growing cyber threats affecting businesses across Botswana and Southern Africa. Attackers encrypt your files and demand payment — often in cryptocurrency — before restoring access. This playbook gives your organisation a clear, step-by-step response framework the moment ransomware is detected.

**This playbook is designed for:**
- Botswana SMEs with limited IT staff
- Office administrators who first discover the attack
- IT officers responding without a dedicated security team
- Law enforcement and forensic investigators

---

## ⚠️ CRITICAL FIRST RULE

> **DO NOT PAY THE RANSOM.**  
> Payment does not guarantee file recovery. It funds criminal operations and marks your organisation as a willing target for future attacks. Contact Forensic Eye Botswana or BOCRA before making any payment decision.

---

## 🔴 PHASE 1 — DETECTION & IDENTIFICATION (0–15 Minutes)

### Signs You May Have a Ransomware Infection

- Files have strange extensions (e.g. `.locked`, `.encrypted`, `.crypted`, `.WNCRY`)
- You cannot open documents, spreadsheets, or images
- A ransom note appears on screen (usually a `.txt` or `.html` file)
- Desktop wallpaper has changed to a ransom demand
- Multiple users on the network suddenly cannot access files
- Shared drives are inaccessible

### Immediate Actions

- [ ] **Stay calm.** Do not click anything on the ransom note screen.
- [ ] **Note the exact time** you discovered the infection.
- [ ] **Take a photo** of the ransom note screen with your phone — this is evidence.
- [ ] **Do NOT restart** the infected computer — this may destroy forensic evidence.
- [ ] **Do NOT attempt to decrypt** files yourself using unknown tools.
- [ ] **Alert your supervisor or IT officer immediately.**

---

## 🟠 PHASE 2 — CONTAINMENT (15–60 Minutes)

### Step 1: Isolate the Infected Machine

Disconnect the infected computer from the network **immediately** to stop the ransomware from spreading:

- **Unplug the network cable** (ethernet) from the back of the computer
- **Turn off Wi-Fi** on the infected machine
- **Do NOT shut down the computer** — keep it powered on for forensic investigation

### Step 2: Identify the Scope

Check which systems are affected:

- [ ] How many computers show symptoms?
- [ ] Are shared network drives (e.g. company file server) affected?
- [ ] Is the backup server accessible?
- [ ] Are any cloud services (e.g. Google Drive, OneDrive) syncing encrypted files?

> ⚠️ **Stop all cloud sync immediately** — ransomware can encrypt cloud-synced files too.

### Step 3: Isolate Other At-Risk Systems

For every other computer on the same network:

- [ ] Disconnect from network temporarily
- [ ] Check for suspicious file extensions
- [ ] Check if they can open normal files

### Step 4: Preserve the Network

- [ ] Take a photo or screenshot of your network diagram if you have one
- [ ] Note which switches, routers, and servers are connected
- [ ] Do NOT reset or reboot any networking equipment yet

---

## 🟡 PHASE 3 — EVIDENCE COLLECTION (1–3 Hours)

### Why Evidence Matters in Botswana

Under the **Cybercrime and Computer Related Crimes Act of Botswana (2007)**, ransomware attacks are criminal offences. Proper evidence collection supports prosecution and insurance claims.

### What to Collect

**On the infected machine (without touching files):**
- [ ] Photograph the ransom note on screen
- [ ] Note all running programs (take a photo of the taskbar)
- [ ] Record the computer name, IP address, and username
- [ ] Note the date and time of discovery

**Network evidence:**
- [ ] Export router/firewall logs if accessible
- [ ] Note any unusual outbound connections
- [ ] Record all IP addresses of affected machines

**Business impact:**
- [ ] List all files and folders that appear encrypted
- [ ] Identify which business operations are affected
- [ ] Note any financial transactions made in the 48 hours before attack

### Chain of Custody

Complete a chain of custody form for each piece of evidence. A template is available in the `legal-frameworks/` folder of this toolkit.

---

## 🔵 PHASE 4 — NOTIFICATION (Within 3 Hours)

### Who to Notify in Botswana

| Contact | Why | Details |
|--------|-----|---------|
| **BOCRA** (Botswana Communications Regulatory Authority) | Cyber incident reporting | bocra.org.bw |
| **Botswana Police Service — CID** | Criminal investigation | Report at nearest station |
| **Forensic Eye Botswana** | Digital forensics & recovery | forensiceyebotswana.com |
| **Your Insurance Provider** | Cyber insurance claim | Check your policy |
| **Your Bank** | If financial systems affected | Call fraud line immediately |
| **BURS** | If tax/financial data was accessed | Notify data breach |

### Notify Your Staff

Send a brief internal notice:

> *"We are currently experiencing a cyber security incident. Please do not use your work computers until further notice. Do not access company email or shared drives. IT support is investigating. We will update you shortly."*

### Do NOT Post on Social Media

Do not publicly announce the attack until you have legal advice. Premature disclosure can harm your business reputation and compromise the investigation.

---

## 🟢 PHASE 5 — ERADICATION & RECOVERY (Hours to Days)

### Step 1: Identify the Ransomware Variant

Use these free resources to identify the ransomware:
- **ID Ransomware** (id-ransomware.malwarehunterteam.com) — upload the ransom note
- **No More Ransom** (nomoreransom.org) — free decryption tools for known variants

### Step 2: Clean Infected Systems

- [ ] Do NOT reuse infected machines until professionally cleaned
- [ ] Engage a certified digital forensics firm (Forensic Eye Botswana) for safe forensic imaging before wiping
- [ ] Wipe and reinstall operating systems on infected machines
- [ ] Change ALL passwords — email, banking, company systems, Wi-Fi

### Step 3: Restore from Backup

> This is why **offline backups** are critical. Cloud backups may also be encrypted.

- [ ] Identify your most recent clean backup (before infection date)
- [ ] Restore to a freshly wiped machine — not the infected one
- [ ] Verify restored files are clean before reconnecting to network
- [ ] Test all critical business systems after restore

### Step 4: Patch and Harden

After recovery, immediately:

- [ ] Update all operating systems (Windows Update)
- [ ] Update all software (especially Office, browsers, Java, Adobe)
- [ ] Enable Windows Defender or install reputable antivirus
- [ ] Disable Remote Desktop Protocol (RDP) if not needed
- [ ] Enable Multi-Factor Authentication (MFA) on all accounts

---

## 🛡️ PHASE 6 — POST-INCIDENT REVIEW

### Lessons Learned Meeting

Within 1 week of recovery, hold a review with key staff:

- How did the ransomware enter? (phishing email, USB, RDP, software vulnerability)
- Which systems were most affected and why?
- How long did recovery take?
- What was the total business cost?
- What controls failed?

### Update Your Defences

| Control | Action |
|---------|--------|
| Backups | Implement 3-2-1 rule: 3 copies, 2 media types, 1 offsite |
| Email | Enable spam filtering, train staff on phishing |
| Access | Remove admin rights from standard users |
| Patching | Set automatic updates on all systems |
| Monitoring | Install basic endpoint detection tool |

---

## 🇧🇼 BOTSWANA-SPECIFIC THREAT NOTES

### Common Entry Points Observed in Botswana

- **Phishing emails** pretending to be BURS tax refunds or BPC bills
- **WhatsApp links** claiming to be Orange Money or MyZaka promotions
- **Fake software downloads** from unofficial sites
- **Unpatched remote desktop connections** (very common in SMEs)
- **USB drives** brought from home or shared between offices

### Financial Fraud Connection

Ransomware attackers in the SADC region increasingly combine ransomware with:
- Mobile money fraud (Orange Money, MyZaka)
- Business Email Compromise (BEC) — fake payment instructions
- Data theft before encryption (double extortion)

Always check if sensitive data was exfiltrated before the encryption began.

---

## 📞 EMERGENCY CONTACTS

| Service | Contact |
|---------|---------|
| Forensic Eye Botswana | forensiceyebotswana.com |
| BOCRA Cyber Helpline | bocra.org.bw |
| Botswana Police CID | +267 3655 000 |
| No More Ransom Project | nomoreransom.org |
| SADC Cybersecurity | sadc.int |

---

## 📎 RELATED RESOURCES IN THIS TOOLKIT

- `legal-frameworks/chain-of-custody-form.md`
- `awareness-training/cyber-hygiene-checklist.md`
- `mobile-forensics/android-forensics-workflow.md`
- `tools/hash_verify.py`

---

## 📄 License

MIT License — Free to use, adapt, and share.  
Attribution to Forensic Eye Botswana (Pty) Ltd appreciated.

---

*Built in Botswana. For Africa. For the World.* 🌍  
**Forensic Eye Botswana (Pty) Ltd | Gaborone, Botswana 🇧🇼**
