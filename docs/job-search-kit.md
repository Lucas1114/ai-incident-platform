# Job Search Kit

Use the versions below as starting points and adjust the number of bullets to
fit the application. Every claim is limited to the implementation in this
repository and its public portfolio deployment.

## Resume bullets

Recommended three-bullet version:

- Built a Python and FastAPI application that turns incident descriptions into structured investigation briefs using the OpenAI Responses API and Pydantic validation.
- Containerized and deployed a browser interface and REST API to Google Cloud Run, with API credentials stored in Google Secret Manager.
- Added input and output limits, per-client rate limiting, controlled upstream error responses, seven automated tests, and GitHub Actions checks for tests and Docker builds.

Alternative bullet for AI-focused roles:

- Designed schema-constrained LLM output that separates observed evidence from an unconfirmed leading hypothesis and returns one diagnostic next action.

Alternative bullet for backend-focused roles:

- Defined validated request and response contracts, HTTP `429` rate-limit behavior with `Retry-After`, and controlled HTTP `502` handling for upstream model failures.

## LinkedIn Projects entry

### AI Incident Investigation Platform

Built and deployed an AI-assisted incident investigation application using
Python, FastAPI, Pydantic, and Google Cloud Run. The application turns an
incident description into a structured brief containing a summary, severity
assessment, observed evidence, an explicitly unconfirmed leading hypothesis,
and one diagnostic next action.

Implemented a responsive browser interface, REST API, Docker packaging, seven
automated tests, GitHub Actions checks, secret management, and basic request and
cost controls for a public portfolio demo.

**Technologies:** Python, FastAPI, Pydantic, OpenAI Responses API, Google Cloud
Run, Google Secret Manager, Docker, GitHub Actions, HTML, CSS, JavaScript

**Links:** [Live demo](https://ai-incident-platform-152544821369.australia-southeast1.run.app/)
· [Source code](https://github.com/Lucas1114/ai-incident-platform)

## LinkedIn announcement

I built and deployed an AI Incident Investigation Platform to practise taking
an LLM-powered application from API implementation to a public cloud
deployment.

It turns an incident description into a structured investigation brief: a
summary, severity assessment, observed evidence, an unconfirmed leading
hypothesis, and one diagnostic next action.

The engineering work included:

- FastAPI and Pydantic for validated API contracts
- OpenAI structured responses
- Docker and Google Cloud Run deployment
- Automated tests and GitHub Actions checks
- Secret management, rate limiting, and request and output limits

One design decision I focused on was keeping a plausible hypothesis clearly
separate from a confirmed root cause.

This is a small portfolio project, built to demonstrate backend, cloud, and AI
engineering fundamentals. I would welcome feedback on the implementation.

[Try the demo](https://ai-incident-platform-152544821369.australia-southeast1.run.app/)
· [Explore the code](https://github.com/Lucas1114/ai-incident-platform)

#Python #BackendEngineering #CloudComputing #AIEngineering

## Skills and keywords

Prioritize the terms most relevant to each role instead of copying the entire
list into every application.

- **Backend:** Python, FastAPI, Pydantic, REST APIs, API design, schema validation, input validation, error handling, rate limiting
- **Cloud:** Google Cloud Platform (GCP), Cloud Run, Google Secret Manager, Docker, containerization
- **AI engineering:** LLM integration, OpenAI Responses API, structured outputs, prompt design
- **Engineering quality:** automated testing, API testing, mocking, GitHub Actions, continuous integration, Git
- **Frontend support:** HTML, CSS, JavaScript, responsive design

## Claims to avoid

Do not describe the project as serving production users or operating at scale.
Do not claim automated root-cause analysis, autonomous remediation, retrieval-
augmented generation, model training, measured reliability improvements, or
continuous deployment. The current GitHub Actions workflow runs tests and
builds the image; it does not deploy it.
