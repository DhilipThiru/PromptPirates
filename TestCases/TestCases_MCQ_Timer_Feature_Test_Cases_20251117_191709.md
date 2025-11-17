# Manual Test Cases for MCQ Timer Feature

---

### TC-001: Display Countdown Timer for Each Question

**Priority**: High
**Type**: Positive
**Requirement**: FR-1
**Preconditions**:
- Quiz application is running
- User is logged in and starts a quiz session

**Test Steps**:
1. Start a quiz session
2. Observe the UI for the countdown timer display for the first question
3. Verify the timer counts down from configured duration

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 30 seconds | Default duration |

**Expected Result**:
- ✅ Countdown timer visible and starts from configured duration
- ✅ Timer updates every second without UI lag

---

### TC-002: Auto-submit Incorrect Answer on Timer Expiry

**Priority**: High
**Type**: Positive
**Requirement**: FR-2
**Preconditions**:
- Quiz session started
- Timer running for current question

**Test Steps**:
1. Wait for timer to reach zero without submitting an answer
2. Observe system behavior

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 30 seconds | Default duration |

**Expected Result**:
- ✅ System auto-submits the current question as incorrect
- ✅ User receives feedback indicating time expired and incorrect answer
- ✅ Next question is displayed with timer reset

---

### TC-003: Pause and Reset Timer on New Question

**Priority**: High
**Type**: Positive
**Requirement**: FR-3
**Preconditions**:
- User has answered or timed out on a question
- Next question is about to display

**Test Steps**:
1. Complete or let timer expire on question N
2. Observe that timer for question N stops
3. Confirm timer for question N+1 starts fresh at configured duration

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 30 seconds | Default duration |

**Expected Result**:
- ✅ Previous timer is paused or cancelled
- ✅ New timer starts from full duration for next question

---

### TC-004: Display Timer Warning Near Expiry

**Priority**: Medium
**Type**: Positive
**Requirement**: FR-4
**Preconditions**:
- Timer running for current question

**Test Steps**:
1. Start timer for a question
2. Wait until timer reaches warning threshold (e.g., last 5 seconds)
3. Observe UI warning or visual indicator

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 30 seconds | Default duration |
| Warning Threshold | 5 seconds | Configured warning time |

**Expected Result**:
- ✅ Timer warning displayed visually (color change, blinking, or message)
- ✅ Warning activates exactly at threshold time

---

### TC-005: Configure Timer Duration Per Question

**Priority**: Medium
**Type**: Positive
**Requirement**: FR-5
**Preconditions**:
- Quiz with multiple questions having different timer durations

**Test Steps**:
1. Start quiz with questions configured with varying timer durations (e.g., Q1=20s, Q2=40s)
2. Observe timer duration for each question

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Question 1 Timer | 20 seconds | Custom duration |
| Question 2 Timer | 40 seconds | Custom duration |

**Expected Result**:
- ✅ Timer duration matches configured value per question
- ✅ Timer counts down accordingly for each question

---

### TC-006: Timer Does Not Cause UI Lag

**Priority**: High
**Type**: Positive
**Requirement**: NFR-1
**Preconditions**:
- Quiz running with timer enabled

**Test Steps**:
1. Start quiz and observe chat UI responsiveness while timer is active
2. Interact with chat (submit answer, navigate)

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|

**Expected Result**:
- ✅ No noticeable lag or delay in chat interface during timer updates

---

### TC-007: Support Multiple Concurrent Users with Independent Timers

**Priority**: High
**Type**: Positive
**Requirement**: NFR-3
**Preconditions**:
- Multiple users logged in concurrently

**Test Steps**:
1. User A starts quiz session
2. User B starts quiz session
3. Both users proceed independently
4. Observe timers for both users are independent and accurate

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|

**Expected Result**:
- ✅ Each user’s timer operates independently without interference
- ✅ Timer expiry and auto-submission work correctly per user

---

### TC-100: Reject Invalid Timer Duration Configuration (Negative)

**Priority**: Medium
**Type**: Negative
**Requirement**: FR-5
**Preconditions**:
- Admin or config attempts to set invalid timer duration (negative, zero, non-integer)

**Test Steps**:
1. Configure timer duration as -10 seconds
2. Configure timer duration as 0 seconds
3. Configure timer duration as "abc" (non-integer)
4. Start quiz session

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | -10, 0, "abc" | Invalid configurations |

**Expected Result**:
- ⛔ System rejects invalid timer configuration with error message
- ⛔ Timer uses default duration if invalid value provided
- ⛔ Timer does not start with invalid duration

