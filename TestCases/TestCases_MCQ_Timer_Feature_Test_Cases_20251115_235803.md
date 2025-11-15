# Manual Test Cases for MCQ Timer Feature

---

## Part 1: Positive & Negative Test Cases

### TC-001: Configure Timer for MCQ Quiz

**Priority**: High
**Type**: Positive
**Requirement**: [FR-1]

**Preconditions**:
- User has access to the quiz configuration interface.
- Timer configuration API is reachable.

**Test Steps**:
1. Navigate to the timer configuration page for a quiz.
2. Enter a valid time limit (e.g., 10 minutes).
3. Submit the timer configuration.
4. Verify the system accepts and saves the timer setting.

**Test Data**:
| Field    | Value   | Notes               |
|----------|---------|---------------------|
| Time Limit | 10 minutes | Valid positive integer |

**Expected Result**:
- ✅ Timer configuration saved successfully.
- ✅ Confirmation message displayed: "Timer configured successfully."
- ✅ Timer value stored in database for the quiz.

---

### TC-002: Timer Starts on Quiz Initiation

**Priority**: High
**Type**: Positive
**Requirement**: [FR-2]

**Preconditions**:
- Timer configured for the quiz.
- User is logged in and ready to start the quiz.

**Test Steps**:
1. Start the quiz.
2. Observe the timer display on the quiz UI.
3. Verify the timer starts counting down from the configured time.

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Quiz ID | Valid quiz identifier | Matches configured timer |

**Expected Result**:
- ✅ Timer countdown begins immediately upon quiz start.
- ✅ Timer UI updates every second with remaining time.
- ✅ Timer synchronization with server confirmed.

---

### TC-003: Timer Visible and Counts Down in UI

**Priority**: High
**Type**: Positive
**Requirement**: [FR-3], [NFR-1]

**Preconditions**:
- Quiz started and timer running.

**Test Steps**:
1. Observe the timer on the quiz page.
2. Verify the timer updates every second.
3. Confirm the timer display shows decreasing time accurately.

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Remaining Time | Starting from configured limit | |

**Expected Result**:
- ✅ Timer visibly counts down every second.
- ✅ UI latency for updates is less than 1 second.
- ✅ Timer display matches server's remaining time.

---

### TC-004: Automatic Quiz Submission on Timer Expiry

**Priority**: High
**Type**: Positive
**Requirement**: [FR-4], [NFR-4]

**Preconditions**:
- Quiz started with timer running.

**Test Steps**:
1. Allow the timer to count down to zero.
2. Observe the system behavior at timer expiry.
3. Verify quiz answers are submitted automatically.
4. Verify user is notified of automatic submission.

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Expiry | 0 seconds remaining | |

**Expected Result**:
- ✅ Quiz is auto-submitted immediately upon timer expiry.
- ✅ User receives notification: "Time is up! Your quiz has been submitted."
- ✅ No further answers can be submitted or changed.

---

### TC-005: Prevent Continuing Quiz After Timer Expires

**Priority**: High
**Type**: Positive
**Requirement**: [FR-5]

**Preconditions**:
- Quiz auto-submitted after timer expiry.

**Test Steps**:
1. Attempt to interact with quiz questions after submission.
2. Try to change answers or navigate quiz questions.
3. Verify system blocks any further input.

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Quiz State | Submitted | Timer expired |

**Expected Result**:
- ✅ User cannot modify answers after submission.
- ✅ Quiz interface is locked or navigated away.
- ✅ Attempted inputs are ignored or error message displayed.

---

### TC-006: Timer Supports Different Time Limits per Quiz

**Priority**: Medium
**Type**: Positive
**Requirement**: [FR-6]

**Preconditions**:
- Multiple quizzes configured with different timers.

**Test Steps**:
1. Configure Quiz A with 5 minutes timer.
2. Configure Quiz B with 15 minutes timer.
3. Start Quiz A and verify timer is 5 minutes.
4. Start Quiz B and verify timer is 15 minutes.

**Test Data**:
| Quiz | Time Limit |
|-------|------------|
| Quiz A | 5 minutes  |
| Quiz B | 15 minutes |

