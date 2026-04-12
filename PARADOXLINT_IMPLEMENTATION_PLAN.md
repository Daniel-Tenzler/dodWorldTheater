# ParadoxLint Implementation Plan

## 1) Goal and Scope

Build an ESLint-like linter for Paradox/Victoria 2 mod files that provides:

- One-line execution (`paradoxlint .`)
- Consistent diagnostics with file/line/column/rule-id/severity
- Configurable rules and severities
- Safe auto-fixes for selected style issues
- CI-friendly exit codes and machine-readable reports

This tool will supersede and eventually replace the current `validate_mod.sh` script with a parser-driven, extensible architecture.

---

## 2) Product Requirements

### 2.1 User Experience

- Run from repo root or any subfolder
- Detect mod root automatically (for example by `.mod` file + expected folder structure)
- Human-friendly default output
- Optional JSON and SARIF output for CI/code-scanning
- Fast incremental reruns using cache

### 2.2 CLI Contract

Primary command:

```bash
paradoxlint [path]
```

Required options:

- `--config <file>`: config path override
- `--format <stylish|json|sarif|compact>`: output format
- `--fix`: apply safe fixes
- `--max-warnings <n>`: fail build when warnings exceed threshold
- `--no-cache`: disable cache
- `--cache-location <file>`: cache file path
- `--rule <rule-id:severity>`: runtime override
- `--quiet`: show errors only
- `--stdin --stdin-filename <path>`: editor integration

Exit codes:

- `0`: no errors and warnings <= threshold
- `1`: lint errors or warnings above threshold
- `2`: internal/config/runtime failure

---

## 3) Technology and Packaging

### 3.1 Recommended Stack

- Language: Python 3.11+
- Parser: custom tokenizer + recursive descent parser for Paradox script
- CLI: `typer` (or `argparse` if zero dependencies preferred)
- Config: YAML via `ruamel.yaml` or `PyYAML`
- Reporting: built-in formatters + SARIF emitter
- Testing: `pytest`

### 3.2 Distribution

- `pyproject.toml` with console script entry point:
  - `paradoxlint = paradoxlint.cli:app`
- Install modes:
  - Local dev: `pip install -e .`
  - CI: `pip install .`
- Optional wrapper script for repo convenience:
  - `./lint_mod.sh` or `./lint_mod.ps1` that calls `paradoxlint .`

---

## 4) Repository Layout

```text
paradoxlint/
  __init__.py
  cli.py
  engine.py
  config.py
  cache.py
  diagnostics.py
  file_discovery.py
  parser/
    tokenizer.py
    ast.py
    parser.py
    trivia.py
  rules/
    __init__.py
    base.py
    registry.py
    syntax_unbalanced_braces.py
    style_spacing_around_equals.py
    events_duplicate_ids.py
    events_id_range_policy.py
    localization_semicolon_columns.py
    localization_missing_keys.py
    map_invalid_province_refs.py
    decisions_required_blocks.py
  index/
    symbol_tables.py
  formatters/
    stylish.py
    compact.py
    json_formatter.py
    sarif_formatter.py
  fixes/
    edits.py
    applier.py
tests/
  parser/
  rules/
  integration/
docs/
  rules.md
  config.md
```

---

## 5) Parsing and Data Model

### 5.1 Tokenizer

Tokenize:

- Identifiers
- Numbers
- Strings
- Operators (`=`, `{`, `}`)
- Comments (`#` line comments)
- Whitespace/newlines as trivia for accurate source mapping and fixes

### 5.2 AST

Represent:

- Assignment nodes (`key = value`)
- Block nodes (`key = { ... }`)
- Value nodes (identifier/number/string/block)
- Generic list/entries to tolerate mixed syntaxes used in mods

Each node stores:

- File path
- Start/end line + column
- Parent links (optional, useful for rule context)

### 5.3 Error Tolerance

Parser must recover from malformed segments and continue to produce partial AST so multiple errors can be reported in one run.

---

## 6) Rule Engine Design

### 6.1 Rule Interface

Each rule defines:

- `id` (for example `events/duplicate-id`)
- `default_severity` (`error` or `warning`)
- `applies_to` (file globs and optional AST node types)
- `check(context) -> list[Diagnostic]`
- Optional `fix(diagnostic, context) -> list[TextEdit]`

### 6.2 Execution Model

- Phase A: per-file parse + file-local rules
- Phase B: project indexing (event IDs, loc keys, province definitions)
- Phase C: cross-file rules using index
- Deterministic ordering of diagnostics (path, line, column, rule)

### 6.3 Rule Configuration

Config supports:

- `off | warn | error`
- Rule options object
- Path-specific overrides

Example:

```yaml
rules:
  syntax/unbalanced-braces: error
  style/spacing-around-equals:
    level: warn
    options:
      require_single_space: true
overrides:
  - files: ["events/**/*.txt"]
    rules:
      events/id-range-policy: error
```

---

## 7) Initial Rule Set (MVP + parity with `validate_mod.sh`)

### 7.1 Syntax and Style

1. `syntax/unbalanced-braces` (error)
2. `style/spacing-around-equals` (warn, auto-fixable)

### 7.2 Events

3. `events/duplicate-id` (error)
4. `events/id-range-policy` (warn/error configurable)

### 7.3 Localization

5. `localization/semicolon-columns` (warn)
6. `localization/missing-key` (warn, cross-check against event/decision/title/desc references)

### 7.4 Map/Province

7. `map/invalid-province-reference` (error)

### 7.5 Decisions

