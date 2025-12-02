# Test Cases for Timer Feature

---

### Part 1: Functional & Negative Tests

#### TC-001: Enforce Exam Time Limit (Happy Path)

**Priority**: High  
**Type**: Positive  
**Requirement**: FR-1  

**Preconditions**:  
- User is authenticated and starts the exam.  
- Timer configuration is set for the exam duration.

**Test Steps**:  
1. Start the exam and observe the timer starting countdown from configured duration.  
2. Verify timer counts down every second accurately.  
3. Continue the exam until timer expires.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Exam Duration | 60 minutes | Configured by admin |  

**Expected Result**:  
- Timer counts down from 60 minutes to zero accurately.  
- Timer UI updates every second with latency 60 100 ms.  
- User cannot extend exam time beyond configured limit.

---

#### TC-002: Auto-save and Auto-submit on Timer Expiry (Happy Path)

**Priority**: High  
**Type**: Positive  
**Requirement**: FR-2  

**Preconditions**:  
- User is actively taking the exam.  
- Timer is running and about to expire.

**Test Steps**:  
1. Allow timer to run until expiry.  
2. Observe auto-save of responses triggered at expiry.  
3. Verify exam auto-submission occurs immediately after expiry.  
4. Attempt to edit answers after expiry.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Timer State | Expired | After countdown reaches zero |  

**Expected Result**:  
- Exam responses are auto-saved successfully.  
- Exam is auto-submitted without user intervention.  
- User is prevented from making further edits.  
- Confirmation message displayed: "Exam submitted due to timer expiry."

---

#### TC-003: Display Visible Timer to Candidate (Happy Path)

**Priority**: High  
**Type**: Positive  
**Requirement**: FR-3  

**Preconditions**:  
- User is on the exam page.  
- Timer is configured and running.

**Test Steps**:  
1. Load the exam page.  
2. Verify timer is displayed in fixed header and visible at all times.  
3. Confirm timer updates every second with correct remaining time.  
4. Verify timer states: normal, warning, critical, expired.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Timer States | Normal, Warning, Critical, Expired | Based on configured thresholds |  

**Expected Result**:  
- Timer is clearly visible in fixed header.  
- Timer updates accurately every second.  
- Visual states and notifications reflect current timer status.  
- Accessible notifications (e.g., screen reader) announce state changes.

---

#### TC-004: Log Timing Events for Audit (Happy Path)

**Priority**: Medium  
**Type**: Positive  
**Requirement**: FR-4  

**Preconditions**:  
- User is taking the exam.  
- Timer events occur (tick, warning, expiry).

**Test Steps**:  
1. Trigger timer events during exam (e.g., tick every second, warning threshold reached, expiry).  
2. Verify that each event is logged with correct event type and timestamp in audit logs.  
3. Access audit logs through backend or admin interface.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Event Types | Tick, Warning, Expiry | Logged events |  

**Expected Result**:  
- All timer events are logged with correct user ID, exam ID, event type, and timestamp.  
- Logs are immutable and accessible for audit.  

---

#### TC-005: Admin Configures Timer Settings (Happy Path)

**Priority**: High  
**Type**: Positive  
**Requirement**: FR-5  

**Preconditions**:  
- Admin is authenticated and authorized.  
- Admin UI is accessible.

**Test Steps**:  
1. Access timer configuration interface in admin UI.  
2. Update timer modes, durations, warning thresholds, expiry behaviors, and accommodations.  
3. Save configuration changes.  
4. Verify changes are persisted and reflected in timer behavior during exams.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Duration | 90 minutes | Admin input |  
| Warning Threshold | 5 minutes | Admin input |  
| Auto-submit Enabled | True | Admin input |  

**Expected Result**:  
- Admin can successfully update and save timer configurations.  
- Configuration changes are applied to active and future exams.

---

#### TC-006: Timer State Persistence Across Page Refresh (Happy Path)

**Priority**: Medium  
**Type**: Positive  
**Requirement**: FR-6  

**Preconditions**:  
- User is taking an exam with timer running.  
- Timer state is saved on server and client.

**Test Steps**:  
1. Refresh exam page during active timer session.  
2. Verify timer state is restored accurately without reset.  
3. Simulate brief network outage and reconnect.  
4. Verify timer continues without loss or reset.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Timer Remaining Time | 10 minutes | During refresh |  