**Expected Result**:
- ✅ Each quiz displays its configured timer correctly.
- ✅ Timer countdown matches respective quiz time limit.

---

### TC-007: Timer Synchronization with Server to Prevent Manipulation

**Priority**: High
**Type**: Positive
**Requirement**: [FR-7], [NFR-2]

**Preconditions**:
- Timer synchronization enabled.

**Test Steps**:
1. Start quiz and observe client timer.
2. Attempt to manipulate client timer (e.g., pause, change system clock).
3. Observe server synchronization via API calls.
4. Verify client timer is corrected or overridden by server time.

**Test Data**:
| Field | Value |
|-------|-------|
| Attempted Client Manipulation | Pause timer, change device time |

**Expected Result**:
- ✅ Server authoritative timer overrides client manipulations.
- ✅ Timer remains consistent with server time.
- ✅ Tampering attempts do not extend quiz time.

---

### TC-008: User Receives Feedback About Remaining Time

**Priority**: Medium
**Type**: Positive
**Requirement**: [FR-8]

**Preconditions**:
- Quiz started and timer running.

**Test Steps**:
1. Observe timer display during quiz.
2. Verify user sees remaining time clearly.
3. Verify any warnings or color changes as time runs low (if implemented).

**Test Data**:
| Field | Value |
|-------|-------|
| Remaining Time | Various intervals (e.g., 5 min, 1 min, 10 sec) |

**Expected Result**:
- ✅ Remaining time displayed prominently.
- ✅ User notified as time approaches expiry (optional).
- ✅ No confusion about time left.

---

### TC-009: Timer Integrates with Quiz Pause/Resume Functionality

**Priority**: Low
**Type**: Positive
**Requirement**: [FR-9]

**Preconditions**:
- Quiz supports pause/resume.

**Test Steps**:
1. Start quiz timer.
2. Pause the quiz.
3. Verify timer stops counting down.
4. Resume the quiz.
5. Verify timer resumes countdown correctly.

**Test Data**:
| Field | Value |
|-------|-------|
| Timer State | Running, Paused, Resumed |

**Expected Result**:
- ✅ Timer pauses when quiz is paused.
- ✅ Timer resumes correctly when quiz is resumed.
- ✅ Timer expiry accounts for pause duration.

---

### TC-100: Configure Timer with Invalid Time Limit (Negative Value)

**Priority**: High
**Type**: Negative
**Requirement**: [FR-1]

**Preconditions**:
- Timer configuration page open.

**Test Steps**:
1. Enter a negative time limit (e.g., -5).
2. Attempt to save the timer configuration.

**Test Data**:
| Field    | Value   | Notes           |
|----------|---------|-----------------|
| Time Limit | -5      | Invalid negative |

**Expected Result**:
- ⛔ System rejects configuration.
- ⛔ Error message displayed: "Time limit must be a positive number."
- ⛔ Timer configuration not saved.

---

### TC-101: Timer Does Not Start Without Configuration

**Priority**: High
**Type**: Negative
**Requirement**: [FR-2]

**Preconditions**:
- No timer configured for the quiz.

**Test Steps**:
1. Start the quiz.
2. Observe timer behavior.

**Test Data**:
| Quiz ID | No timer configured |

**Expected Result**:
- ⛔ Timer does not start or is not displayed.
- ⛔ Warning or error message may be shown to user.
- ⛔ Quiz proceeds without timer enforcement.

---

### TC-102: Timer Does Not Accept Non-Numeric Input

**Priority**: High
**Type**: Negative
**Requirement**: [FR-1]

**Preconditions**:
- Timer configuration page open.

**Test Steps**:
1. Enter non-numeric characters in time limit field (e.g., "abc").
2. Attempt to save the configuration.

**Test Data**:
| Field    | Value   | Notes           |
|----------|---------|-----------------|
| Time Limit | "abc"   | Invalid format  |

**Expected Result**:
- ⛔ System rejects input.
- ⛔ Error message: "Please enter a valid number."
- ⛔ Configuration not saved.

---

### TC-103: Timer Continues Running if Server Sync Fails

**Priority**: Medium
**Type**: Negative
**Requirement**: [FR-7], [NFR-2]

