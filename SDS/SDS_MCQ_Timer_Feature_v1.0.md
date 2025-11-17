# Software Design Specification (SDS)  
## MCQ Timer Feature  

**Document Version**: 1.0  
**Date**: 2024-06-10  
**Project**: MCQ App  
**Module**: Timer Feature  
**Author**: AI-Generated (GitHub Copilot)  
**Reviewed By**: _________________  
**Approved By**: _________________  
**Approval Date**: _________________  

---

### Document History  

| Version | Date       | Author       | Changes                |  
|---------|------------|--------------|------------------------|  
| 1.0     | 2024-06-10 | AI-Generated | Initial SDS creation    |  
|         |            |              |                        |  

---

### Distribution List  

| Role           | Name         | Date Sent |  
|----------------|--------------|-----------|  
| Technical Lead |              |           |  
| QA Lead       |              |           |  
| Product Owner |              |           |  
|                |              |           |  

---

## 1. Executive Summary  

The MCQ Timer Feature introduces configurable timers within the Multiple Choice Question (MCQ) application to enforce exam time constraints, ensure fairness, and enhance user experience. The timer controls the duration of assessments, providing visible countdowns to candidates and handling auto-save and auto-submit functionalities on expiry. This feature aims to reduce exam overruns, prevent answer loss, and comply with audit and security requirements.

This feature serves candidates taking assessments and administrators configuring timer parameters. Key success metrics include a greater than 95% reduction in exam overruns, autosave reliability of at least 99%, and positive candidate feedback on timer visibility.

Stakeholders include Product Management, UX Designers, Frontend and Backend Developers, QA, and Support teams.

---

## 2. Scope & Requirements  

### Functional Requirements  

1. [FR-1] Enforce a time limit for the entire exam with a visible countdown timer.  
2. [FR-2] Auto-save answers and auto-submit the exam on timer expiry if configured.  
3. [FR-3] Display an accurate, server-authoritative timer visible to candidates throughout the exam.  
4. [FR-4] Log all timing-related events for audit purposes.  
5. [FR-5] Provide admin-configurable timer settings including durations, warning thresholds, and accommodations.  
6. [FR-6] Ensure timer state persists across page reloads and brief network outages.  
7. [FR-7] Provide accessibility and localization support for timer display and messages.  

### Non-Functional Requirements  

1. [NFR-1] Performance: Timer updates every second with UI latency under 100 milliseconds.  
2. [NFR-2] Reliability: No answer loss during transient network loss up to 60 seconds.  
3. [NFR-3] Security: Server authoritative timing to prevent client-side clock tampering.  
4. [NFR-4] Scalability: Support large numbers of concurrent exam sessions without degradation.  

### Scope  

**In Scope**:  
- Exam-level countdown timer with start, warning, critical, and expired states.  
- Auto-save and auto-submit functionality triggered by timer expiry.  
- Admin interface for timer configuration parameters.  
- Persistence of timer state across refresh and short network interruptions.  
- Accessibility features and localization support for timer UI and messages.  

**Out of Scope**:  
- Section-level timers (handled separately).  
- Integration with external authentication or proctoring systems.  
- Offline exam modes.  

### Assumptions and Constraints  

- The application runs in a web environment with consistent server connectivity.  
- The timer is synchronized using server time to prevent client clock manipulation.  
- Admin users have proper authorization to configure timer settings.  

### Dependencies  

- Chainlit framework for frontend and backend integration.  
- Backend services for logging and persistence of timer and exam state.  
- Database storage for audit logs and timer configurations.  

---

## 3. Architecture Overview  

The MCQ Timer Feature is integrated into the existing MCQ application built using Python and Chainlit. The system follows a client-server architecture where the frontend UI displays the timer, and the backend maintains authoritative timing and state management.

### Technology Stack  

| Layer           | Technology                  |  
|-----------------|-----------------------------|  
| Frontend        | Chainlit (Python-based UI)  |  
| Backend         | Python (Chainlit + Asyncio) |  
| Data Storage    | Database (audit logs, configs) |  
| Hosting         | Cloud / Server environment  |  

### System Context Diagram  

```mermaid
graph LR
    Candidate[Candidate Browser]
    Frontend[Chainlit Frontend]
    Backend[Chainlit Backend Server]
    Database[(Database)]
    Admin[Admin Interface]

    Candidate -->|View Timer, Submit Answers| Frontend
    Frontend -->|Request Timer Data| Backend
    Backend -->|Store Logs & Configs| Database
    Admin -->|Configure Timer Settings| Backend
```

