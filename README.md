# AI Incident Investigation Platform

[![CI](https://github.com/Lucas1114/ai-incident-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Lucas1114/ai-incident-platform/actions/workflows/ci.yml)

A FastAPI service that uses structured LLM output to summarize an incident,
assign its severity, identify a leading hypothesis, list observed evidence, and
recommend one next action.

## API

The service is deployed on Google Cloud Run:

- API documentation: https://ai-incident-platform-152544821369.australia-southeast1.run.app/docs
- Health check: https://ai-incident-platform-152544821369.australia-southeast1.run.app/health

Send an incident description to `POST /investigate`:

```json
{
  "incident": "Checkout latency increased and payment-provider calls timed out."
}
```

To control public-demo usage, incident descriptions are limited to 4,000
characters and each client can submit up to five investigations per hour.
Rate-limited requests return HTTP `429` with a `Retry-After` header.

## Run locally

Set `OPENAI_API_KEY`, then run:

```shell
uvicorn app.main:app --reload
```

## Container

```shell
docker build -t ai-incident-platform .
docker run --rm -p 8080:8080 --env OPENAI_API_KEY ai-incident-platform
```
