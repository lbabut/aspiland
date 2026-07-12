# SANDBOX-01 / Cubic Fingerprint

Status: Design draft

## Research question

Do the arrival directions and maximum observed energies of ultra-high-energy cosmic rays contain a reproducible anisotropy compatible with a cubic computational lattice?

## Competing hypotheses

### H0 — rotationally symmetric physics

After accounting for detector exposure, source distribution, magnetic deflection and known astrophysical structure, no preferred orthogonal lattice axes remain.

### H1 — cubic lattice signature

At sufficiently high energy, propagation or the available momentum states exhibit a small violation of rotational symmetry aligned with three mutually perpendicular axes. The effect should strengthen with energy and reproduce in independent datasets.

This hypothesis tests one specific architecture. Failure to find the signature does not show that no simulation exists.

## Preregistration requirements

Before examining confirmation data, record:

- datasets and observation periods;
- energy threshold and energy bins;
- sky mask and detector-exposure correction;
- treatment of magnetic deflection and source clustering;
- exact cubic-symmetry statistic;
- nuisance parameters;
- number of searched orientations and trials correction;
- discovery and replication thresholds;
- exclusion and missing-data rules;
- analysis code revision and random seeds.

## Proposed analysis

1. Transform all events into a common celestial coordinate system.
2. Apply published exposure functions for each observatory.
3. Fit ordinary anisotropy models and known large-scale structure first.
4. Scan the orientation of an orthogonal three-axis frame.
5. Measure whether residual event density or maximum energy follows cubic symmetry rather than a generic dipole, quadrupole or source pattern.
6. Estimate global significance with exposure-matched Monte Carlo skies.
7. Freeze the model and test it on an untouched dataset or later observation period.
8. Seek confirmation from an independent observatory.

## Evidence standard

A candidate result must satisfy all of the following:

- global statistical significance after orientation and threshold trials;
- the same axes in independent confirmation data;
- increasing effect size at higher energies;
- robustness to calibration uncertainty and reasonable magnetic-field models;
- better predictive performance than ordinary astrophysical alternatives;
- independent reproduction by another team.

## Outcomes

### Null result

Publish constraints on lattice spacing or model parameters. A null result is useful because it excludes part of the model space.

### Anomaly

Classify it as an unexplained rotational-symmetry anomaly. Do not describe it as proof of a simulation until instrumental, statistical and physical explanations have been exhausted.

### Confirmed symmetry violation

Treat it as evidence for new physics with a preferred structure. Simulation language remains only one interpretation among several.

## Data and reproducibility

The intended implementation should contain:

```text
SANDBOX-01/
├── README.md
├── preregistration.md
├── data-sources.md
├── environment.yml
├── src/
├── tests/
├── notebooks/
└── results/
```

Raw observatory data should not be committed when licensing or size makes that inappropriate. Store download instructions, checksums and provenance instead.

## Related literature

- Beane, Davoudi and Savage, *Constraints on the Universe as a Numerical Simulation*, arXiv:1210.1847.
- High-energy photon time-of-flight tests provide a related but distinct probe of modified propagation.
- Interferometric searches for correlated geometric noise provide another distinct test class.

## Safety against self-deception

The experiment explicitly excludes retrospective pattern matching, numerology, personally meaningful coincidences and changing the hypothesis after results are visible. Unexpected findings must be converted into a new preregistered experiment before they count as confirmatory evidence.