8. `decisions/required-blocks` (warn; checks `political_decisions`, `potential`, `allow`, `effect`)

### 7.6 Additional High-Value Rules (post-MVP)

9. `events/missing-title-or-desc`
10. `events/option-without-name`
11. `scope/unknown-trigger-or-effect` (backed by known keyword lists)
12. `localization/duplicate-key`
13. `format/tabs-indentation-policy`
14. `compat/disallowed-vanilla-overwrite` (project-specific policy)

---

## 8) Config Specification

Default config file names:

- `.paradoxlintrc.yml`
- `.paradoxlintrc.yaml`
- `paradoxlint.yml`

Top-level keys:

- `mod_root`: explicit root if auto-detect fails
- `include`: glob list
- `ignore`: glob list
- `rules`: rule map
- `overrides`: per-path config blocks
- `id_policies`: reserved/allowed ranges by domain
- `localization`: expected column count, file patterns
- `map`: definition.csv location override

Baseline support:

- `baseline_file`: path to stored accepted findings
- `--update-baseline`: regenerate baseline

---

## 9) Output and Developer Experience

### 9.1 Default Human Output

Format:

```text
events/amazonia.txt:123:9  error  Duplicate event id 98401  events/duplicate-id
```

Summary:

- file count
- elapsed time
- errors/warnings by rule

### 9.2 Machine Output

- JSON (structured diagnostics + metadata)
- SARIF for GitHub code scanning / CI annotations

### 9.3 Rule Docs

Generate `docs/rules.md` from rule metadata:

- description
- why it matters
- examples (bad/good)
- fixability

---

## 10) Performance and Scaling

### 10.1 Targets

- Cold run on full repo: <= 8 seconds (target)
- Warm run with cache: <= 2 seconds (target)

### 10.2 Strategies

- Hash-based file cache (mtime + size + fingerprint)
- Parallel parsing/rule execution (process pool) with deterministic merge
- Separate incremental index updates for changed files only

---

## 11) Testing Strategy

### 11.1 Unit Tests

- Tokenizer coverage for edge syntax
- Parser recovery tests for malformed files
- Rule-level tests with minimal fixtures

### 11.2 Integration Tests

- Fixture repos with expected diagnostics snapshots
- CLI behavior tests (exit codes, format outputs, max-warnings)

### 11.3 Regression Tests

- Import current `validate_mod.sh` sample cases and verify parity
- Add real-world bugs from repo history as fixtures

### 11.4 Quality Gates

- Lint (ruff/flake8)
- Type check (mypy/pyright)
- Tests (pytest)
- Packaging smoke test (`pip install .` + `paradoxlint --help`)

---

## 12) CI/CD Integration

Pipeline steps:

1. Install Python and dependencies
2. Install package
3. Run `paradoxlint . --format compact --max-warnings 0`
4. Optionally emit SARIF artifact

Optional pre-commit hook:

- Lint changed files before commit

---

## 13) Migration Plan from `validate_mod.sh`

### Stage 1: Side-by-side

- Keep `validate_mod.sh` as legacy
- Introduce `paradoxlint` with equivalent checks
- Compare outputs for several real branches

### Stage 2: Default shift

- Update docs and team workflow to use `paradoxlint .`
- Keep shell script as compatibility wrapper that calls `paradoxlint`

### Stage 3: Retirement

- Remove duplicated shell logic once confidence is high

---

## 14) Detailed Delivery Roadmap

### Milestone 1: Foundation (Week 1)

- CLI skeleton and config loader
- File discovery + ignore handling
- Tokenizer + basic parser + diagnostics model
- Stylish formatter

Exit criteria:

- `paradoxlint .` runs and reports parser errors with line/col

### Milestone 2: MVP Rules (Week 2)

- Implement 8 parity rules from current script
- Build project index for events/localization/provinces
- Add JSON formatter

Exit criteria:

- Feature parity with `validate_mod.sh` on core checks

### Milestone 3: Auto-fix + SARIF + Cache (Week 3)

- Implement safe fixes for style rules
- Add SARIF output
- Add caching and no-cache switch

Exit criteria:

- CI-ready execution and measurable rerun speedup

### Milestone 4: Hardening (Week 4)

- Baseline support
- Improved parser recovery
- Additional high-value rules and rule docs
- Cross-platform packaging and release process

Exit criteria:

- Stable, documented, team-adopted linter with predictable output

---

## 15) Risks and Mitigations

1. Grammar ambiguity across Paradox files
   - Mitigation: tolerant parser + rule-specific guards + broad fixtures

2. False positives from strict assumptions
   - Mitigation: configurable rules, per-path overrides, baseline mode

3. Performance degradation on large mod repos
   - Mitigation: cache + parallelism + incremental index

4. Team adoption friction
   - Mitigation: compatible defaults, clear docs, migration wrapper

---

## 16) Definition of Done

The implementation is complete when all items below are true:

- `paradoxlint .` is available as a one-line command
- Parser-driven diagnostics include file/line/column/rule/severity
- MVP parity rules implemented and tested
- Config + overrides + ignore behavior documented
- `--fix` works for designated safe rules
- JSON and SARIF outputs validated
- CI integration is in place and enforced
- Legacy script is either wrapped or officially deprecated

---

## 17) Immediate Next Actions

1. Approve Python stack and command name (`paradoxlint`)
2. Create package skeleton and CLI entrypoint
3. Implement parser and diagnostics core
4. Port the 8 existing checks as first rules
5. Wire CI with `--max-warnings 0`