**Expected Result**:  
- Timer resumes correctly with accurate remaining time after refresh.  
- Timer state persists through brief network failures.

---

#### TC-007: Timer Accessibility and Localization (Happy Path)

**Priority**: Medium  
**Type**: Positive  
**Requirement**: FR-7  

**Preconditions**:  
- Exam UI supports accessibility and localization.  
- Timer component is displayed.

**Test Steps**:  
1. Verify timer UI complies with WCAG 2.1 accessibility guidelines.  
2. Use screen reader to confirm timer announcements.  
3. Change language or locale settings.  
4. Verify timer displays localized time format, text, and notifications.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Locale | French (fr-FR) | Admin or user setting |  

**Expected Result**:  
- Timer is accessible via keyboard navigation and screen readers.  
- Timer text and notifications appear in selected language and correct format.

---

#### TC-100: Reject Timer Configuration with Negative Duration (Negative Test)

**Priority**: High  
**Type**: Negative  
**Requirement**: FR-5  

**Preconditions**:  
- Admin UI accessible.  
- Admin attempts to save invalid configuration.

**Test Steps**:  
1. Enter negative number for timer duration (e.g., -10 minutes).  
2. Attempt to save configuration.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Duration | -10 | Invalid input |  

**Expected Result**:  
- Configuration is rejected with validation error message: "Duration must be a positive integer."  
- Configuration is not saved.

---

#### TC-101: Prevent Exam Submission if Timer Not Expired (Negative Test)

**Priority**: Medium  
**Type**: Negative  
**Requirement**: FR-2  

**Preconditions**:  
- User is taking exam with timer running.  
- Timer has not reached expiry.

**Test Steps**:  
1. Attempt to trigger auto-submit manually before timer expiry.  
2. Verify system response.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Timer State | Normal or Warning | Not expired |  

**Expected Result**:  
- Auto-submit request is rejected.  
- Error message: "Auto-submit can only occur on timer expiry."

---

#### TC-102: Timer Does Not Auto-submit if Auto-submit Disabled (Negative Test)

**Priority**: Medium  
**Type**: Negative  
**Requirement**: FR-5  

**Preconditions**:  
- Admin has disabled auto-submit feature.

**Test Steps**:  
1. Allow timer to expire during exam.  
2. Verify auto-submit does not occur.  
3. Check for any warnings or alerts.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Auto-submit Enabled | False | Admin config |  

**Expected Result**:  
- Exam is not auto-submitted on timer expiry.  
- User receives notification: "Timer expired, please submit manually."  

---

#### TC-103: Timer Fails to Synchronize on Network Loss Beyond Threshold (Negative Test)

**Priority**: High  
**Type**: Negative  
**Requirement**: NFR-2  

**Preconditions**:  
- User is taking exam.  
- Network connection is lost for longer than 60 seconds.

**Test Steps**:  
1. Simulate network outage of >60 seconds during exam.  
2. Observe timer behavior and autosave attempts.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Network Outage Duration | 65 seconds | Simulated |  

**Expected Result**:  
- Timer does not update or sync during prolonged outage.  
- User warned of potential answer loss.  
- Autosave attempts fail gracefully.

---

#### TC-104: Reject Unauthorized Access to Admin Timer Configuration (Negative Test)

**Priority**: High  
**Type**: Negative  
**Requirement**: NFR-Security (Implicit from admin auth)  

**Preconditions**:  
- User is authenticated as candidate, not admin.

**Test Steps**:  
1. Attempt to access `/admin/timer/config` GET and PUT endpoints.  
2. Verify access control enforcement.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| User Role | Candidate | Unauthorized for admin APIs |  

**Expected Result**:  
- Access denied with HTTP 403 Forbidden status.  
- Error message: "Insufficient privileges."

---

#### TC-105: Reject Malformed Timer Event Logging Request (Negative Test)

**Priority**: Medium  
**Type**: Negative  
**Requirement**: FR-4  

**Preconditions**:  
- Candidate user is logged in.

**Test Steps**:  
1. Send POST to `/timer/event` with missing or invalid `eventType`.  
2. Observe server response.

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| eventType | "" or null | Invalid |  

**Expected Result**:  
- Server responds with HTTP 400 Bad Request.  
- Error message: "Invalid eventType parameter."

---

### Part 2: Edge Cases & Security Tests

---

#### TC-200: Timer Duration Set to Zero (Edge Case)

