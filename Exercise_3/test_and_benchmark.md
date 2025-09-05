# Test and Benchmark the Agent

This folder contains scripts to perform end-to-end tests and benchmarking of the Exercise_2 Movie Agent.

Contents:
- e2e_test.py — a short conversational end-to-end test that logs inputs, timing, and results.
- benchmark.py — runs multiple prompts over several repetitions and saves detailed logs and a summary report.
- test_cases.json — example prompts for benchmarking.
- logs/ — output logs directory (created automatically).

## Prerequisites

- Python environment that can import the Exercise_2 package from project root.
- Internet connectivity (the agent calls iTunes and Wikipedia).
- LLM backend (llamafile) running and reachable at LLAMAFILE_BASE_URL.
  - Default: http://localhost:8080/v1
  - Example to start: `./Exercise_2/your_choosen_model.llamafile --server --port 8080`
  - Optionally export: `export LLAMAFILE_BASE_URL=http://127.0.0.1:8080/v1`

Option A: Use in-process TestClient (default)
- Pros: No need to launch the FastAPI server separately.
- Cons: Still requires llamafile server to be up (the app checks readiness via LLAMAFILE_BASE_URL).

Option B: Target a running web server
- Start the web app server in another terminal, for example:
  - `python -m uvicorn Exercise_2.web_app:app --host 127.0.0.1 --port 8000`
- Then pass `--server-url http://127.0.0.1:8000` to the scripts below.

## Running the E2E Test

- Simple run (in-process):
  - `python -m Exercise_3.e2e_test --prompt "lighthearted sci-fi from the 90s"`
- Against a running server:
  - `python Exercise_3/e2e_test.py --server-url http://127.0.0.1:8000 --prompt "romantic comedy 2005"`
- Output: JSONL log written to Exercise_3/logs/e2e_log_YYYYmmdd_HHMMSS.jsonl containing per-step inputs, timestamps, durations, HTTP status, and a compact result summary.

## Running the Benchmark

- With example prompts:
  - `python -m Exercise_3.benchmark --repeats 3 --prompts-file Exercise_3/test_cases.json`
- Against a running server:
  - `python Exercise_3/benchmark.py --server-url http://127.0.0.1:8000 --repeats 5`
- Output:
  - JSONL per-run log at Exercise_3/logs/bench_runs_YYYYmmdd_HHMMSS.jsonl
  - Summary JSON at Exercise_3/logs/bench_runs_YYYYmmdd_HHMMSS_summary.json with avg/p50/p95 latency and success rates per prompt and overall.

## What gets recorded

- For every request: input text, HTTP status, start/end timestamps, duration (ms), result count, and a compact list of the first few titles (if any).
- For benchmark summary: success rates, average and percentile latencies, and average results per prompt.

## Troubleshooting

- 503 LLM backend not ready:
  - Ensure llamafile is running and LLAMAFILE_BASE_URL is correct.
  - Example: `export LLAMAFILE_BASE_URL=http://127.0.0.1:8080/v1`
- Network errors: the agent relies on iTunes/Wikipedia; ensure internet access.
- Import errors: run scripts from repository root so that `Exercise_2` is importable.

## Disclaimer

This file is generated with the help of Junie. If there are any mistakes or misinformation, please summit an issue [here]().
