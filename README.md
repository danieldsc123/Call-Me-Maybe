*This project has been created as part of the 42 curriculum by <login1>.*

# Call Me Maybe

## Description

Translate natural-language requests into structured function calls using
Qwen/Qwen3-0.6B and constrained decoding.

The command-line interface, JSON file reader, and Pydantic input validation are
implemented. Empty function catalogs and duplicate function names are rejected. Dependencies
are configured with uv, and the provided SDK and sample inputs are included.
Model inference, output schema validation, constrained decoding, output writing,
and the Makefile remain to be implemented.
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

The provided SDK is installed as a local workspace package in llm_sdk/.
Local development tests belong in tests/ and are excluded from Git.
Generated results belong in data/output/ and are excluded from Git.

## Instructions

Run `uv sync` from the repository root to install dependencies.
The required execution interface is `uv run python -m src`, with optional
`--functions_definition`, `--input`, and `--output` arguments.
The command currently reads and validates both JSON inputs and reports errors without
a traceback. It does not process requests or generate an output file yet.

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

Input validation has been checked with valid inputs, missing fields, wrong types,
empty function catalogs, and duplicate function names.
To be implemented: JSON and schema constraints, unseen function
catalogs, argument extraction, error handling, and performance checks.

## Example Usage

Run `uv run python -m src` to read the default input files, or
`uv run python -m src --help` to view the available options.

## Resources

- Call Me Maybe subject, version 1.7.
- AI assistance: subject explanation, architecture planning, scaffolding,
  guided CLI and JSON reader implementation, error handling, and verification.
- Add documentation and references consulted during implementation.