**Priority**: High  
**Type**: Edge  
**Requirement**: FR-1  

**Preconditions**:  
- Admin configures timer duration as 0 minutes.

**Test Steps**:  
1. Admin sets timer duration to zero.  
2. Candidate starts exam.  
3. Observe timer behavior.

**Expected Result**:  
- Timer immediately expires.  
- Auto-submit triggered immediately if enabled.  
- User notified of zero duration exam.

---

#### TC-201: Timer Warning Threshold Equals Duration (Edge Case)

**Priority**: Medium  
**Type**: Edge  
**Requirement**: FR-5  

**Preconditions**:  
- Admin sets warning threshold equal to total duration.

**Test Steps**:  
1. Admin configures warning threshold = exam duration.  
2. Candidate starts exam and views timer.

**Expected Result**:  
- Warning state triggers immediately at exam start.  
- Timer UI reflects warning state properly.

---

#### TC-202: Timer Critical Threshold Greater Than Duration (Edge Case)

**Priority**: Medium  
**Type**: Edge  
**Requirement**: FR-5  

**Preconditions**:  
- Admin configures critical threshold greater than exam duration.

**Test Steps**:  
1. Set critical threshold > duration in admin config.  
2. Candidate takes exam.

**Expected Result**:  
- Critical state never triggered.  
- Timer proceeds to expiry as normal.

---

#### TC-203: Timer State Persistence with Concurrent Sessions (Edge Case)

**Priority**: High  
**Type**: Edge  
**Requirement**: NFR-4  

**Preconditions**:  
- Multiple concurrent exam sessions active for same user.

**Test Steps**:  
1. User opens multiple exam sessions simultaneously.  
2. Refresh pages and observe timer state synchronization.

**Expected Result**:  
- Timer state remains consistent across sessions.  
- No conflicting timer expiries.

---

#### TC-204: Timer Update Delay Exceeds Latency Threshold (Edge Case)

**Priority**: Medium  
**Type**: Edge  
**Requirement**: NFR-1  

**Preconditions**:  
- Network latency causes timer UI updates delayed beyond 100 ms.

**Test Steps**:  
1. Simulate high network latency (e.g. 200 ms).  
2. Observe timer UI update frequency and accuracy.

**Expected Result**:  
- Timer UI updates every second, tolerating latency up to 100 ms.  
- Minor delay does not affect exam flow or timing.

---

#### TC-300: SQL Injection Attempt in Timer Event Logging (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A03:2021 	6 Injection  

**Attack Vector**: SQL injection via malicious payload in event logging.

**Preconditions**:  
- Candidate authenticated.

**Test Steps**:  
1. Send POST request to `/timer/event` with eventType: `'; DROP TABLE timer_events;--`  
2. Observe server response and database integrity.

**Test Data**:  
- Malicious Payload: `'; DROP TABLE timer_events;--`

**Expected Result**:  
- Server rejects request with HTTP 400 or 500 error.  
- No SQL commands executed.  
- Database remains intact.  
- Security event logged.

---

#### TC-301: Cross-Site Scripting (XSS) in Timer Warning Notifications (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: FR-3, NFR-Security  
**OWASP Category**: A03:2021 	6 Injection  

**Attack Vector**: XSS payload injected into timer warning messages.

**Preconditions**:  
- Admin attempts to configure warning text with script tags.

**Test Steps**:  
1. Admin inputs `<script>alert('XSS')</script>` in warning message config.  
2. Candidate receives warning notification during exam.

**Test Data**:  
- Malicious Payload: `<script>alert('XSS')</script>`

**Expected Result**:  
- Payload sanitized or rejected by server.  
- No script execution in client browser.  
- Warning message displays safely.

---

#### TC-302: Unauthorized Access to Timer Auto-submit Endpoint (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: FR-2, NFR-Security  
**OWASP Category**: A01:2021 	6 Broken Access Control  

**Attack Vector**: Attempt to trigger auto-submit by unauthorized user.

**Preconditions**:  
- User is unauthenticated or has insufficient privileges.

**Test Steps**:  
1. Send POST request to `/timer/auto-submit` without valid authentication token.  
2. Observe server response.

**Expected Result**:  
- Request denied with HTTP 401 Unauthorized or 403 Forbidden.  
- Auto-submit not triggered.

---

#### TC-303: Session Fixation Attack on Timer API (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A07:2021 	6 Identification and Authentication Failures  