### Component Interactions  

- The frontend displays the countdown timer, updates every second, and shows warning/critical states.  
- Backend manages the exam timer using server time, triggers auto-save and auto-submit on expiry.  
- Timer state is persisted to the backend to survive page reloads and network issues.  
- Admin interface allows configuration of timer parameters stored in the database.  
- Audit logs capture timing events for compliance and troubleshooting.  

---

## 4. Component Breakdown  

### Timer UI Component  

- Displays the countdown timer in a fixed header on the exam page.  
- Shows different states: Normal, Warning, Critical, Expired with appropriate messages and optional sounds.  
- Updates every second with latency < 100 ms.  
- Supports accessibility features (ARIA roles, keyboard navigation).  
- Localized text for messages.  

### Timer Backend Service  

- Maintains authoritative exam timer using server clock.  
- Handles timer start, pause (if applicable), expiry events.  
- Auto-saves answers and auto-submits exam on expiry.  
- Persists timer state and events to database.  
- Sends timer state updates to frontend on request or reconnect.  

### Admin Configuration Module  

- Provides UI for admins to configure timer duration, warnings, expiry behavior, and accommodations.  
- Validates inputs and stores configurations in database.  
- Applies configurations per exam instance.  

### Persistence & Logging  

- Database tables to store timer configurations, timer event logs, and exam state.  
- Ensures audit trail for compliance.  

---

## 5. API Overview  

The MCQ Timer Feature exposes APIs primarily between the frontend and backend within the Chainlit framework.

| Endpoint                       | Method | Description                              | Request Body                | Response                  | Auth Required |  
|-------------------------------|--------|--------------------------------------|-----------------------------|---------------------------|---------------|  
| `/api/timer/start`             | POST   | Start the exam timer                   | Exam ID, User ID             | Timer start confirmation  | Yes           |  
| `/api/timer/state`             | GET    | Get current timer state for exam/user | Exam ID, User ID             | Timer state (time left, state) | Yes           |  
| `/api/timer/auto-save`         | POST   | Auto-save user answers                 | Exam ID, User ID, Answers    | Save confirmation         | Yes           |  
| `/api/timer/auto-submit`       | POST   | Auto-submit exam on timer expiry      | Exam ID, User ID             | Submit confirmation       | Yes           |  
| `/api/admin/timer/config`      | GET/POST | Get/Set timer configuration           | Config data                  | Config confirmation       | Admin Only    |  
| `/api/timer/log-event`         | POST   | Log timer-related events               | Event details                | Log confirmation          | Yes           |  

### Authentication and Authorization  

- All timer-related API endpoints require authenticated user sessions.  
- Admin endpoints require elevated privileges.  

### Error Handling  

- Standard HTTP error codes (400, 401, 403, 500) used.  
- API returns error messages for invalid inputs or unauthorized access.  
- Frontend handles errors gracefully, displaying user-friendly messages.  

---

## 6. Data Model & Persistence

### Database Schemas

| Table Name          | Description                               |
|---------------------|-------------------------------------------|
| `timer_config`      | Stores admin-configured timer settings per exam. Includes duration, warning thresholds, accommodation flags. |
| `timer_state`       | Stores current timer state per exam session. Includes start time, remaining time, expiry status, and sync timestamps. |
| `timer_event_log`   | Logs all timer events such as start, warning, expiry, autosave, and autosubmit for audit purposes. |
| `exam_answers`      | Stores user answers to questions, supports autosave and final submission persistence. |

### Entity-Relationship Diagram (ERD)

```mermaid
erDiagram
    TIMER_CONFIG {
        int id PK
        int exam_id FK
        int duration_seconds
        int warning_threshold_seconds
        bool auto_submit_enabled
        bool time_accommodations_enabled
        timestamp updated_at
    }
    TIMER_STATE {
        int id PK
        int exam_session_id FK
        timestamp start_time
        int time_remaining_seconds
        bool expired
        timestamp last_sync
    }
    TIMER_EVENT_LOG {
        int id PK
        int exam_session_id FK
        string event_type
        timestamp event_time
        string details
    }
    EXAM_ANSWERS {
        int id PK
        int exam_session_id FK
        int question_id
        int selected_option
        bool is_correct
        timestamp saved_at
    }
    TIMER_CONFIG ||--o{ TIMER_STATE : relates_to
    TIMER_STATE ||--o{ TIMER_EVENT_LOG : logs
    TIMER_STATE ||--o{ EXAM_ANSWERS : stores
```

