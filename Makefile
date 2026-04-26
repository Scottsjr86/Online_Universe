SHELL := /usr/bin/env bash

.PHONY: help status verify-workstation phase-docs

help:
	@printf 'Multiverse Codex developer targets\n'
	@printf '===================================\n'
	@printf 'help                Show this target list.\n'
	@printf 'status              Show concise git status and progress state.\n'
	@printf 'verify-workstation  Run the Phase 0 workstation verification script.\n'
	@printf 'phase-docs          List canonical phase-control documents.\n'

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