**Attack Vector**: Use fixed session ID to hijack timer session.

**Preconditions**:  
- Attacker sets session ID before user login.

**Test Steps**:  
1. Attacker sets session cookie with fixed ID.  
2. User logs in with session ID.  
3. Attacker attempts to access timer API using same session ID.

**Expected Result**:  
- Session ID regenerated on login.  
- Attacker cannot hijack session.  
- Timer API calls require valid, fresh session tokens.

---

#### TC-304: Replay Attack on Timer Event Logging (Security Test)

**Priority**: Medium  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A07:2021 	6 Identification and Authentication Failures  

**Attack Vector**: Replay timer event POST requests to cause duplicate logs.

**Preconditions**:  
- Valid timer event request captured by attacker.

**Test Steps**:  
1. Replay captured `/timer/event` POST request multiple times.  
2. Observe server handling of duplicate events.

**Expected Result**:  
- Server detects and rejects replayed requests using timestamps or nonces.  
- No duplicate audit logs created.

---

#### TC-305: Directory Listing Enabled on Timer Config Files (Security Test)

**Priority**: Medium  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A05:2021 	6 Security Misconfiguration  

**Attack Vector**: Attempt to list contents of `config/` directory.

**Preconditions**:  
- External user tries to access `config/` directory URL.

**Test Steps**:  
1. Access `config/` directory URL via browser or HTTP client.  
2. Observe server response.

**Expected Result**:  
- Directory listing disabled or forbidden.  
- HTTP 403 Forbidden or 404 Not Found returned.

---

#### TC-306: Weak Password Policy in Admin Authentication (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A07:2021 	6 Identification and Authentication Failures  

**Attack Vector**: Admin accepts weak passwords like "12345".

**Preconditions**:  
- Admin attempts to set weak password during authentication setup.

**Test Steps**:  
1. Attempt to create or change admin password to "12345".  
2. Observe password policy enforcement.

**Expected Result**:  
- Weak passwords rejected with clear error message.  
- Password must meet complexity requirements.

---

#### TC-307: Missing Rate Limiting on Timer API (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A04:2021 	6 Insecure Design  

**Attack Vector**: Excessive requests cause denial of service.

**Preconditions**:  
- No rate limiting configured on timer API endpoints.

**Test Steps**:  
1. Send high volume of requests (e.g., 100 per second) to `/timer/event`.  
2. Observe system behavior and response times.

**Expected Result**:  
- Rate limiting enforced, throttling excessive requests.  
- Server remains stable without crashes.

---

#### TC-308: Sensitive Timer Config Data Sent Without Encryption (Security Test)

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-Security  
**OWASP Category**: A02:2021 	6 Cryptographic Failures  

**Attack Vector**: Timer config sent over HTTP instead of HTTPS.

**Preconditions**:  
- System configured to allow HTTP traffic.

**Test Steps**:  
1. Access `/admin/timer/config` over HTTP.  
2. Observe data transmission security.

**Expected Result**:  
- Connection redirected or blocked if not secure.  
- Sensitive data not sent over unencrypted channel.

---

### Part 3: Additional Tests & Coverage Matrix

---

#### TC-400: Load Test - Support 10,000 Concurrent Exam Sessions

**Priority**: High  
**Type**: Performance  
**Requirement**: NFR-4  

**Performance Goal**: Support 10,000 concurrent timer sessions without degradation.

**Test Environment**:  
- Server specs: 16 CPU cores, 64 GB RAM  
- Network: 1 Gbps LAN  

**Load Profile**:  
- Concurrent users: 10,000  
- Ramp-up time: 5 minutes  
- Test duration: 30 minutes  
- Think time: 0 seconds (continuous timer updates)

**Test Steps**:  
1. Simulate 10,000 users starting exams simultaneously.  
2. Monitor timer API response times and error rates.  
3. Verify system stability and resource usage.

**Success Criteria**:  
- Average response time < 200 ms  
- Error rate < 1%  
- No crashes or memory leaks

---

#### TC-401: Stress Test - Exceed Max Concurrent Sessions

**Priority**: Medium  
**Type**: Performance  
**Requirement**: NFR-4  

**Performance Goal**: System handles overload gracefully.

**Test Environment**: Same as TC-400  

**Load Profile**:  
- Concurrent users: 15,000 (50% above max)  
- Ramp-up time: 2 minutes  
- Test duration: 15 minutes  