---

### TC-101: Handle User Input Outside Valid Option Range

**Priority**: High
**Type**: Negative
**Requirement**: 6.3 Data Validation Rules
**Preconditions**:
- Quiz active and timer running

**Test Steps**:
1. Submit answer option index 0 (below valid range)
2. Submit answer option index greater than number of options (e.g., 5 if only 4 options)

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| User Answer | 0, 5 | Invalid option indices |

**Expected Result**:
- ⛔ System rejects invalid input with warning message
- ⛔ Prompt user to submit answer within valid range
- ⛔ Timer continues running without reset

---

### TC-102: Reject Non-Numeric User Answers

**Priority**: High
**Type**: Negative
**Requirement**: 6.4 Input Validation and Sanitization
**Preconditions**:
- Quiz active and timer running

**Test Steps**:
1. Submit answer as a non-numeric string (e.g., "abc", "one")

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| User Answer | "abc", "one" | Non-numeric input |

**Expected Result**:
- ⛔ System rejects input with warning message
- ⛔ Prompt user to submit a numeric answer
- ⛔ Timer continues without reset

---

### TC-103: Auto-Submit Only Once on Timer Expiry

**Priority**: High
**Type**: Negative
**Requirement**: FR-2
**Preconditions**:
- Timer expires for a question

**Test Steps**:
1. Let timer expire without user input
2. Verify auto-submission triggered once
3. Verify no duplicate submissions or errors occur

**Test Data**:
| Field | Value | Notes |

**Expected Result**:
- ✅ Auto-submit triggered exactly once per timer expiry
- ⛔ No duplicate answer submissions or quiz state corruption

---

### TC-104: Reject Timer Cancel Requests from Unauthorized Sessions

**Priority**: Medium
**Type**: Negative
**Requirement**: NFR-2 Security
**Preconditions**:
- Session attempting to cancel timer does not match active session

**Test Steps**:
1. Attempt to cancel timer with invalid or missing session ID

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Session ID | Invalid or missing | Unauthorized cancel attempt |

**Expected Result**:
- ⛔ System rejects unauthorized timer cancel request
- ⛔ Timer continues unaffected for valid sessions

---

### TC-200: Timer Duration Minimum Boundary (1 Second)

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-5
**Preconditions**:
- Timer duration configurable

**Test Steps**:
1. Configure timer duration to minimum valid value (1 second)
2. Start quiz session
3. Observe timer countdown and expiry

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 1 second | Minimum boundary |

**Expected Result**:
- ✅ Timer counts down from 1 second correctly
- ✅ Auto-submit triggered immediately after expiry

---

### TC-201: Timer Duration Maximum Boundary (e.g., 3600 Seconds)

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-5
**Preconditions**:
- Timer duration configurable

**Test Steps**:
1. Configure timer duration to a large value (3600 seconds, 1 hour)
2. Start quiz session
3. Confirm timer counts down without errors

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 3600 seconds | Maximum boundary |

**Expected Result**:
- ✅ Timer runs for full duration without errors or drift
- ✅ UI displays large timer values correctly

---

### TC-202: Timer with Zero Duration (Edge Negative)

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-5
**Preconditions**:
- Timer duration configurable

**Test Steps**:
1. Configure timer duration to zero
2. Start quiz session

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | 0 seconds | Invalid edge case |

**Expected Result**:
- ⛔ Timer does not start
- ⛔ System uses default timer duration or shows error

---

### TC-203: Timer with Extreme Negative Duration (Edge Negative)

**Priority**: Medium
**Type**: Edge
**Requirement**: FR-5
**Preconditions**:
- Timer duration configurable

**Test Steps**:
1. Configure timer duration to -9999 seconds
2. Start quiz session

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | -9999 seconds | Invalid edge case |

**Expected Result**:
- ⛔ Timer does not start
- ⛔ System rejects configuration and falls back to default

---

### TC-204: Timer String Value with Leading/Trailing Spaces

**Priority**: Low
**Type**: Edge
**Requirement**: FR-5
**Preconditions**:
- Timer duration configurable as string input

**Test Steps**:
1. Configure timer duration as string with spaces: " 30 "
2. Start quiz session

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | " 30 " | String with spaces |

**Expected Result**:
- ✅ Timer accepts trimmed numeric value
- ✅ Timer starts with 30 seconds duration

---

### TC-300: SQL Injection Attempt in User Answer Input

**Priority**: High
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A03:2021 - Injection
**Attack Vector**: SQL Injection payload submitted as answer

**Preconditions**:
- Quiz active and input accepted

