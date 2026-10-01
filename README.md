*This project has been created as part of the 42 curriculum by <login1>.*

# Call Me Maybe

## Description

Translate natural-language requests into structured function calls using
Qwen/Qwen3-0.6B and constrained decoding.

This repository currently contains a scaffold only. Python modules, the
Makefile, and pyproject.toml are intentionally empty for manual implementation.
The input JSON files contain empty arrays and must be populated before testing.
Replace <login1> above with your 42 login.

## Architecture

| Module | Responsibility |
| --- | --- |
| src/__main__.py | Application entry point. |
| src/cli.py | Command-line arguments and default paths. |
| src/schemas.py | Pydantic models and dynamic schema validation. |
| src/file_io.py | JSON file reading, writing, and file error handling. |
| src/prompting.py | Instructions and function definitions for the model. |
| src/llm_client.py | Access to the public SDK methods and vocabulary. |
| src/constraints.py | Partial JSON state and schema-valid continuations. |
| src/decoder.py | Token generation, logit masking, and termination. |
| src/pipeline.py | Coordinate request processing and result validation. |

The provided SDK must be copied into llm_sdk/ beside src/.
Local development tests belong in tests/ and are excluded from Git.
Generated results belong in data/output/ and are excluded from Git.

## Instructions

Pending implementation: configure dependencies with uv and generate uv.lock.
The required execution interface is `uv run python -m src`, with optional
`--functions_definition`, `--input`, and `--output` arguments.
This command does not process requests yet.

The Makefile must later provide install, run, debug, clean, and lint targets.

## Algorithm Explanation

To be documented after implementing constrained decoding.

## Design Decisions

Separate file handling, input validation, SDK interaction, decoding constraints,
and orchestration so each responsibility can be implemented and studied independently.

## Performance Analysis

No measurements yet. Targets: at least 90% accuracy, 100% valid and
schema-compliant JSON, and processing the test prompts in under five minutes.

## Challenges Faced

To be recorded during development.

## Testing Strategy

To be implemented: input validation, JSON and schema constraints, unseen function
catalogs, argument extraction, error handling, and performance checks.

## Example Usage

To be completed after the command-line interface is implemented.

## Resources

- Call Me Maybe subject, version 1.7.
- AI assistance: subject explanation, architecture planning, and creation of
  the initial scaffold. Python implementation has not been generated.
- Add documentation and references consulted during implementation.
