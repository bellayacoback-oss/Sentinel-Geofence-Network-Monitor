# Security Audit Log Format Documentation

## Overview

This document describes the format and schema for `SENTINEL_SECURITY_AUDIT.log`, the official security audit log for the Sentinel Geofence Network Monitor system.

## Log Format

The audit log uses a **pipe-delimited (|) structured format** to enable automated parsing, filtering, and analysis by security tools and SIEM systems.

### Field Definitions

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| TIMESTAMP | ISO 8601 | Event timestamp in UTC | `2026-05-18T12:37:24Z` |
| EVENT_ID | String | Unique event identifier for tracking | `EVT-20260518-001` |
| SEVERITY | Enum | Alert severity level | `ALERT`, `ERROR`, `WARNING`, `INFO`, `DEBUG`, `CRITICAL` |
| EVENT_TYPE | String | Category of security event | `GEOFENCE_VIOLATION`, `UNAUTHORIZED_ACCESS`, `PORT_SCAN` |
| SOURCE_IP | IP Address | Originating IP address | `185.134.66.235` |
| SOURCE_PORT | Integer | Source port number | `54832` |
| DEST_PORT | Integer | Destination port number | `4444` |
| GEOFENCE_NAME | String | Name of the geofence boundary | `Primary-Zone-A` |
| EXPECTED_REGION | String | Expected geographic region | `US-CA` |
| ACTUAL_REGION | String | Detected region of source IP | `Unknown` |
| ACTION_TAKEN | String | Response action executed | `BLOCKED`, `LOGGED`, `ESCALATED`, `QUARANTINED` |
| RESPONSE_TIME_MS | Integer | Time to detect and respond (milliseconds) | `245` |
| INCIDENT_STATUS | String | Current status of the incident | `MITIGATED`, `ONGOING`, `RESOLVED`, `INVESTIGATING` |
| DETAILS | String | Free-form description of the event | Comprehensive event context |
| RESOLUTION_STATUS | String | Whether the incident was resolved | `RESOLVED`, `PENDING`, `ESCALATED` |
| ADMIN_NOTE | String | Administrative notes and follow-up actions | Actions taken and escalation details |

## Severity Levels

- **CRITICAL**: Severe security threat requiring immediate intervention (e.g., breach, system compromise)
- **ALERT**: Significant security event requiring prompt attention (e.g., geofence violation, unauthorized access)
- **ERROR**: Configuration or system error affecting security
- **WARNING**: Potential security issue requiring monitoring
- **INFO**: Informational security event (e.g., successful authentication, policy changes)
- **DEBUG**: Detailed diagnostic information (development/troubleshooting only)

## Event Types

Common event types include:

- `GEOFENCE_VIOLATION` - Unauthorized access from outside geofence boundary
- `UNAUTHORIZED_ACCESS` - Authentication failure or permission denied
- `PORT_SCAN` - Suspicious port scanning activity
- `POLICY_CHANGE` - Security policy modification
- `CONFIG_ERROR` - Configuration issue detected
- `PRIVILEGE_ESCALATION` - Unusual privilege elevation attempt
- `DATA_ACCESS` - Sensitive data access logged
- `CONNECTION_BLOCKED` - Connection attempt rejected
- `AUTHENTICATION_FAILURE` - Failed login attempt

## Log Rotation & Retention

- **Rotation**: Daily (midnight UTC)
- **File Naming Convention**: `SENTINEL_SECURITY_AUDIT.log.YYYY-MM-DD`
- **Retention**: 90 days active, then archived
- **Archive Location**: `logs/archive/`
- **Compression**: gzip (.gz) for archived logs
- **Max File Size**: 500 MB (triggers rotation)

## Access Control

- **Read Access**: Authorized security administrators and auditors only
- **Write Access**: Sentinel system service only
- **File Permissions**: `640` (rw-r-----)
- **Directory Permissions**: `750` (rwxr-x---)
- **Ownership**: `sentinel:sentinel` (dedicated service account)

## Integrity & Security

- **Hash Verification**: SHA-256 checksum calculated daily
- **Tampering Detection**: Compare checksums against secure external log server
- **Backup**: Critical logs synced to centralized SIEM system in real-time
- **Encryption**: Logs encrypted in transit using TLS 1.3+
- **Immutability**: Once written, logs cannot be modified or deleted

