# AI Incident Investigation Platform

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