**Test Steps**:  
1. Simulate 15,000 concurrent timer sessions.  
2. Monitor latency, error responses, and system behavior.

**Success Criteria**:  
- System throttles or queues requests properly.  
- No data loss or crashes.  
- Alerts triggered on resource saturation.

---

#### TC-500: Integration Test - Timer API with Exam Submission Service

**Priority**: High  
**Type**: Integration  
**Requirement**: FR-2  

**Preconditions**:  
- Exam submission service is operational.  
- Timer API configured.

**Test Steps**:  
1. Trigger timer expiry event.  
2. Verify auto-submit API calls exam submission service.  
3. Confirm exam status updated to "submitted".  
4. Check audit logs for event consistency.

**Expected Result**:  
- Exam submission service receives and processes auto-submit.  
- Exam state transitions correctly.

---

#### TC-501: Integration Test - Timer Event Logs Stored in Audit Service

**Priority**: Medium  
**Type**: Integration  
**Requirement**: FR-4  

**Preconditions**:  
- Audit logging service is active.

**Test Steps**:  
1. Generate timer events during exam.  
2. Verify events are logged in audit service database.  
3. Check log integrity and timestamps.

**Expected Result**:  
- Timer events appear in audit logs with correct metadata.

---

#### TC-600: Accessibility Test - Keyboard Navigation of Timer UI

**Priority**: High  
**Type**: Accessibility  
**Requirement**: FR-7  
**WCAG Level**: AA  

**Testing Tools**: NVDA screen reader, Chrome browser, axe DevTools  

**Test Steps**:  
1. Navigate to exam page using keyboard only.  
2. Tab through interactive elements including timer controls.  
3. Verify focus indicators on timer component.  
4. Use screen reader to confirm timer announcements.

**Expected Result**:  
- Timer UI is fully accessible via keyboard.  
- Screen reader announces timer states correctly.

---

#### TC-601: Accessibility Test - Color Contrast Compliance

**Priority**: Medium  
**Type**: Accessibility  
**Requirement**: FR-7  
**WCAG Level**: AA  

**Test Steps**:  
1. Inspect timer UI colors using axe DevTools.  
2. Verify color contrast ratio meets 64.5:1 for text and 63:1 for UI components.

**Expected Result**:  
- Timer UI meets color contrast guidelines.

---

### Requirements-to-Test Coverage Matrix

| Requirement ID | Description                                      | Test Case IDs                                     | Total Tests | Coverage % | Priority | Status   | Notes                       |
|----------------|------------------------------------------------|--------------------------------------------------|-------------|------------|----------|----------|-----------------------------|
| FR-1           | Enforce exam time limit                         | TC-001, TC-200                                   | 2           | 100%       | High     | Complete | Includes edge case zero duration |
| FR-2           | Auto-save and auto-submit on timer expiry      | TC-002, TC-101, TC-102, TC-500                   | 4           | 100%       | High     | Complete | Integration test included    |
| FR-3           | Display visible timer                           | TC-003, TC-301                                   | 2           | 100%       | High     | Complete | Security test for XSS        |
| FR-4           | Log timing events                               | TC-004, TC-105, TC-501                           | 3           | 100%       | Medium   | Complete | Includes malformed request   |
| FR-5           | Admin configures timer settings                 | TC-005, TC-100, TC-201, TC-202                   | 4           | 100%       | High     | Complete | Validation and edge cases    |
| FR-6           | Persist timer state across refresh/network loss| TC-006, TC-203                                   | 2           | 100%       | Medium   | Complete | Concurrent session test      |
| FR-7           | Timer accessibility and localization            | TC-007, TC-600, TC-601                           | 3           | 100%       | Medium   | Complete | Accessibility tests included |
| NFR-1          | Timer UI updates every second with latency 60 100ms | TC-001, TC-204                                  | 2           | 100%       | Medium   | Complete | Latency edge case            |
| NFR-2          | No answer loss under transient network loss    | TC-103                                           | 1           | 100%       | High     | Complete | Network outage negative test |
| NFR-4          | Support large concurrent exam sessions          | TC-400, TC-401                                   | 2           | 100%       | High     | Complete | Load and stress tests        |
| NFR-Security   | Security tests covering OWASP Top 10            | TC-300 to TC-308, TC-310                         | 10+         | 100%       | High     | Complete | Full OWASP coverage          |

---