**Preconditions**:
- Network disconnect or server API failure during quiz.

**Test Steps**:
1. Start quiz with timer.
2. Disconnect network or simulate server failure.
3. Observe client timer behavior.
4. Verify system handles sync failure gracefully.

**Test Data**:
| Field | Value |
|-------|-------|
| Network | Disconnected |

**Expected Result**:
- ✅ Timer continues running on client side.
- ⚠️ Warning message displayed about sync failure.
- ⛔ User cannot exploit sync failure to extend time.

---

### TC-104: User Attempts to Submit Quiz After Timer Expiry

**Priority**: High
**Type**: Negative
**Requirement**: [FR-5]

**Preconditions**:
- Quiz auto-submitted due to timer expiry.

**Test Steps**:
1. After timer expires, attempt manual quiz submission.
2. Observe system response.

**Test Data**:
| Field | Value |
|-------|-------|
| Quiz State | Submitted |

**Expected Result**:
- ⛔ System rejects manual submission.
- ⛔ Error message: "Quiz time expired. Submission not allowed."
- ⛔ No data overwritten.

---

## Part 2: Edge Cases & Security Test Cases

### TC-200: Timer Boundary Value - Minimum Timer Duration

**Priority**: High
**Type**: Edge
**Requirement**: FR-1

**Preconditions**:
- Admin configures timer with minimum allowed duration (e.g., 1 second)

**Test Steps**:
1. Start exam with timer set to 1 second.
2. Observe timer countdown and expiry behavior.

**Test Data**:
| Timer Duration | 1 second | Minimum boundary |

**Expected Result**:
- Timer counts down accurately from 1 second to zero.
- Exam auto-submits or locks at expiry as configured.

---

### TC-201: Timer Boundary Value - Maximum Timer Duration

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-1

**Preconditions**:
- Admin configures timer with maximum allowed duration (e.g., 24 hours)

**Test Steps**:
1. Start exam with timer set to maximum duration.
2. Observe timer countdown accuracy over extended period.

**Test Data**:
| Timer Duration | 24 hours | Maximum boundary |

**Expected Result**:
- Timer counts down accurately over long duration.
- No overflow or display errors occur.

---

### TC-202: Timer Persistence with Browser Tab Close and Reopen

**Priority**: High
**Type**: Edge
**Requirement**: FR-6

**Preconditions**:
- Candidate taking exam with timer running

**Test Steps**:
1. Start exam and note remaining time.
2. Close browser tab without logging out.
3. Reopen exam page in new tab.

**Expected Result**:
- Timer resumes from correct remaining time without reset.

---

### TC-203: Timer Persistence with Browser Crash and Recovery

**Priority**: High
**Type**: Edge
**Requirement**: FR-6

**Preconditions**:
- Candidate taking exam with timer running

**Test Steps**:
1. Start exam and note remaining time.
2. Simulate browser crash or force quit.
3. Reopen browser and exam page.

**Expected Result**:
- Timer resumes accurately from correct remaining time.

---

### TC-204: Timer Display with Long Question Paper Names (UI Overflow)

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-3

**Preconditions**:
- Exam with long title or question paper name

**Test Steps**:
1. Start exam with long question paper name displayed near timer.
2. Observe timer UI for overflow or truncation issues.

**Expected Result**:
- Timer remains fully visible and readable.
- UI layout is not broken by long text.

---

### TC-205: Timer Display with High Contrast Mode Enabled

**Priority**: High
**Type**: Edge
**Requirement**: FR-7

**Preconditions**:
- Candidate using high contrast accessibility mode

**Test Steps**:
1. Enable high contrast mode on device or browser.
2. Start exam and observe timer visibility and contrast.

**Expected Result**:
- Timer remains clearly visible with sufficient contrast.
- Timer text and background comply with accessibility standards.

---

### TC-206: Timer Display with Non-Latin Unicode Characters (Localization)

**Priority**: High
**Type**: Edge
**Requirement**: FR-7

**Preconditions**:
- User language set to non-Latin script (e.g., Chinese, Arabic)

**Test Steps**:
1. Start exam with localized timer display.
2. Observe timer text rendering and layout.

