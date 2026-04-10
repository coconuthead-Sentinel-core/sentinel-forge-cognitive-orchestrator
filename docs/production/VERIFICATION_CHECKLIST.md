# Verification Checklist - Gold Standard

This checklist must be completed for **every individual task** listed in the `TASK_LIST.md` before it can be marked as complete. This ensures every component meets our gold standard for production quality.

---

### Task ID: `[Enter Task ID, e.g., 4.1]`

### Task Description: `[Enter Task Description]`

---

### ✅ 1. Code Quality & Style

- [ ] **Linting:** Code passes all `pylint` / `flake8` checks with zero errors.
- [ ] **Formatting:** Code is formatted using `black` to ensure consistency.
- [ ] **Type Hinting:** All functions and methods have complete and accurate type hints.
- [ ] **Readability:** Code is clear, concise, and follows Pythonic best practices. Variable and function names are descriptive.

### ✅ 2. Testing & Reliability

- [ ] **Unit Tests:** Comprehensive unit tests are written for all new functions and classes.
- [ ] **Integration Tests:** Tests are written to verify the component's interaction with other parts of the system.
- [ ] **Test Coverage:** Code coverage for the new code is above 98%.
- [ ] **All Tests Passing:** The entire test suite (`pytest tests/`) passes successfully.

### ✅ 3. Documentation

- [ ] **Docstrings:** All public modules, classes, functions, and methods have clear, descriptive docstrings in Google format.
- [ ] **Inline Comments:** Complex or non-obvious logic is explained with inline comments.
- [ ] **Architecture Document:** `ARCHITECTURE.md` is updated if the change impacts the system's design.
- [ ] **API Document:** `docs/API.md` is updated if the change affects any public-facing API endpoints.

### ✅ 4. Security

- [ ] **No Hardcoded Secrets:** No API keys, passwords, or other secrets are present in the code. All secrets are loaded from the environment via the `core/config.py` module.
- [ ] **Input Validation:** All inputs from external sources (API requests, user data) are rigorously validated and sanitized.
- [ ] **Dependency Scan:** No vulnerable packages were added. A `snyk` or `pip-audit` scan has been run.
- [ ] **Permissions:** The code does not require excessive permissions to run.

### ✅ 5. Performance

- [ ] **Efficiency:** Algorithms and data structures are chosen for optimal performance. No obvious performance bottlenecks exist.
- [ ] **Resource Management:** Resources like database connections and file handles are properly managed and released.
- [ ] **Scalability:** The code is designed with scalability in mind and can handle increased load.

### ✅ 6. Peer Review

- [ ] **Pull Request:** The change is submitted as a pull request.
- [ ] **Reviewer Approval:** The pull request has been reviewed and approved by at least one other team member.
- [ ] **CI/CD Pipeline:** The pull request passes all automated checks in the CI/CD pipeline.

---

### Sign-off

- **Developer:** _________________________
- **Reviewer:** _________________________
- **Date:** _________________________
