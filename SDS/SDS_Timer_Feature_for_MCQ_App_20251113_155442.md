# Software Design Specification (SDS)
## Timer Feature for MCQ Quiz Application

**Document Version**: 1.0  
**Date**: 2024-11-13  
**Project**: MCQ Quiz Application  
**Module**: Timer Feature  
**Author**: AI-Generated  
**Reviewed By**: _________________  
**Approved By**: _________________  
**Approval Date**: _________________  

## Document History

| Version | Date       | Author       | Changes              |
|---------|------------|--------------|----------------------|
| 1.0     | 2024-11-13 | AI-Generated | Initial SDS creation |

## Distribution List

| Role           | Name | Date Sent |
|----------------|------|-----------|
| Technical Lead |      |           |
| QA Lead        |      |           |
| Product Owner  |      |           |

## 1. Executive Summary

The Timer Feature adds time constraints to quiz questions, enhancing engagement and simulating real exam conditions. When a question is presented, a countdown timer starts. If the user doesn't answer within the time limit, the system automatically marks it as unanswered and proceeds to the next question.

**Key Stakeholders:**
- Development team (implementation)
- QA team (testing)
- Product management (validation)

**Success Criteria:**
- Timer starts and displays correctly per question
- Automatic progression on timeout
- Accurate scoring for timed-out questions
- Configurable timer duration
- No regression on existing features

## 2. Scope & Requirements

### 2.1 Functional Requirements

| ID     | Requirement                                           | Priority |
|--------|-------------------------------------------------------|----------|
| FR-1   | Start countdown timer when question is presented      | High     |
| FR-2   | Display remaining time visibly in UI                  | High     |
| FR-3   | Automatically move to next question on timeout        | High     |
| FR-4   | Mark unanswered timed-out questions as incorrect      | High     |
| FR-5   | Allow configuration of timer duration                 | Medium   |
| FR-6   | Pause/reset timer when user restarts quiz             | Medium   |
| FR-7   | Log timer events for analytics                        | Low      |

### 2.2 Non-Functional Requirements

| ID      | Requirement                                          | Priority |
|---------|------------------------------------------------------|----------|
| NFR-1   | Timer accuracy within ±1 second                      | High     |
| NFR-2   | No performance degradation from timer                | High     |
| NFR-3   | Maintain security and data privacy                   | High     |
| NFR-4   | Secure timer duration configuration                  | Medium   |
| NFR-5   | Scalable to support concurrent users                 | Medium   |

### 2.3 Scope

**In Scope:**
- Timer integration with quiz logic
- UI display of countdown timer
- Automatic progression on timeout
- Configuration management
- Event logging

**Out of Scope:**
- UI redesign beyond timer display
- Analytics dashboard/reporting
- Offline/mobile app adaptations

## 3. Architecture Overview

### 3.1 Current System

The quiz application is built with:
- **Framework**: Chainlit (Python async chat framework)
- **Event Handlers**: `@cl.on_chat_start`, `@cl.on_message`
- **Session Management**: In-memory dictionary keyed by session IDs
- **Question Bank**: Managed in `questions.py`
- **Flow**: Asynchronous message-based interaction

### 3.2 Timer Architecture

The timer will be implemented using Python's `asyncio`:
- Timer task starts when question is sent
- If answer received before timeout → timer canceled
- If timer expires first → auto-submit timeout event → mark question unanswered → proceed

**Technology Stack:**
- Python 3.x with asyncio
- Chainlit framework
- Standard library timer components

**Integration Points:**
- `send_question()` - starts timer
- `main()` message handler - cancels timer on answer
- User session state - stores timer status

## 4. Component Breakdown

| Component           | Responsibility                          | Interfaces                    | Code Location      |
|---------------------|-----------------------------------------|-------------------------------|--------------------|
| Timer Manager       | Manage countdown, start, cancel, timeout| Async timer coroutines        | app.py (new)       |
| Quiz Controller     | Send questions, receive answers         | Chainlit message handlers     | app.py             |
| User Session Store  | Maintain per-user state with timer info | Dictionary by session ID      | app.py user_data   |
| Configuration       | Provide timer duration settings         | Config variables              | config.py or .env  |

## 5. API Overview

This feature does not add external APIs but extends internal application interfaces.

| Function            | Type     | Description                        | Parameters              | Returns        |
|---------------------|----------|------------------------------------|-------------------------|----------------|
| start_timer()       | Internal | Start countdown for current question| session_id, duration    | timer_task     |
| cancel_timer()      | Internal | Cancel active timer                | session_id              | bool           |
| on_timer_expire()   | Internal | Handle timeout event               | session_id              | None           |
| get_timer_status()  | Internal | Get current timer state            | session_id              | dict           |

## 6. Data Model & Persistence

### 6.1 Data Model Changes

The timer feature requires additions to the in-memory session data structure:

