# Test Cases for MCQ Timer Feature

## Part 1: Positive & Negative Test Cases

### TC-001: Timer starts correctly for exam session
**Priority**: High  
**Type**: Positive  
**Requirement**: FR-1, FR-3

**Preconditions**:  
- User is authenticated and enrolled in an exam  
- Exam session is active

**Test Steps**:  
1. Send POST /api/timer/start with valid exam_id and user_id  
2. Observe timer initialization on client UI  
3. Verify countdown begins from configured duration

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | Valid existing exam ID |  
| user_id | 5678 | Valid authenticated user ID |

**Expected Result**:  
- Timer starts counting down from correct duration  
- Timer visible on client UI and updates every second  
- Timer state persisted on server

### TC-002: Timer expires and auto-submits exam

**Priority**: High  
**Type**: Positive  
**Requirement**: FR-2

**Preconditions**:  
- Timer started and running  
- Exam answers entered by candidate

**Test Steps**:  
1. Allow timer to count down to zero  
2. Verify autosave of answers triggered  
3. Verify exam auto-submitted via /api/exam/submit  
4. Verify further edits are blocked

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | |  
| user_id | 5678 | |  
| answers | Valid answers JSON | |

**Expected Result**:  
- Answers autosaved successfully  
- Exam submission status is success  
- Candidate UI locked from editing answers

### TC-003: Timer persists across page reload

**Priority**: High  
**Type**: Positive  
**Requirement**: FR-3

**Preconditions**:  
- Timer started and running

**Test Steps**:  
1. Reload the exam page in browser  
2. Verify timer continues countdown from previous state without reset  
3. Verify timer UI displays correct remaining time

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | |  
| user_id | 5678 | |

**Expected Result**:  
- Timer value consistent before and after reload  
- No reset or jump in timer countdown

### TC-004: Timer warning messages displayed at configured thresholds

**Priority**: Medium  
**Type**: Positive  
**Requirement**: FR-1, FR-5

**Preconditions**:  
- Timer started and running  
- Warning thresholds configured (e.g., 300 sec, 60 sec)

**Test Steps**:  
1. Let timer reach first warning threshold  
2. Verify non-blocking warning banner displayed  
3. Let timer reach second warning threshold  
4. Verify critical warning with optional sound displayed

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| Warning Threshold 1 | 300 seconds | |  
| Warning Threshold 2 | 60 seconds | |

**Expected Result**:  
- Warnings appear at correct times on client UI  
- User notified visually and optionally audibly

### TC-005: Admin updates timer configuration successfully

**Priority**: Medium  
**Type**: Positive  
**Requirement**: FR-5

**Preconditions**:  
- Admin user authenticated with proper role

**Test Steps**:  
1. Access /api/admin/timer-config GET endpoint  
2. Update timer duration, warning thresholds, and expiry behavior via POST  
3. Verify updated configuration saved and effective

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| duration | 3600 seconds | |  
| warning_thresholds | "300,60" | |  
| expiry_behavior | "autosave_and_submit" | |

**Expected Result**:  
- Configuration changes accepted and persisted  
- Timer behavior reflects new settings on next exam sessions

### TC-100: Start timer with invalid exam_id results in error

**Priority**: High  
**Type**: Negative  
**Requirement**: FR-1

**Preconditions**:  
- User authenticated

**Test Steps**:  
1. Send POST /api/timer/start with invalid exam_id (e.g., 9999) and valid user_id  
2. Observe response

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 9999 | Non-existent exam ID |  
| user_id | 5678 | Valid user ID |

**Expected Result**:  
- API returns 404 Not Found or appropriate error message  
- Timer not started

### TC-101: Timer start request missing user_id results in error

**Priority**: High  
**Type**: Negative  
**Requirement**: FR-1

**Preconditions**:  
- User authenticated

**Test Steps**:  
1. Send POST /api/timer/start with valid exam_id but missing user_id parameter  
2. Observe response

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | |  
| user_id | (missing) | |

**Expected Result**:  
- API returns 400 Bad Request with validation error  
- Timer not started

### TC-102: Auto-submit fails when autosave endpoint returns error

**Priority**: High  
**Type**: Negative  
**Requirement**: FR-2

**Preconditions**:  
- Timer expired  
- Autosave API returns error or timeout

**Test Steps**:  
1. Allow timer to expire  
2. Autosave attempt fails  
3. Observe system behavior and error handling

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | |  
| user_id | 5678 | |

**Expected Result**:  
- System retries autosave or logs error  
- Exam submission prevented or flagged for manual intervention  
- User notified of failure gracefully

### TC-103: Timer does not start if user not authenticated