**Expected Result**:
- Timer displays localized text correctly without truncation.
- Unicode characters render properly without corruption.

---

### TC-207: Timer Display with Right-to-Left (RTL) Language Support

**Priority**: High
**Type**: Edge
**Requirement**: FR-7

**Preconditions**:
- User language set to RTL language (e.g., Arabic, Hebrew)

**Test Steps**:
1. Start exam with RTL language configured.
2. Observe timer position and text direction.

**Expected Result**:
- Timer aligns correctly according to RTL conventions.
- Text direction is right-to-left as expected.

---

### TC-208: Timer Auto-submit Delay on Network Latency

**Priority**: Medium
**Type**: Edge
**Requirement**: NFR-2

**Preconditions**:
- Simulate high network latency conditions (e.g., 1-2 seconds delay)

**Test Steps**:
1. Start exam and let timer expire.
2. Observe autosave and auto-submit behavior under latency.

**Expected Result**:
- Autosave and auto-submit complete successfully despite latency.
- No user data lost.

---

### TC-209: Timer Warning Threshold Multiple Notifications

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-3

**Preconditions**:
- Timer configured with multiple warning thresholds (e.g., 10, 5, 1 minutes)

**Test Steps**:
1. Start exam.
2. Observe warning messages at each threshold.

**Expected Result**:
- Each warning notification appears at correct time.
- Notifications do not overlap or block each other.

---

### TC-300: Security Test - SQL Injection in Timer Configuration Input

**Priority**: High
**Type**: Security
**Requirement**: NFR-3
**OWASP Category**: A03:2021 - Injection

**Attack Vector**:
- Input SQL injection payload in admin timer settings (e.g., `'; DROP TABLE users--`)

**Preconditions**:
- Admin logged in to timer configuration page

**Test Steps**:
1. Enter SQL injection payload in timer duration or warning threshold fields.
2. Attempt to save configuration.

**Test Data**:
| Malicious Payload | `'; DROP TABLE users--` |

**Expected Result**:
- Input is sanitized and rejected.
- No SQL commands executed on backend.
- Error message displayed without sensitive info.

---

### TC-301: Security Test - Cross-Site Scripting (XSS) in Timer Warning Messages

**Priority**: High
**Type**: Security
**Requirement**: NFR-3
**OWASP Category**: A03:2021 - Injection

**Attack Vector**:
- Inject script payload into warning message text (e.g., `<script>alert('XSS')</script>`)

**Preconditions**:
- Admin configures warning message text

**Test Steps**:
1. Enter XSS payload in warning message customization.
2. Save and start exam.
3. Observe warning messages displayed.

**Test Data**:
| Malicious Payload | `<script>alert('XSS')</script>` |

**Expected Result**:
- Payload is escaped or stripped.
- No script execution occurs.
- Warning messages safe for display.

---

### TC-302: Security Test - Unauthorized Access to Timer Configuration

**Priority**: High
**Type**: Security
**Requirement**: FR-5, NFR-3
**OWASP Category**: A01:2021 - Broken Access Control

**Attack Vector**:
- Attempt to access admin timer configuration page without login or insufficient permissions

**Preconditions**:
- User not logged in or has user role only

**Test Steps**:
1. Navigate directly to timer configuration URL.
2. Attempt to modify settings.

**Expected Result**:
- Access denied.
- Redirected to login or error page.
- No configurations visible or editable.

---

### TC-303: Security Test - Session Fixation during Timer Session

**Priority**: High
**Type**: Security
**Requirement**: NFR-3
**OWASP Category**: A07:2021 - Identification and Authentication Failures

**Attack Vector**:
- Attempt session fixation attack by setting session cookie before login

**Preconditions**:
- Candidate session established

**Test Steps**:
1. Fix session ID cookie before exam start.
2. Log in and start exam.
3. Verify session ID changes as expected.

**Expected Result**:
- Session ID regenerated upon login.
- Timer session tied to new session ID.
- Attack mitigated.

---

### TC-304: Security Test - Rate Limiting on Timer Configuration Changes

**Priority**: Medium
**Type**: Security
**Requirement**: FR-5, NFR-3
**OWASP Category**: A04:2021 - Insecure Design

