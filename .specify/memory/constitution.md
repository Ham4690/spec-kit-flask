<!-- Sync Impact Report (v1.0.0)
VERSION: 0.0.0 → 1.0.0 (MINOR - Initial constitution for Flask project)
NEW PRINCIPLES:
  1. I. Test-First Development
  2. II. Simplicity (YAGNI)
  3. III. Documentation Excellence
ADDED SECTIONS:
  - Governance (amendment procedures, versioning, compliance)
TEMPLATES UPDATED: ✅ All dependent templates reviewed for compatibility
FOLLOW-UP TODOS: None - initial ratification complete
-->

# spec-kit-flask Constitution

## Core Principles

### I. Test-First Development

Test-driven development (TDD) is non-negotiable. Tests MUST be written before implementation code. All changes MUST include:
- Unit tests for individual functions and methods
- Integration tests for component interactions
- Acceptance tests aligned with user stories (given/when/then format)

The Red-Green-Refactor cycle is mandatory: tests fail first, implementation follows, then refactor for clarity.

**Rationale**: Tests serve as executable specifications, catch regressions early, and document intended behavior. TDD disciplines design decisions and ensures code quality from the start.

### II. Simplicity (YAGNI)

You Aren't Gonna Need It (YAGNI). Every feature MUST solve the current requirement, no more. No speculative abstractions, no premature optimization, no unused helper functions.

Implementation approach:
- Start with the simplest solution that works
- Avoid over-engineering for "future extensibility"
- Add complexity only when requirements demand it
- Delete unused code immediately

**Rationale**: Simpler code is easier to understand, test, and maintain. Over-engineering introduces bugs, increases cognitive load, and creates unmaintainable systems. Simplicity is a feature.

### III. Documentation Excellence

Every module, function, and complex algorithm MUST be documented. Documentation MUST be:
- Clear and concise (plain language, not jargon)
- Co-located with code (docstrings, inline comments for non-obvious logic)
- Kept synchronized with implementation (not allowed to drift)
- Accessible to developers at all experience levels

README files MUST include:
- Purpose and scope of the module
- Quick start / usage examples
- Key design decisions and their rationale
- Known limitations or caveats

**Rationale**: Documentation reduces onboarding friction, prevents tribal knowledge, and ensures knowledge survives team transitions. Clear docs are a sign of clear thinking.

## Governance

### Amendment Procedure

Changes to this constitution MUST:
1. Be proposed with a written rationale (why the change, what problem it solves)
2. Be reviewed by at least one other developer to ensure alignment with project values
3. Be documented in the git log with version bump and amendment date
4. Be propagated to dependent artifacts (templates, guidelines, processes)

### Versioning Policy

Constitution versions follow semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Backward-incompatible principle removals or complete redefinitions
- **MINOR**: New principles added or significant principle clarifications
- **PATCH**: Wording improvements, typo fixes, non-semantic refinements

### Compliance & Review

- All pull requests MUST verify compliance with these principles
- Code review checklist MUST include: "Does this follow the constitution?"
- Violations MUST be flagged and resolved before merge
- Quarterly review of constitution effectiveness against project health

**Version**: 1.0.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27

## IV. Flask API Project Standards

This project follows a **minimal, opinionated Flask API architecture** optimized for clarity, speed, and low cognitive overhead.

### Technology Stack

- **Language**: Python 3.10
- **Framework**: Flask 3.1
- **Package Management / Execution**: uv
- **Build System**: hatchling (via hatching)
- **Linting / Formatting**: ruff (single source of truth)
- **Testing**: pytest 8.4

No additional tooling is permitted unless it clearly reduces complexity.

---

### Application Structure & Execution

- Flask MUST be started via **CLI mode**
- Local development server runs on **localhost:8080**
- Entry point MUST be executed through `uv`

```bash
$ uv run flask run