### Data Validation Rules

- Timer durations must be positive integers within allowed maximum limits.  
- Warning thresholds must be less than timer duration.  
- Auto-submit flag enables or disables auto-submission on expiry.  
- Timer state updates must be atomic and consistent to avoid race conditions.  
- Answer saves must be idempotent to prevent data loss.

### Migration Strategy

- Introduce new tables and columns with zero downtime migrations.  
- Backfill existing exams with default timer configurations if needed.  
- Ensure backward compatibility with exams without timer feature enabled.

### Data Retention Policies

- Timer event logs retained for minimum 6 months for audit compliance.  
- Exam answers and timer states retained per existing exam data policies.

---

## 7. Configuration & Deployment

### Environment Variables

| Variable Name           | Description                                | Default/Example           | Required |
|------------------------|--------------------------------------------|--------------------------|----------|
| `TIMER_AUTO_SUBMIT`    | Enable auto-submit on timer expiry          | `true`                   | Yes      |
| `TIMER_WARNING_THRESH`  | Warning threshold in seconds                 | `300` (5 minutes)        | Yes      |
| `TIMER_ACCOMMODATIONS`  | Enable time accommodations                   | `false`                  | No       |
| `DATABASE_URL`          | Database connection string                    | `postgresql://user:pass@host/db` | Yes      |
| `LOGGING_LEVEL`         | Level of logging detail (INFO, DEBUG, ERROR) | `INFO`                   | No       |

### Configuration Files

- Timer feature settings persisted in the database via admin UI.  
- Application config files include timer-related environment variables.

### Deployment Steps

1. Deploy backend service updates including timer modules.  
2. Deploy frontend changes to include timer UI components.  
3. Run database migrations for new timer tables and schema changes.  
4. Apply configuration environment variables in deployment environment.  
5. Perform smoke tests to verify timer start, warnings, expiry behavior.

### Infrastructure Requirements

- Backend servers must support asynchronous operations for timer events.  
- Database must support transactions for timer state and event logging.  
- Load balancer and session affinity ensure consistent session routing.

### Scaling Considerations

- Use caching for timer configuration data to reduce DB load.  
- Employ horizontal scaling on backend to support concurrent exams.  
- Monitor autosave endpoints for throughput and latency.

---

## 8. Security & Compliance

### Authentication Mechanisms

- User sessions authenticated via existing MCQ app authentication.  
- Timer API endpoints require valid JWT or session tokens.  
- Admin endpoints require role-based access control (RBAC).

### Authorization and Access Control

- Only authorized admins can modify timer configurations.  
- Candidates restricted to read-only timer views and exam submission APIs.

### Data Encryption

- Transport Layer Security (TLS 1.2+) enforced for all API calls.  
- Sensitive data encrypted at rest per organizational policies.

### Input Validation and Sanitization

- Timer configuration inputs validated for type, range, and format.  
- API requests sanitized to prevent injection attacks.

### Compliance Requirements

- Server-authoritative timer implementation ensures exam integrity (audit trail).  
- Timer event logs retained to meet compliance with assessment standards.  
- Accessibility features meet WCAG 2.1 AA guidelines.

### Audit Logging

- All timer state changes and critical events logged with timestamps and user IDs.  
- Logs stored securely and accessible for audit reviews.

### Threat Modeling

- Mitigate client clock tampering via server authoritative timing.  
- Protect against denial-of-service attacks on timer auto-save endpoints.  
- Ensure secure session management to prevent hijacking.

---

## 9. Observability

### Logging Strategy

- Log timer start, warning, expiry, autosave, and auto-submit events.  
- Log errors and exceptions with stack traces for diagnostics.  
- Use structured logging for integration with monitoring systems.

### Monitoring and Alerting

- Monitor timer service uptime and response times.  
- Alert on failed auto-save or auto-submit attempts.  
- Track user session timer expiries and anomalies.

### Performance Metrics

- Timer tick update latency.  
- Autosave success rate.  
- Number of concurrent active timers.

### Health Checks

- Endpoint to verify timer service health and database connectivity.  
- Periodic self-check of timer synchronization accuracy.

### Debugging Approaches

- Enable debug logging in development and test environments.  
- Use session tracing to diagnose user-specific timer issues.

