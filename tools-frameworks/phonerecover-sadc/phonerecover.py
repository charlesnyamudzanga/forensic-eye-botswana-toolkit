#!/usr/bin/env python3
"""
PhoneRecover-SADC Toolkit - IMEI Validator & Forensic Report Generator
Prototype v0.1

© 2026 Runych Group (Pty) Ltd trading as Forensic Eye Botswana
Maintainer: Charles Nyamudzanga
Contact: starshapetech@gmail.com | +267 71897197
Address: Plot 14357 G-West, Gaborone, Botswana
License: Apache 2.0

LEGAL NOTICE:
- Use only with proper legal authority or device owner consent.
- Complies with SADC Model Law on Cybercrime principles.
- Complies with Botswana Cybercrime and Computer Related Crimes Act (2007).
- Runych Group (Pty) Ltd assumes no liability for misuse.
- All processing is done locally. No data is transmitted externally.
"""

import re
import sys
import argparse
from datetime import datetime

BANNER = """
+----------------------------------------------------------+
|        PhoneRecover-SADC Toolkit v0.1                    |
|   IMEI Validator & Forensic Report Generator             |
|                                                          |
|   Forensic Eye Botswana | Runych Group (Pty) Ltd         |
|   Maintainer: Charles Nyamudzanga                        |
|   Gaborone, Botswana | SADC Region                       |
+----------------------------------------------------------+
"""

def validate_imei(imei: str) -> dict:
    imei_clean = re.sub(r'\D', '', imei)
    result = {
        "imei": imei_clean,
        "original_input": imei,
        "length_ok": len(imei_clean) == 15,
        "digits_only": imei.replace(" ", "").replace("-", "").isdigit(),
        "luhn_pass": False,
        "valid": False,
        "tac": "",
        "snr": "",
        "check_digit": "",
        "validation_notes": []
    }
    if not result["length_ok"]:
        result["validation_notes"].append(
            f"FAIL Length invalid: {len(imei_clean)} digits (expected 15)")
        return result
    total = 0
    for i, digit in enumerate(imei_clean):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    result["luhn_pass"] = (total % 10 == 0)
    result["tac"] = imei_clean[:8]
    result["snr"] = imei_clean[8:14]
    result["check_digit"] = imei_clean[14]
    result["valid"] = result["luhn_pass"]
    if result["luhn_pass"]:
        result["validation_notes"].append(
            "PASS Luhn checksum PASSED - IMEI is mathematically valid")
        result["validation_notes"].append(
            f"PASS TAC (Manufacturer Code): {result['tac']}")
        result["validation_notes"].append(
            f"PASS Serial Number: {result['snr']}")
        result["validation_notes"].append(
            f"PASS Check Digit: {result['check_digit']}")
    else:
        result["validation_notes"].append(
            "FAIL Luhn checksum FAILED - IMEI may be fake or tampered")
        result["validation_notes"].append(
            "WARN This IMEI does not conform to international standards")
    return result


def collect_incident_details(imei_result: dict) -> dict:
    print("\n" + "-" * 60)
    print("  INCIDENT DETAILS")
    print("-" * 60)
    details = {}
    details["imei_result"] = imei_result
    details["report_id"] = f"FEB-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    details["report_datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("  [VICTIM INFORMATION]")
    details["victim_name"] = input("  Victim Full Name: ").strip() or "Not provided"
    details["victim_id"] = input("  Victim ID/Passport Number: ").strip() or "Not provided"
    details["victim_contact"] = input("  Victim Contact Number: ").strip() or "Not provided"
    print("\n  [DEVICE INFORMATION]")
    details["device_make"] = input("  Device Make (e.g. Samsung): ").strip() or "Not provided"
    details["device_model"] = input("  Device Model: ").strip() or "Not provided"
    details["device_color"] = input("  Device Color: ").strip() or "Not provided"
    details["sim_number"] = input("  SIM/Phone Number: ").strip() or "Not provided"
    print("\n  [INCIDENT INFORMATION]")
    details["incident_date"] = input("  Date of Theft/Loss (DD/MM/YYYY): ").strip() or "Not provided"
    details["incident_location"] = input("  Location of Incident: ").strip() or "Not provided"
    details["incident_description"] = input("  Brief Description: ").strip() or "Not provided"
    print("\n  [REPORTING OFFICER]")
    details["officer_name"] = input("  Officer Name: ").strip() or "Self-reported"
    details["officer_badge"] = input("  Badge/Force Number: ").strip() or "N/A"
    details["police_station"] = input("  Police Station: ").strip() or "Not provided"
    details["case_number"] = input("  Case/Docket Number: ").strip() or "Pending"
    return details