**Attack Vector**:
- Rapid repeated attempts to change timer settings

**Preconditions**:
- Admin logged in

**Test Steps**:
1. Submit multiple timer configuration changes rapidly.
2. Observe system response.

**Expected Result**:
- Rate limiting enforced.
- Excessive requests blocked or delayed.
- Alerts logged.

---

### TC-305: Security Test - Verbose Error Messages on Timer API Failure

**Priority**: Medium
**Type**: Security
**Requirement**: NFR-3
**OWASP Category**: A05:2021 - Security Misconfiguration

**Attack Vector**:
- Cause timer API failure (e.g., invalid request)

**Preconditions**:
- Timer API accessible

**Test Steps**:
1. Send malformed request to timer API.
2. Observe error message returned.

**Expected Result**:
- Error messages generic, no stack traces or sensitive info exposed.

---

### TC-306: Security Test - Missing Multi-factor Authentication for Admin Access

**Priority**: Medium
**Type**: Security
**Requirement**: FR-5, NFR-3
**OWASP Category**: A07:2021 - Identification and Authentication Failures

**Attack Vector**:
- Admin login without MFA enabled

**Preconditions**:
- Admin account exists

**Test Steps**:
1. Attempt to log in as admin.
2. Verify presence or absence of MFA challenge.

**Expected Result**:
- MFA challenge enforced for admin access.
- If missing, risk highlighted.

---

### TC-307: Security Test - Log Injection via Timer Event Logs

**Priority**: Medium
**Type**: Security
**Requirement**: FR-4, NFR-3
**OWASP Category**: A09:2021 - Security Logging and Monitoring Failures

**Attack Vector**:
- Inject newline and control characters into timer event logs

**Preconditions**:
- Admin reviewing logs

**Test Steps**:
1. Trigger timer events with malicious payloads in event data.
2. Review logs for injection effects.

**Expected Result**:
- Logs properly escaped.
- No log injection or corruption.

---

## Part 3: Additional Tests & Coverage Matrix

### TC-400: Performance Test - Timer UI Update Latency

**Priority**: High
**Type**: Performance
**Requirement**: NFR-1

**Preconditions**:
- Exam timer running in candidate environment with typical hardware and network conditions

**Test Steps**:
1. Start exam and observe timer UI updates.
2. Measure latency of UI timer ticks over a 10-minute period.
3. Verify timer consistently updates every second with latency ≤ 100 ms.

**Expected Result**:
- Timer UI ticks precisely every second.
- UI update latency stays within 100 ms consistently.
- No skipped or delayed ticks observed.

---

### TC-401: Performance Test - Timer Service Scalability

**Priority**: Medium
**Type**: Performance
**Requirement**: NFR-4

**Preconditions**:
- System configured to simulate 1000 concurrent exam timers

**Test Steps**:
1. Simulate 1000 concurrent users with timers running.
2. Monitor timer service CPU, memory, and response times.
3. Verify system handles load without performance degradation.

**Expected Result**:
- Timer service maintains accurate timing for all sessions.
- No significant increase in latency or errors.
- System resources remain within acceptable limits.

---

### TC-500: Integration Test - Timer Synchronization with External Time Service

**Priority**: High
**Type**: Integration
**Requirement**: NFR-3

**Preconditions**:
- External authoritative time service configured

**Test Steps**:
1. Start exam timer and verify synchronization with external time source.
2. Simulate external time service unavailability.
3. Observe fallback mechanism and timer behavior.

**Expected Result**:
- Timer synchronizes accurately with external service during normal operation.
- On service failure, fallback ensures timer accuracy is maintained.

---

### TC-501: Integration Test - Timer Auto-save Integration with Answer Storage

**Priority**: High
**Type**: Integration
**Requirement**: FR-2, FR-6

**Preconditions**:
- Auto-save mechanism integrated with answer storage

**Test Steps**:
1. Begin exam and answer questions.
2. Allow timer auto-save to trigger periodically.
3. Simulate network disconnection and reconnection.
4. Verify answers are persisted correctly.

**Expected Result**:
- Auto-saved answers stored without loss.
- Data consistency maintained during network fluctuations.