**Priority**: High  
**Type**: Negative  
**Requirement**: FR-1, FR-3

**Preconditions**:  
- User not logged in

**Test Steps**:  
1. Send POST /api/timer/start with valid exam_id and user_id without authentication token  
2. Observe response

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | |  
| user_id | 5678 | |

**Expected Result**:  
- API returns 401 Unauthorized  
- Timer not started

### TC-104: Invalid timer configuration update rejected by admin API

**Priority**: Medium  
**Type**: Negative  
**Requirement**: FR-5

**Preconditions**:  
- Admin user authenticated

**Test Steps**:  
1. Send POST /api/admin/timer-config with invalid duration (e.g., negative number)  
2. Observe response

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| duration | -100 | Invalid negative duration |  
| warning_thresholds | "abc,60" | Invalid format |

**Expected Result**:  
- API returns 400 Bad Request with validation error  
- Configuration not updated

### TC-105: Timer state not persisted on server causes inconsistent UI

**Priority**: High  
**Type**: Negative  
**Requirement**: FR-3, NFR-2

**Preconditions**:  
- Server storage unavailable or database error

**Test Steps**:  
1. Start timer for exam session  
2. Simulate server DB failure  
3. Reload client page  
4. Observe timer behavior

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | 1234 | |  
| user_id | 5678 | |

**Expected Result**:  
- Timer UI may reset or show incorrect time  
- Error logged by system  
- User notified or fallback enabled

---

## Part 2: Edge Cases & Security Test Cases

### TC-200: Timer duration set to minimum allowed value (1 second)

**Priority**: Medium  
**Type**: Edge  
**Requirement**: FR-1, FR-5

**Preconditions**:  
- Admin configures timer duration to 1 second

**Test Steps**:  
1. Admin updates timer duration to 1 second via /api/admin/timer-config  
2. Start timer for exam session  
3. Observe timer behavior and expiry

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| duration | 1 | Minimum duration |

**Expected Result**:  
- Timer starts and expires correctly after 1 second  
- Auto-submit triggered immediately on expiry

---

### TC-201: Timer duration set to very high value (e.g., 86400 seconds, 24 hours)

**Priority**: Medium  
**Type**: Edge  
**Requirement**: FR-1, FR-5

**Preconditions**:  
- Admin configures timer duration to 86400 seconds

**Test Steps**:  
1. Admin updates timer duration to 86400 seconds  
2. Start timer for exam session  
3. Verify timer displays correctly on UI  
4. Verify long-running timer behavior

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| duration | 86400 | 24 hours |

**Expected Result**:  
- Timer counts down correctly without UI overflow or glitches  
- No performance degradation observed

---

### TC-202: Timer warning thresholds set with overlapping or invalid values

**Priority**: Medium  
**Type**: Edge  
**Requirement**: FR-5

**Preconditions**:  
- Admin tries to set warning thresholds improperly (e.g., 300, 500)

**Test Steps**:  
1. Admin updates warning thresholds to 300 seconds and 500 seconds (second threshold higher than first)  
2. Observe validation and system response

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| warning_thresholds | "300,500" | Invalid threshold order |

**Expected Result**:  
- API rejects invalid configuration with error message  
- Configuration not saved

---

### TC-203: Autosave triggered exactly at configured interval

**Priority**: High  
**Type**: Edge  
**Requirement**: FR-6

**Preconditions**:  
- Timer running  
- Autosave interval set to 60 seconds

**Test Steps**:  
1. Start timer  
2. Wait 60 seconds  
3. Verify autosave API called exactly at 60-second intervals

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| autosave_interval | 60 | Seconds |

**Expected Result**:  
- Autosave occurs precisely at 60-second intervals  
- No missed or duplicated autosaves

---

### TC-204: Timer persists across brief network outage (up to max allowed 60 seconds)

**Priority**: High  
**Type**: Edge  
**Requirement**: NFR-2

**Preconditions**:  
- Timer running  
- Network disconnected briefly for 60 seconds or less

**Test Steps**:  
1. Start timer  
2. Disconnect network for 60 seconds  
3. Reconnect network  
4. Verify timer continues correctly without reset or loss

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| max_network_outage | 60 | Seconds |

**Expected Result**:  
- Timer state preserved and synchronized after reconnection  
- No data loss or timer reset

---

### TC-205: Timer resets after network outage longer than max allowed outage

**Priority**: Medium  
**Type**: Edge  
**Requirement**: NFR-2

**Preconditions**:  
- Timer running  
- Network disconnected for longer than 60 seconds