def generate_report(details: dict) -> str:
    imei_r = details["imei_result"]
    status = "VALID" if imei_r["valid"] else "INVALID / SUSPICIOUS"
    report = f"""
================================================================
   FORENSIC EYE BOTSWANA - MOBILE DEVICE INCIDENT REPORT
                PhoneRecover-SADC Toolkit v0.1
================================================================

  Report ID      : {details['report_id']}
  Generated      : {details['report_datetime']}
  Maintainer     : Charles Nyamudzanga | Runych Group (Pty) Ltd

================================================================
  SECTION 1: IMEI VALIDATION
================================================================

  IMEI Number    : {imei_r['imei']}
  Status         : {status}
  Luhn Checksum  : {'PASS' if imei_r['luhn_pass'] else 'FAIL'}
  TAC Code       : {imei_r.get('tac', 'N/A')}
  Serial Number  : {imei_r.get('snr', 'N/A')}
  Check Digit    : {imei_r.get('check_digit', 'N/A')}

================================================================
  SECTION 2: VICTIM INFORMATION
================================================================

  Full Name      : {details['victim_name']}
  ID / Passport  : {details['victim_id']}
  Contact        : {details['victim_contact']}

================================================================
  SECTION 3: DEVICE INFORMATION
================================================================

  Make           : {details['device_make']}
  Model          : {details['device_model']}
  Color          : {details['device_color']}
  SIM / Number   : {details['sim_number']}
  IMEI           : {imei_r['imei']}

================================================================
  SECTION 4: INCIDENT DETAILS
================================================================

  Date           : {details['incident_date']}
  Location       : {details['incident_location']}
  Description    : {details['incident_description']}

================================================================
  SECTION 5: REPORTING OFFICER
================================================================

  Officer Name   : {details['officer_name']}
  Badge / Force# : {details['officer_badge']}
  Police Station : {details['police_station']}
  Case / Docket# : {details['case_number']}

================================================================
  SECTION 6: RECOMMENDED ACTIONS
================================================================
"""
    if imei_r["valid"]:
        report += """
  1. IMEI is valid. Proceed with formal police report.
  2. Contact your mobile network operator to blacklist IMEI.
     - Mascom: 103 | Orange: 111 | BTC: 121
  3. Submit this report to the nearest police station.
  4. For cross-border theft contact INTERPOL via BPS CID.
  5. Keep a copy of this report for insurance claims.
"""
    else:
        report += """
  1. IMEI FAILED validation - device may have cloned/fake IMEI.
  2. Report immediately to Botswana Police Service CID.
  3. Engage Forensic Eye Botswana for forensic investigation.
  4. Do NOT attempt to use or sell this device.
"""
    report += f"""
================================================================
  LEGAL NOTICE
================================================================

  Generated by PhoneRecover-SADC
  Forensic Eye Botswana | Runych Group (Pty) Ltd
  Maintainer: Charles Nyamudzanga
  Contact: starshapetech@gmail.com | +267 71897197
  Gaborone, Botswana

================================================================
  Built in Botswana. For Africa. For the World.
================================================================
"""
    return report


def save_report(report: str, report_id: str):
    filename = f"FEB_Report_{report_id}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n  Report saved to: {filename}")
    return filename


def main():
    print(BANNER)
    parser = argparse.ArgumentParser(
        description="PhoneRecover-SADC - IMEI Validator & Forensic Report Generator"
    )
    parser.add_argument("--imei", help="IMEI number to validate", default=None)
    parser.add_argument("--generate-report", action="store_true")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    if args.imei:
        imei_input = args.imei
    else:
        print("  Enter the 15-digit IMEI number.")
        print("  Tip: Dial *#06# on the phone to find the IMEI\n")
        imei_input = input("  IMEI Number: ").strip()

    if not imei_input:
        print("  No IMEI provided. Exiting.")
        sys.exit(1)

    print("\n" + "-" * 60)
    print("  VALIDATING IMEI...")
    print("-" * 60)
    result = validate_imei(imei_input)

    for note in result["validation_notes"]:
        print(f"  {note}")

    if args.validate_only:
        print("\n  Validation complete.")
        sys.exit(0)

    print("\n  Generate a full forensic incident report?")
    choice = input("  Y for Yes, N for No: ").strip().upper()
    if choice == "Y":
        details = collect_incident_details(result)
        report = generate_report(details)
        print(report)
        save_choice = input("\n  Save report to file? (Y/N): ").strip().upper()
        if save_choice == "Y":
            save_report(report, details["report_id"])

    print("\n  Thank you for using PhoneRecover-SADC.")
    print("  Forensic Eye Botswana | Runych Group (Pty) Ltd\n")


if __name__ == "__main__":
    main()
