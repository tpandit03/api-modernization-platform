# ADR 001: Strangler Facade

## Decision
Use an API facade and adapter as the migration boundary.

## Rationale
It reduces blast radius and allows consumers to adopt a stable modern contract before the legacy implementation is fully replaced.

## Trade-off
Both modern and legacy paths operate during migration, increasing temporary operational complexity.
