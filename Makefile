SHELL := /usr/bin/env bash
PYTHON ?= python3
CI := PYTHONDONTWRITEBYTECODE=1 $(PYTHON) scripts/run_ci.py

.PHONY: help status verify-workstation phase-docs ci-list ci-quick ci-professional ci-release ci-enterprise phase-close

help:
	@printf 'Multiverse Codex developer targets\n'
	@printf '===================================\n'
	@printf 'help                 Show this target list.\n'
	@printf 'status               Show concise git status and progress state.\n'
	@printf 'verify-workstation   Run the Phase 0 workstation verification script.\n'
	@printf 'phase-docs           List canonical phase-control documents.\n'
	@printf 'ci-list              List repo-owned local CI lanes.\n'
	@printf 'ci-quick             Run the fast local CI guardrail.\n'
	@printf 'ci-professional      Run the professional phase-close gate.\n'
	@printf 'ci-release           Run ship-adjacent verification.\n'
	@printf 'ci-enterprise        Run the deepest local verification lane.\n'
	@printf 'phase-close          Alias for ci-professional.\n'

status:
	@git status --short
	@printf '\nProgress state:\n'
	@cat docs/progress.json

verify-workstation:
	@bash scripts/verify-workstation.sh

phase-docs:
	@printf '%s\n' \
		docs/multiverse_codex_phase_plan.md \
		docs/multiverse_codex_phase_completion_checklist.md \
		docs/multiverse_codex_architecture_laws.md \
		docs/multiverse_codex_fresh_chat_workflow_header.md

ci-list:
	@$(CI) --list

ci-quick:
	@$(CI) quick

ci-professional:
	@$(CI) professional

ci-release:
	@$(CI) release

ci-enterprise:
	@$(CI) enterprise

phase-close: ci-professional
