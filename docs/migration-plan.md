# Migration Plan

## Phase 1 — Establish the seam
Introduce the facade and adapter without changing legacy behavior.

## Phase 2 — Instrument
Add correlation IDs, latency metrics, error rates, and trace propagation.

## Phase 3 — Migrate capability by capability
Move one domain operation at a time behind the modern boundary.

## Phase 4 — Dual run
Compare modern and legacy results for selected traffic.

## Phase 5 — Cut over
Shift traffic gradually with rollback capability.

## Phase 6 — Decommission
Remove legacy capability only after operational and business acceptance criteria are met.