---

## 10. Non-Functional Requirements

### Performance

- Timer UI updates every second with less than 100 ms latency.  
- Backend autosave responses within 200 ms under normal load.

### Scalability

- Support thousands of concurrent exam sessions without degradation.  
- Horizontal scaling of backend timer service with stateless design.

### Reliability and Availability

- Target 99.9% uptime for timer services during exam windows.  
- Auto-save ensures no answer loss under transient network failures.

### Disaster Recovery

- Backup and restore procedures for timer state and event logs.  
- Failover support for database and backend services.

### Accessibility

- Timer UI complies with WCAG 2.1 AA standards.  
- Supports screen readers, keyboard navigation, and color contrast.

### Internationalization/Localization

- Timer messages and tooltips localized per user language settings.  
- Support for right-to-left languages if applicable.

---

## 11. Risks & Mitigation

| Risk                                         | Mitigation Strategy                            |  
|----------------------------------------------|-----------------------------------------------|  
| Client-side clock manipulation               | Use server-authoritative timing; validate client times |  
| Network interruptions causing timer desync  | Persist timer state on server; sync on reconnect |  
| Autosave failures leading to answer loss    | Retry autosave requests; show user notifications |  
| Performance degradation under high load      | Scale backend horizontally; use caching for configs |  
| Unauthorized admin access                     | Implement RBAC and strong authentication      |  
| Accessibility features not meeting standards | Conduct accessibility testing and audits      |  
| Localization errors                           | Use standard i18n libraries and review translations |  

### Known Limitations  

- Timer feature currently supports exam-level timers only; section timers handled separately.  
- Auto-submit behavior may be delayed in extremely high latency environments.

---

## 12. Architecture Decision Records (ADRs)

### ADR-001: Server-Authoritative Timer Design

**Status**: Accepted  
**Date**: 2024-06-10  
**Deciders**: Development Team, Product Manager  

#### Context  
Timing accuracy and exam integrity require preventing client-side clock tampering.  

#### Decision Drivers  
- Security and compliance requirements  
- User experience consistency  
- Auditability of timing events  

#### Considered Options  
1. Client-side timer only  
2. Server-authoritative timer with periodic sync  
3. Hybrid approach with client prediction and server verification  

#### Decision Outcome  
**Chosen option**: Server-authoritative timer with periodic sync to client.  

**Positive Consequences**:  
- Prevents clock tampering  
- Provides audit trail of timing events  
- Ensures timer accuracy  

**Negative Consequences**:  
- Increased backend load  
- Requires reliable client-server communication  

#### Links  
- Related ADR-002 (Auto-save implementation)  

---

### ADR-002: Auto-save and Auto-submit Mechanism

**Status**: Accepted  
**Date**: 2024-06-10  
**Deciders**: Development Team, QA Lead  

#### Context  
To prevent data loss, autosave must reliably save user answers and auto-submit on timer expiry.  

#### Decision Drivers  
- Data reliability  
- User experience (non-intrusive autosave)  
- Performance constraints  

#### Considered Options  
1. Autosave on fixed intervals  
2. Autosave on answer change events  
3. Autosave triggered by timer expiry events  

#### Decision Outcome  
**Chosen option**: Combination of autosave on answer changes and forced auto-submit on expiry.  

**Positive Consequences**:  
- Minimizes data loss  
- Provides smooth user experience  
- Meets compliance for exam integrity  

**Negative Consequences**:  
- More frequent backend calls  
- Complexity in conflict resolution  

#### Links  
- Related ADR-001 (Timer design)  

---

## 13. Assumptions & Constraints

### Assumptions  

- Users have stable network connections during exams.  
- Admin users have proper permissions for timer configurations.  
- Backend infrastructure supports required scaling and async operations.  
- Candidate devices support JavaScript and modern browsers for timer UI.  

### Constraints  

- Timer granularity limited to seconds (1-second ticks).  
- Autosave and auto-submit rely on timely server responses.  
- Accessibility requirements impose UI design constraints.  
- Localization depends on available language resources.  

---

## 14. Dependencies & Integration

| Dependency            | Description                                      | Impact                     |  
|-----------------------|-------------------------------------------------|----------------------------|  
| Chainlit Framework    | Core frontend and backend framework               | High - foundational        |  
| Database              | Storage for timer state, logs, configuration      | High - critical            |  
| User Authentication   | Existing auth system for session management       | Medium - required          |  
| Admin Panel           | Interface for configuring timer settings          | Medium - admin usability   |  
| Network Infrastructure| Connectivity for real-time timer sync             | High - affects reliability |  