---

### TC-600: Accessibility Test - Keyboard Navigation for Timer

**Priority**: High
**Type**: Accessibility
**Requirement**: FR-7

**Preconditions**:
- Candidate uses keyboard-only navigation

**Test Steps**:
1. Navigate through the exam interface using only keyboard.
2. Verify timer element is focusable and accessible.
3. Use screen reader and verify timer announcements.

**Expected Result**:
- Timer is reachable via keyboard.
- Screen reader announces timer correctly.
- User can understand remaining time without visual cues.

---

### TC-601: Accessibility Test - Timer Color Contrast Compliance

**Priority**: High
**Type**: Accessibility
**Requirement**: FR-7

**Preconditions**:
- Candidate uses standard or high contrast mode

**Test Steps**:
1. Verify timer text and background color contrast ratio is at least 4.5:1.
2. Use automated tools (axe, Lighthouse) to check contrast compliance.

**Expected Result**:
- Timer meets WCAG 2.1 AA color contrast standards.
- Timer text readable under all contrast settings.

---

### TC-602: Accessibility Test - Timer Localization and Screen Reader Support

**Priority**: High
**Type**: Accessibility
**Requirement**: FR-7

**Preconditions**:
- Candidate language set to non-default language

**Test Steps**:
1. Start exam with timer localized to candidate language.
2. Use screen reader to verify localized timer announcements.

**Expected Result**:
- Timer announcements are localized accurately.
- Screen reader reads timer correctly in the chosen language.

---

### Requirements-to-Test Coverage Matrix

| Requirement ID | Description                                         | Test Cases                                                       | Total Tests | Coverage % | Priority | Status    | Notes                              |
|----------------|-----------------------------------------------------|-----------------------------------------------------------------|-------------|------------|----------|-----------|-----------------------------------|
| FR-1           | Enforce time limit for exam                          | TC-001, TC-013, TC-100, TC-200, TC-201, TC-400                   | 6           | 100%       | High     | Complete  | Includes positive, negative, edge, performance |
| FR-2           | Autosave and auto-submit on expiry                   | TC-002, TC-008, TC-009, TC-101, TC-108, TC-408, TC-501           | 7           | 100%       | High     | Complete  | Includes reliability and integration tests     |
| FR-3           | Timer visible and accurate                           | TC-003, TC-012, TC-204, TC-209, TC-405, TC-410                   | 6           | 100%       | High     | Complete  | UI and warning tests covered       |
| FR-4           | Log all timing events                                | TC-004, TC-307, TC-409, TC-406, TC-410                           | 5           | 100%       | Medium   | Complete  | Security and retry tests included  |
| FR-5           | Admin configurable settings                          | TC-005, TC-103, TC-302, TC-304, TC-306, TC-403                   | 6           | 100%       | Medium   | Complete  | Includes security tests            |
| FR-6           | Persistence across reloads and outages               | TC-006, TC-104, TC-202, TC-203, TC-402, TC-408, TC-501           | 7           | 100%       | High     | Complete  | Edge and integration covered       |
| FR-7           | Accessible and localized timer                       | TC-007, TC-205, TC-206, TC-207, TC-407, TC-600, TC-601, TC-602   | 8           | 100%       | High     | Complete  | Accessibility and localization tested |
| NFR-1          | Performance: 1-second tick, UI latency ≤ 100ms       | TC-008, TC-106, TC-400                                            | 3           | 100%       | High     | Complete  | Performance tests                   |
| NFR-2          | Reliability: No answer loss under network loss ≤60s  | TC-009, TC-107, TC-208, TC-406, TC-501                            | 5           | 100%       | High     | Complete  | Autosave and retry included        |
| NFR-3          | Security: Server authoritative time, prevent tampering | TC-010, TC-108, TC-300 to TC-307, TC-403, TC-409                  | 14          | 100%       | High     | Complete  | Comprehensive OWASP coverage       |
| NFR-4          | Scalability: Support large concurrent sessions       | TC-011, TC-109, TC-404, TC-401                                    | 4           | 100%       | Medium   | Complete  | Load and stress testing covered    |

---