**Test Steps**:
1. Submit answer: `' OR '1'='1`
2. Observe system response

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| User Answer | `' OR '1'='1` | SQL Injection payload |

**Expected Result**:
- ⛔ Input rejected or sanitized
- ⛔ No database errors or injection occurs
- ⛔ User prompted to enter valid numeric answer

---

### TC-301: Cross-Site Scripting (XSS) Payload in User Answer

**Priority**: High
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A03:2021 - Injection (XSS)
**Attack Vector**: XSS payload submitted as answer

**Preconditions**:
- Quiz active and input accepted

**Test Steps**:
1. Submit answer: `<script>alert('XSS')</script>`
2. Observe output and UI behavior

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| User Answer | `<script>alert('XSS')</script>` | XSS payload |

**Expected Result**:
- ⛔ Input sanitized or rejected
- ⛔ No script execution or UI corruption
- ⛔ Warning to user for invalid input

---

### TC-302: Unauthorized Timer Cancel Attempt

**Priority**: High
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A01:2021 - Broken Access Control
**Attack Vector**: Attempt to cancel timer for another user's session

**Preconditions**:
- Multiple user sessions active

**Test Steps**:
1. User A attempts to invoke timer cancel API for User B's session
2. Observe system response

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Session ID | User B's session ID | Unauthorized access |

**Expected Result**:
- ⛔ Access denied error returned
- ⛔ Timer for User B remains active

---

### TC-303: Brute Force Attempts with Rapid Inputs

**Priority**: Medium
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A07:2021 - Identification and Authentication Failures
**Attack Vector**: Rapidly submitting answers to overwhelm system

**Preconditions**:
- Quiz active

**Test Steps**:
1. Submit a high volume of answers in rapid succession
2. Observe system behavior and performance

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| User Input | Multiple rapid submissions | Automated script or tool |

**Expected Result**:
- ⛔ System throttles or rate-limits inputs
- ⛔ No crashes or denial of service occurs

---

### TC-304: Session Fixation Attempt

**Priority**: High
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A07:2021 - Identification and Authentication Failures
**Attack Vector**: Attempt to reuse or fix session ID to hijack quiz session

**Preconditions**:
- Active quiz session exists

**Test Steps**:
1. Attempt to reuse existing session ID in new connection
2. Observe system behavior

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Session ID | Previously used session ID | Session fixation attempt |

**Expected Result**:
- ⛔ New session rejected or isolated
- ⛔ No unauthorized access to quiz state

---

### TC-305: Timer State Tampering Attempt

**Priority**: High
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A01:2021 - Broken Access Control
**Attack Vector**: Client attempts to manipulate timer state or duration

**Preconditions**:
- Quiz session active

**Test Steps**:
1. Attempt to modify timer duration or remaining time via client-side injection or API calls
2. Observe system response

**Test Data**:
| Field | Value | Notes |
|-------|-------|-------|
| Timer Duration | Modified value | Tampering attempt |

**Expected Result**:
- ⛔ Server validates timer state and ignores client tampering
- ⛔ Timer enforces correct duration and expiry

---

### TC-306: Timer Expiry Logging Check

**Priority**: Medium
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A09:2021 - Security Logging and Monitoring Failures
**Attack Vector**: Verify that timer expirations are logged

**Preconditions**:
- Logging enabled in system

**Test Steps**:
1. Let timer expire on a question
2. Check logs for timer expiry event

**Test Data**:
| Field | Value | Notes |

**Expected Result**:
- ✅ Timer expiry event logged with session ID and timestamp
- ✅ Logs do not contain sensitive data

---

### TC-307: Denial of Service via Timer Overload

**Priority**: High
**Type**: Security
**Requirement**: NFR-2
**OWASP Category**: A05:2021 - Security Misconfiguration
**Attack Vector**: Attempt to start excessive timers to overload server

**Preconditions**:
- System running

**Test Steps**:
1. Simulate many concurrent quiz sessions starting timers rapidly
2. Monitor server resource usage and response

**Test Data**:
| Field | Value | Notes |

**Expected Result**:
- ⛔ System handles load gracefully or rejects excess connections
- ⛔ No crashes or degraded service beyond acceptable limits

---

### TC-400: Timer Response Time Under Load

**Priority**: High
**Type**: Performance
**Requirement**: NFR-1
**Performance Goal**: Timer updates with latency < 100ms

**Test Environment**:
- Server with Python 3.10+
- Network latency < 50ms

**Load Profile**:
- 100 concurrent quiz sessions
- Each session with timer running