### Integration Sequence  

1. Deploy updated backend with timer services.  
2. Deploy frontend timer UI and admin config changes.  
3. Run database migrations and seed default timer configs.  
4. Validate integration with user authentication and admin panel.  

---

## 15. Glossary & References

| Term                | Definition                                        |  
|---------------------|--------------------------------------------------|  
| MCQ                 | Multiple Choice Question                          |  
| Timer Expiry        | Event when exam time runs out                      |  
| Auto-save           | Automatic saving of user answers                   |  
| Auto-submit         | Automatic submission of exam on timer expiry      |  
| Server-authoritative| Timer managed primarily by the backend server     |  
| Accessibility (a11y)| Design to make UI usable by people with disabilities |  
| Localization (l10n) | Adapting UI for different languages and regions   |  

### References  

- Business Requirements Specification (BRS) - MCQ Timer Feature  
- Chainlit Documentation: https://chainlit.io/  
- WCAG 2.1 Accessibility Guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/  
- GDPR Compliance Overview: https://gdpr-info.eu/  
- OWASP Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices/  

---

## 16. Appendices

### Appendix A: Sequence Diagram - Timer Expiry and Auto-Submit Flow

The following sequence diagram illustrates the process flow when the exam timer expires, triggering auto-save and auto-submit:

```mermaid
sequenceDiagram
    participant Candidate
    participant Frontend
    participant Backend
    participant Database

    Frontend->>Backend: Request current timer state
    Backend-->>Frontend: Send timer countdown

    Note over Frontend,Candidate: Timer counts down on UI

    Frontend->>Backend: Notify timer expiry event
    Backend->>Database: Log timer expiry event
    Backend->>Backend: Trigger auto-save and auto-submit
    Backend->>Database: Save final answers and submission status
    Backend-->>Frontend: Confirm submission
    Frontend-->>Candidate: Display exam submission confirmation
```

---

### Appendix B: Sample Timer Configuration JSON

```json
{
  "exam_id": 12345,
  "duration_seconds": 3600,
  "warning_threshold_seconds": 300,
  "auto_submit_enabled": true,
  "time_accommodations_enabled": false,
  "localization": {
    "en": {
      "timer_label": "Time Remaining",
      "warning_message": "5 minutes remaining",
      "expired_message": "Time is up! Your exam has been submitted."
    },
    "es": {
      "timer_label": "Tiempo Restante",
      "warning_message": "Quedan 5 minutos",
      "expired_message": "¡Se acabó el tiempo! Su examen ha sido enviado."
    }
  }
}
```

---

### Appendix C: Code Snippet - Timer Tick Update (Python/Chainlit)

```python
@cl.on_message
async def timer_tick():
    session_id = cl.user_session.get("id")
    timer_state = get_timer_state(session_id)
    if timer_state.expired:
        await auto_submit_exam(session_id)
    else:
        await cl.Message(content=f"Time left: {timer_state.time_remaining} seconds").send()
```

---

## 📄 Converting to Word (.docx)

To convert this Markdown document to Word format, use Pandoc:

### Prerequisites
- Install Pandoc: https://pandoc.org/installing.html
  - Windows: `choco install pandoc` or download installer
  - Mac: `brew install pandoc`
  - Linux: `apt-get install pandoc`

### Conversion Commands

**Basic Conversion**:
```bash
pandoc docs/SDS_MCQ_Timer_Feature_20240610.md -o docs/SDS_MCQ_Timer_Feature_20240610.docx
```

**With Table of Contents**:
```bash
pandoc docs/SDS_MCQ_Timer_Feature_20240610.md -o docs/SDS_MCQ_Timer_Feature_20240610.docx --toc --toc-depth=3
```

**With Custom Styling** (requires reference.docx template):
```bash
pandoc docs/SDS_MCQ_Timer_Feature_20240610.md -o docs/SDS_MCQ_Timer_Feature_20240610.docx --reference-doc=custom-reference.docx --toc
```

### Mermaid Diagrams in Word
Mermaid diagrams must be manually converted:
1. Copy Mermaid code to https://mermaid.live/
2. Export as PNG/SVG
3. Insert images into Word document

---

✅ All 4 parts generated! Would you like me to save and upload this SDS to GitHub? (yes/no)
