# Architecture

The API contract is independent of the legacy implementation.

- **API:** external contract and validation
- **Service:** business orchestration
- **Adapter:** translation to legacy interfaces
- **Legacy system:** replaceable implementation
- **Observability:** correlation and operational telemetry

## Cloud target

```text
Clients -> API Gateway -> Kubernetes Service -> Modernization API -> Legacy Adapter -> Legacy Platform
```

Add WAF, managed secrets, service identity, autoscaling, distributed tracing, and centralized logging in production.