**Test Steps**:
1. Start 100 concurrent quiz sessions
2. Monitor timer update response times on UI
3. Check for lag or delays

**Success Criteria**:
- ✅ Average timer update latency < 100ms
- ✅ No timer skips or UI freezes

---

### TC-401: Stress Test with Maximum Concurrent Timers

**Priority**: High
**Type**: Performance
**Requirement**: NFR-3
**Performance Goal**: System supports at least 1000 concurrent timers

**Test Environment**:
- Server configured for high load

**Load Profile**:
- 1000 concurrent quiz sessions started simultaneously

**Test Steps**:
1. Simulate 1000 concurrent users starting quiz sessions
2. Observe system stability and timer accuracy

**Success Criteria**:
- ✅ System remains stable
- ✅ Timer expiry and auto-submit function correctly for all sessions

---

### TC-402: Integration Test - Timer and Answer Submission Interaction

**Priority**: High
**Type**: Integration
**Requirement**: FR-2, FR-3
**Preconditions**:
- Timer running for a question

**Test Steps**:
1. Start timer for a question
2. User submits answer before timer expiry
3. Verify timer is cancelled or paused
4. Verify quiz logic processes answer correctly

**Expected Result**:
- ✅ Timer cancelled on answer submission
- ✅ Answer processed correctly
- ✅ Next question timer starts fresh

---

### TC-403: Integration Test - Timer Expiry and Auto-Submission Flow

**Priority**: High
**Type**: Integration
**Requirement**: FR-2
**Preconditions**:
- Timer running

**Test Steps**:
1. Let timer expire without user input
2. Verify auto-submission triggered
3. Verify quiz advances to next question with new timer

**Expected Result**:
- ✅ Auto-submission occurs on timer expiry
- ✅ Next question timer starts correctly

---

### TC-600: Accessibility Test - Timer Visibility and Screen Reader Support

**Priority**: Medium
**Type**: Accessibility
**Requirement**: NFR-5
**WCAG Level**: AA

**Test Steps**:
1. Use screen reader to navigate quiz
2. Verify timer is announced correctly at start and during countdown
3. Verify timer warnings are accessible

**Expected Result**:
- ✅ Timer information is accessible via screen reader
- ✅ Visual timer warnings have accessible equivalents

---

### TC-601: Accessibility Test - Keyboard Navigation for Timer Controls

**Priority**: Medium
**Type**: Accessibility
**Requirement**: NFR-5
**WCAG Level**: AA

**Test Steps**:
1. Navigate quiz using keyboard only
2. Verify timer display and warnings are visible and operable

**Expected Result**:
- ✅ Timer UI accessible without mouse
- ✅ Focus indicator visible on timer elements

---

### Requirements-to-Test Coverage Matrix

| Requirement ID | Description                                   | Test Case IDs                      | Total Tests | Coverage % | Priority | Status   | Notes                        |
|----------------|-----------------------------------------------|----------------------------------|-------------|------------|----------|----------|------------------------------|
| FR-1           | Countdown timer visible per question          | TC-001                           | 1           | 100%       | High     | Complete |                              |
| FR-2           | Auto-submit answer if timer expires           | TC-002, TC-103, TC-303, TC-403   | 4           | 100%       | High     | Complete | Includes security edge cases |
| FR-3           | Pause/reset timer per new question             | TC-003, TC-402                   | 2           | 100%       | High     | Complete |                              |
| FR-4           | Display timer warnings near expiry             | TC-004, TC-600                   | 2           | 100%       | Medium   | Complete | Accessibility included       |
| FR-5           | Configurable timer duration                     | TC-005, TC-100, TC-200, TC-201, TC-202, TC-203, TC-204, TC-305 | 8 | 100% | Medium   | Complete | Edge and negative tests      |
| NFR-1          | Timer updates without UI lag                    | TC-006, TC-400                  | 2           | 100%       | High     | Complete | Performance tested           |
| NFR-2          | Timer state securely managed                    | TC-104, TC-300, TC-301, TC-302, TC-304, TC-305, TC-306, TC-307 | 8 | 100% | High     | Complete | OWASP coverage               |
| NFR-3          | Support multiple concurrent users               | TC-007, TC-401                  | 2           | 100%       | High     | Complete | Load and concurrency tested  |
| NFR-4          | Timer accuracy and reliability                  | TC-201, TC-402                  | 2           | 100%       | Medium   | Complete | Edge and integration tests   |
| NFR-5          | Timer UI accessible and readable                 | TC-600, TC-601                  | 2           | 100%       | Medium   | Complete | WCAG 2.1 AA                  |

---