| Field Name       | Type      | Description                                    |
|------------------|-----------|------------------------------------------------|
| timer_active     | boolean   | Indicates if timer is currently running        |
| timer_start_time | timestamp | Start time of current question timer           |
| timer_duration   | integer   | Configured time limit in seconds               |
| timer_task       | object    | Reference to async timer coroutine task        |
| questions_timed_out | integer | Count of questions that timed out            |

These fields will be added to the existing `user_data` dictionary keyed by user session ID.

### 6.2 Data Flow

```
1. Question sent → timer_start_time = now(), timer_active = True
2. Timer expires → timer_active = False, questions_timed_out += 1
3. Answer received → timer_active = False, cancel timer_task
```

## 7. Configuration Management

### 7.1 Configuration Parameters

| Parameter              | Type    | Default | Description                    |
|------------------------|---------|---------|--------------------------------|
| TIMER_ENABLED          | boolean | True    | Enable/disable timer feature   |
| DEFAULT_TIMER_DURATION | integer | 30      | Default time limit in seconds  |
| TIMER_WARNING_THRESHOLD| integer | 10      | Seconds before showing warning |

### 7.2 Configuration Storage

Configuration will be stored in `.env` file:

```bash
TIMER_ENABLED=true
DEFAULT_TIMER_DURATION=30
TIMER_WARNING_THRESHOLD=10
```

## 8. Security Considerations

### 8.1 Security Requirements

| Requirement | Description                                   | Mitigation                        |
|-------------|-----------------------------------------------|-----------------------------------|
| SEC-1       | Prevent client-side timer manipulation        | Server-side timer validation      |
| SEC-2       | Secure timer configuration storage            | Environment variables, not in code|
| SEC-3       | Protect session data integrity                | Session validation checks         |

### 8.2 Data Privacy

- Timer data is session-specific and temporary
- No personally identifiable information in timer events
- Timer logs (if enabled) contain only session IDs and timestamps

## 9. Observability & Monitoring

### 9.1 Logging Events

| Event                | Level | Data Logged                               |
|----------------------|-------|-------------------------------------------|
| Timer Started        | INFO  | session_id, question_id, duration         |
| Timer Expired        | INFO  | session_id, question_id                   |
| Timer Canceled       | DEBUG | session_id, question_id, time_remaining   |
| Configuration Loaded | INFO  | timer_enabled, default_duration           |

### 9.2 Metrics (Optional)

- Average time to answer per question
- Timeout rate (% questions timed out)
- Timer accuracy (actual vs configured duration)

## 10. Error Handling & Edge Cases

### 10.1 Error Scenarios

| Scenario                  | Handling Strategy                                    |
|---------------------------|------------------------------------------------------|
| Timer task fails          | Log error, mark question as unanswered, continue     |
| Multiple answers received | Accept first answer, cancel timer, ignore duplicates |
| Session expires mid-timer | Clean up timer task, clear session data             |
| Invalid timer duration    | Use default duration, log warning                    |

### 10.2 Edge Cases

- **User disconnects during timer**: Timer continues server-side, marks as timeout
- **Timer duration = 0**: Disable timer for that question
- **Negative timer duration**: Validation error, use default
- **Very long timer (> 300s)**: Warning logged, but allowed

## 11. Testing Strategy

### 11.1 Unit Tests

| Test Case                    | Verification                                  |
|------------------------------|-----------------------------------------------|
| test_timer_start             | Timer starts with correct duration            |
| test_timer_cancel            | Timer cancels when answer received            |
| test_timer_expiry            | Timeout handler called after duration         |
| test_multiple_timers         | Each session has independent timer            |
| test_invalid_duration        | Handles invalid timer durations gracefully    |

### 11.2 Integration Tests

| Test Case                    | Verification                                  |
|------------------------------|-----------------------------------------------|
| test_quiz_with_timer         | Full quiz flow with timer integration         |
| test_timeout_progression     | Quiz progresses correctly on timeout          |
| test_scoring_with_timeouts   | Score calculated correctly with timeouts      |
| test_session_cleanup         | Timer cleaned up when session ends            |

### 11.3 Manual Test Cases

| ID   | Scenario                          | Steps                                    | Expected Result                     |
|------|-----------------------------------|------------------------------------------|-------------------------------------|
| MT-1 | Timer displays and counts down    | 1. Start quiz<br>2. Observe timer        | Timer shows and decrements          |
| MT-2 | Answer before timeout             | 1. Start quiz<br>2. Answer quickly       | Question marked, timer stops        |
| MT-3 | Timer expires                     | 1. Start quiz<br>2. Wait for timeout     | Auto-proceed to next question       |
| MT-4 | Multiple questions with timer     | 1. Complete quiz with timeouts           | All timeouts handled correctly      |

## 12. Deployment Strategy