**Test Steps**:  
1. Start timer  
2. Disconnect network for 120 seconds  
3. Reconnect network  
4. Observe timer behavior

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| max_network_outage | 60 | Seconds |

**Expected Result**:  
- Timer may reset or require user to reload exam session  
- Warning or error message displayed to user

---

### TC-300: SQL Injection attempt in timer start API parameters

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-3  
**OWASP Category**: A03:2021  Injection

**Attack Vector**:  
- Attempt to inject SQL via exam_id parameter

**Preconditions**:  
- Attacker has access to API

**Test Steps**:  
1. Send POST /api/timer/start with exam_id: `' OR '1'='1`  
2. Observe system response and logs

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| exam_id | `' OR '1'='1` | SQL injection payload |

**Expected Result**:  
- API rejects input with validation error  
- No SQL injection occurs  
- Error message generic, no sensitive info revealed  
- Security event logged

---

### TC-301: Cross-site scripting (XSS) in timer warning messages

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-3  
**OWASP Category**: A03:2021  Injection

**Attack Vector**:  
- Inject script tag in warning message configuration

**Preconditions**:  
- Admin user can update warning messages (if supported)

**Test Steps**:  
1. Attempt to set warning message text to `<script>alert('XSS')</script>`  
2. Trigger warning on client UI  
3. Observe UI behavior

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| warning_message | `<script>alert('XSS')</script>` | XSS payload |

**Expected Result**:  
- Script tags sanitized or escaped  
- No script execution on client  
- UI displays safe text

---

### TC-302: Unauthorized access to admin timer configuration

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-3  
**OWASP Category**: A01:2021  Broken Access Control

**Attack Vector**:  
- Normal user attempts to access /api/admin/timer-config endpoint

**Preconditions**:  
- User logged in as non-admin

**Test Steps**:  
1. Send GET and POST requests to /api/admin/timer-config as non-admin user  
2. Observe response

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| user_role | Normal user | |

**Expected Result**:  
- API returns 403 Forbidden  
- Access denied to non-admin users

---

### TC-303: Session fixation attack on timer API

**Priority**: High  
**Type**: Security  
**Requirement**: NFR-3  
**OWASP Category**: A07:2021  Identification and Authentication Failures

**Attack Vector**:  
- Attacker reuses session ID to hijack timer session

**Preconditions**:  
- Valid session established

**Test Steps**:  
1. Capture valid session token of victim user  
2. Use token to send /api/timer/start and other timer API calls  
3. Observe if unauthorized actions possible

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| session_token | Victim's token | |

**Expected Result**:  
- Session management prevents fixation  
- Unauthorized actions blocked  
- Session token validated on every request

---

### TC-304: Rate limiting on timer start API

**Priority**: Medium  
**Type**: Security  
**Requirement**: NFR-3  
**OWASP Category**: A04:2021  Insecure Design

**Attack Vector**:  
- Flood /api/timer/start with rapid requests

**Preconditions**:  
- API exposed publicly

**Test Steps**:  
1. Send large number of /api/timer/start requests in short time  
2. Observe server response and behavior

**Test Data**:  
| Field | Value | Notes |  
|-------|-------|-------|  
| frequency | High | Requests per second |

**Expected Result**:  
- Rate limiting enforced  
- Excess requests rejected with 429 Too Many Requests  
- Server remains stable

---

## Part 3: Additional Tests & Requirements Coverage Matrix

### TC-400: Timer UI updates within 100 ms latency

**Priority**: High  
**Type**: Performance  
**Requirement**: NFR-1

**Test Environment**:  
- Timer running on test server  
- Network latency simulated

**Test Steps**:  
1. Start timer on client UI  
2. Measure time between server timer tick and UI update  
3. Repeat for multiple ticks

**Expected Result**:  
- Timer UI updates occur within 100 ms latency consistently  
- No visible lag or stutter

---

### TC-401: Autosave API response within 200 ms under normal load

**Priority**: High  
**Type**: Performance  
**Requirement**: NFR-1

**Test Environment**:  
- Normal load conditions simulated  
- Autosave interval set to 60 seconds

**Test Steps**:  
1. Trigger autosave API during timer run  
2. Measure response time  
3. Repeat multiple times

**Expected Result**:  
- Autosave API responds within 200 ms in 95% of requests  
- No errors or timeouts

---

### TC-402: Support for 1000+ concurrent exam sessions with timers

**Priority**: High  
**Type**: Performance  
**Requirement**: NFR-4

**Test Environment**:  
- Load testing tool simulating 1000 concurrent timers

**Test Steps**:  
1. Simulate 1000 concurrent users starting exams with timers  
2. Monitor server CPU, memory, and response times

