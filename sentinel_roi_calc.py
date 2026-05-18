import time

def calculate_roi():
    print("=" * 60)
    print("      SENTINEL GEOFENCE NETWORK MONITOR - ROI CALCULATOR      ")
    print("=" * 60)
    print("This tool projects the cost savings of deploying Sentinel.")
    print("-" * 60)
    
    try:
        company = input("[+] Enter Company Name: ")
        endpoints = int(input("[+] Enter number of network endpoints/devices: "))
        avg_breach_cost = float(input("[+] Estimated cost of a single data breach ($): "))
        hourly_downtime_cost = float(input("[+] Estimated cost of network downtime per hour ($): "))
    except ValueError:
        print("\n[!] Invalid input. Please enter numbers for metrics.")
        return

    print("\n[~] Processing risk metrics against Sentinel security baselines...")
    time.sleep(1.5)

    PROBABILITY_WITHOUT_SENTINEL = 0.28
    PROBABILITY_WITH_SENTINEL = 0.02
    AVG_DOWNTIME_HOURS = 8
    
    annual_risk_no_sentinel = (avg_breach_cost * PROBABILITY_WITHOUT_SENTINEL) + (hourly_downtime_cost * AVG_DOWNTIME_HOURS * PROBABILITY_WITHOUT_SENTINEL)
    annual_risk_with_sentinel = (avg_breach_cost * PROBABILITY_WITH_SENTINEL) + (hourly_downtime_cost * AVG_DOWNTIME_HOURS * PROBABILITY_WITH_SENTINEL)
    
    gross_savings = annual_risk_no_sentinel - annual_risk_with_sentinel
    sentinel_licensing = endpoints * 120
    
    net_savings = gross_savings - sentinel_licensing
    roi_percentage = (net_savings / sentinel_licensing) * 100 if sentinel_licensing > 0 else 0

    print("\n" + "=" * 60)
    print(f" SECURITY ROI ANALYSIS REPORT FOR: {company.upper()}")
    print("=" * 60)
    print(f"[*] Total Monitored Endpoints:        {endpoints:,}")
    print(f"[*] Annual Risk Exposure (Unmonitored): ${annual_risk_no_sentinel:,.2f}")
    print(f"[*] Annual Risk Exposure (With Sentinel):${annual_risk_with_sentinel:,.2f}")
    print("-" * 60)
    print(f"[✓] Projected Annual Gross Savings:    ${gross_savings:,.2f}")
    print(f"[✓] Estimated Sentinel License Cost:   ${sentinel_licensing:,.2f}")
    print(f"[★] NET BUSINESS VALUE (Year 1):      ${net_savings:,.2f}")
    print(f"[★] ESTIMATED RETURN ON INVESTMENT:    {roi_percentage:.1f}%")
    print("=" * 60)
    print("Report generated successfully. Ready for executive review.\n")

if __name__ == "__main__":
    calculate_roi()