### 12.1 Rollout Plan

| Phase | Description                  | Success Criteria                        |
|-------|------------------------------|-----------------------------------------|
| 1     | Development & unit testing   | All unit tests pass                     |
| 2     | Integration testing          | Full quiz flow works with timer         |
| 3     | Staging deployment           | No errors in staging environment        |
| 4     | Production deployment        | Gradual rollout, monitor errors         |

### 12.2 Rollback Plan

If issues occur:
1. Disable timer via `TIMER_ENABLED=false` config
2. Restart application
3. Quiz continues without timer (backward compatible)

## 13. Dependencies & Assumptions

### 13.1 Dependencies

| Dependency | Version | Purpose                  | Criticality |
|------------|---------|--------------------------|-------------|
| Python     | 3.8+    | Runtime environment      | Critical    |
| asyncio    | stdlib  | Timer implementation     | Critical    |
| Chainlit   | latest  | Application framework    | Critical    |

### 13.2 Assumptions

- Users have stable internet connection for real-time timer updates
- Server clock is accurate (NTP synchronized)
- Single instance deployment (or shared session store for multi-instance)
- Timer UI updates don't significantly impact performance

## 14. Risks & Mitigation

| Risk                          | Impact | Probability | Mitigation                                |
|-------------------------------|--------|-------------|-------------------------------------------|
| Timer drift/inaccuracy        | Medium | Low         | Use server-side timing, not client-side   |
| Performance degradation       | High   | Low         | Load testing, async implementation        |
| User confusion/frustration    | Medium | Medium      | Clear timer display, warning at 10s       |
| Session state corruption      | High   | Low         | Input validation, error handling          |

## 15. Future Enhancements

- Per-question timer duration (different times for different questions)
- Pause/resume timer functionality
- Timer history visualization in analytics dashboard
- Customizable timer warnings (e.g., at 50%, 25% remaining)
- Sound alerts when timer is running low

## 16. Architecture Decision Records (ADRs)

### ADR-001: Use asyncio for Timer Implementation

**Status**: Accepted

**Context**: Need to implement countdown timer that doesn't block the main application thread.

**Decision**: Use Python's `asyncio` library for non-blocking timer implementation.

**Consequences**:
- ✅ Non-blocking, maintains application responsiveness
- ✅ Native Python support, no external dependencies
- ✅ Integrates well with Chainlit's async framework
- ⚠️ Requires understanding of async/await patterns

**Alternatives Considered**:
- Threading: More complex, potential race conditions
- External library: Additional dependency

### ADR-002: Server-Side Timer Validation

**Status**: Accepted

**Context**: Need to prevent client-side timer manipulation.

**Decision**: All timer logic and validation runs server-side.

**Consequences**:
- ✅ Secure, client cannot manipulate timer
- ✅ Accurate timing regardless of client behavior
- ⚠️ Requires server-side session management

**Alternatives Considered**:
- Client-side timer: Insecure, easily manipulated
- Hybrid approach: Unnecessarily complex

### ADR-003: In-Memory Session Storage

**Status**: Accepted

**Context**: Need to store timer state per user session.

**Decision**: Store timer state in existing in-memory `user_data` dictionary.

**Consequences**:
- ✅ Simple implementation, no new infrastructure
- ✅ Fast access to timer state
- ⚠️ Data lost on application restart
- ⚠️ Not suitable for multi-instance deployment without shared store

**Alternatives Considered**:
- Database storage: Overkill for temporary timer state
- Redis: Additional infrastructure complexity

## 17. Glossary & References

### 17.1 Glossary

| Term          | Definition                                                            |
|---------------|-----------------------------------------------------------------------|
| SDS           | Software Design Specification - detailed design document              |
| MCQ           | Multiple Choice Question                                              |
| Timeout       | Event when timer expires before user answers                          |
| Session       | User's individual quiz instance with unique identifier                |
| asyncio       | Python library for writing concurrent code using async/await syntax   |
| Chainlit      | Python framework for building conversational AI applications          |

### 17.2 References

- [Python asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Chainlit Documentation](https://docs.chainlit.io/)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)

### 17.3 Related Documents

- User Requirements Document (URD)
- System Architecture Document
- Test Plan Document
- Deployment Guide

---

## Appendix: Converting to Word Document

To convert this markdown SDS to a Microsoft Word document:

```bash
# Using Pandoc
pandoc SDS_Timer_Feature.md -o SDS_Timer_Feature.docx

# With custom styling
pandoc SDS_Timer_Feature.md --reference-doc=custom-template.docx -o SDS_Timer_Feature.docx
```

**Requirements**:
- Install Pandoc: https://pandoc.org/installing.html
- For custom styling, create a `custom-template.docx` with your preferred styles

---

**Document Status**: Complete  
**Last Updated**: 2024-11-13  
**Next Review**: 2024-12-13