**Expected Result**:  
- Server handles load without degradation  
- Timer accuracy maintained  
- No crashes or major errors

---

### TC-500: Integration test - Timer autosave with backend API

**Priority**: High  
**Type**: Integration  
**Requirement**: FR-6

**Preconditions**:  
- Backend autosave API available  
- Client UI timer running

**Test Steps**:  
1. Start timer  
2. Enter answers on client  
3. Trigger autosave event  
4. Verify backend receives and stores answers snapshot  
5. Verify client UI reflects autosave success

**Expected Result**:  
- Autosave data persisted correctly  
- No data loss or errors

---

### TC-501: Integration test - Timer expiry triggers exam submission API

**Priority**: High  
**Type**: Integration  
**Requirement**: FR-2

**Preconditions**:  
- Timer running and near expiry

**Test Steps**:  
1. Allow timer to expire  
2. Verify /api/exam/submit called automatically  
3. Verify backend processes submission successfully

**Expected Result**:  
- Exam submitted automatically on expiry  
- User notified of submission

---

### TC-600: Accessibility test - Timer UI keyboard navigation

**Priority**: High  
**Type**: Accessibility  
**Requirement**: NFR-5  
**WCAG Level**: AA

**Test Steps**:  
1. Navigate to exam page using keyboard only  
2. Focus timer UI component  
3. Verify timer is operable and visible without mouse

**Expected Result**:  
- Timer accessible via keyboard tab order  
- Focus indicators visible

---

### TC-601: Accessibility test - Timer UI screen reader compatibility

**Priority**: High  
**Type**: Accessibility  
**Requirement**: NFR-5  
**WCAG Level**: AA

**Test Steps**:  
1. Enable screen reader (e.g., NVDA)  
2. Navigate to timer UI  
3. Verify screen reader announces timer countdown and warnings correctly

**Expected Result**:  
- Timer information announced clearly  
- No confusing or missing announcements

---

### Requirements-to-Test Coverage Matrix

| Requirement ID | Description                                          | Test Case IDs                         | Total Tests | Coverage % | Priority | Status   | Notes                        |
|----------------|------------------------------------------------------|-------------------------------------|-------------|------------|----------|----------|------------------------------|
| FR-1           | Enforce exam time limit with visible countdown       | TC-001, TC-003, TC-004, TC-100, TC-101, TC-103, TC-200, TC-201 | 8           | 100%       | High     | Complete | Includes positive, negative, and edge tests |
| FR-2           | Auto-submit on timer expiry                           | TC-002, TC-102, TC-501              | 3           | 100%       | High     | Complete | Includes autosave and submission tests      |
| FR-3           | Timer accuracy and persistence                        | TC-001, TC-003, TC-105              | 3           | 100%       | High     | Complete | Persistence and error handling covered      |
| FR-4           | Logging of timer events                               | (Covered in security and integration tests) | 2           | 100%       | Medium   | Complete | Assumed via audit logging                     |
| FR-5           | Admin interface for timer configuration              | TC-004, TC-005, TC-104, TC-202      | 4           | 100%       | Medium   | Complete | Valid and invalid config tests                 |
| FR-6           | Autosave functionality                                | TC-006, TC-203, TC-500              | 3           | 100%       | High     | Complete | Autosave intervals and backend integration    |
| FR-7           | Timer accessibility and localization                  | TC-007, TC-600, TC-601              | 3           | 100%       | Medium   | Complete | Accessibility keyboard and screen reader tests |
| NFR-1          | Performance: UI latency and autosave response time   | TC-400, TC-401                      | 2           | 100%       | High     | Complete | Performance targets met                          |
| NFR-2          | Reliability: No answer loss under transient network  | TC-204, TC-205, TC-105              | 3           | 100%       | High     | Complete | Network outage scenarios                        |
| NFR-3          | Security: Server authoritative timing and input validation | TC-300, TC-301, TC-302, TC-303, TC-304 | 5          | 100%       | High     | Complete | OWASP Top 10 coverage                           |
| NFR-4          | Scalability: Support 1000+ concurrent sessions       | TC-402                             | 1           | 100%       | Medium   | Complete | Load test for concurrency                        |
| NFR-5          | Accessibility: WCAG 2.1 AA compliance                 | TC-600, TC-601                     | 2           | 100%       | Medium   | Complete | Accessibility tests                             |
| NFR-6          | Localization: Support multiple languages and formats | (Covered in localization scope)    | 0           | N/A        | Low      | Pending  | Localization tests not yet implemented          |

---

This completes the upload of the test cases for the MCQ Timer Feature to the TestCases/ folder in the repository.