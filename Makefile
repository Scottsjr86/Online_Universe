SHELL := /usr/bin/env bash

.PHONY: help status verify-workstation phase-docs ci-quick ci-professional ci-release phase-close

help:
	@printf 'Multiverse Codex developer targets\n'
	@printf '===================================\n'
	@printf 'help                 Show this target list.\n'
	@printf 'status               Show concise git status and progress state.\n'
	@printf 'verify-workstation   Run the Phase 0 workstation verification script.\n'
	@printf 'phase-docs           List canonical phase-control documents.\n'
	@printf 'ci-quick             Run fast local CI checks.\n'
	@printf 'ci-professional      Run the professional phase-close gate.\n'
	@printf 'ci-release           Run the deepest local release gate currently available.\n'
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

ci-quick:
	@bash scripts/local-ci.sh quick

ci-professional:
	@bash scripts/local-ci.sh professional

ci-release:
	@bash scripts/local-ci.sh release

phase-close: ci-professional