## Parsing Examples

### Using grep

```bash
# Find all ALERT severity events
grep "^.*|ALERT|" SENTINEL_SECURITY_AUDIT.log

# Find all geofence violations
grep "GEOFENCE_VIOLATION" SENTINEL_SECURITY_AUDIT.log

# Find events from specific IP
grep "185.134.66.235" SENTINEL_SECURITY_AUDIT.log

# Find unresolved incidents
grep "PENDING\|ESCALATED" SENTINEL_SECURITY_AUDIT.log | grep "RESOLUTION_STATUS"
```

### Using awk

```bash
# Extract timestamp and source IP
awk -F'|' '{print $1, $5}' SENTINEL_SECURITY_AUDIT.log

# Count events by severity
awk -F'|' '{print $3}' SENTINEL_SECURITY_AUDIT.log | sort | uniq -c

# List blocked connections
awk -F'|' '$11 == "BLOCKED" {print $1, $5, $7}' SENTINEL_SECURITY_AUDIT.log
```

### Using Python

```python
import csv
from datetime import datetime

with open('SENTINEL_SECURITY_AUDIT.log', 'r') as f:
    reader = csv.DictReader(f, delimiter='|')
    for row in reader:
        if row['SEVERITY'] in ['ALERT', 'CRITICAL']:
            print(f"[{row['EVENT_ID']}] {row['EVENT_TYPE']} from {row['SOURCE_IP']}:{row['SOURCE_PORT']}")
```

### Using jq (with log-to-JSON conversion)

```bash
# Convert pipe-delimited to JSON and filter
awk -F'|' 'NR==1 {header=$0; next} {
  split(header, h, "|")
  for (i=1; i<=NF; i++) printf "\"%s\":\"%s\",", h[i], $i
  printf "\n"
}' SENTINEL_SECURITY_AUDIT.log | jq 'select(.SEVERITY == "ALERT")'
```

## Best Practices

1. **Never disable audit logging** - Always maintain active logging for compliance
2. **Regular review** - Review logs weekly for suspicious patterns and anomalies
3. **Centralize logs** - Forward to SIEM/log aggregation system (e.g., Splunk, ELK Stack)
4. **Alert on critical events** - Configure automated alerts for CRITICAL and ALERT severity
5. **Secure the logs** - Restrict access and prevent tampering with file permissions
6. **Compliance** - Maintain logs for regulatory compliance (SOC 2, ISO 27001, GDPR, HIPAA)
7. **Document incidents** - Always populate ADMIN_NOTE field with resolution details
8. **Monitor log size** - Watch disk usage for log files and archive promptly
9. **Audit access** - Log all access to audit logs themselves (meta-logging)
10. **Automate responses** - Use event data to trigger automated incident response workflows

## Integration with SIEM Systems

### Splunk Configuration

```ini
[monitor://./SENTINEL_SECURITY_AUDIT.log]
sourcetype = sentinel:audit
index = security
timestamp_regex = ^\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)
```

### ELK Stack (Filebeat)

```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/sentinel/SENTINEL_SECURITY_AUDIT.log
  fields:
    service: sentinel
    env: production
```

## Troubleshooting

### Common Issues

**Issue**: Large log file slowing down parsing
- **Solution**: Use grep with `-E` for extended regex or pipe to `head`/`tail` for date range filtering

**Issue**: Missing fields in log entry
- **Solution**: Check that all pipe delimiters are present; ensure no field values contain unescaped pipes

**Issue**: Timestamps not parsing correctly
- **Solution**: Verify ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ); all timestamps must be UTC

## Change Log

| Date | Version | Changes |
|------|---------|---------|
| 2026-05-18 | 1.0 | Initial structured log format with pipe-delimited fields |
| 2026-06-06 | 1.1 | Added SIEM integration examples and parsing guides |

## Related Files

- `SENTINEL_SECURITY_AUDIT.log` - Main audit log file
- `sentinel-config.yaml` - Security configuration
- `LOG_ROTATION_POLICY.md` - Log rotation and archival procedures
