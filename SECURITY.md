# Security policy

Aspiland contains active experiments and a large body of legacy material. Security reports help protect contributors, users, data and infrastructure without exposing additional sensitive information.

## Reporting a vulnerability or exposed secret

Do not post credentials, private keys, tokens, personal data, exploit details or sensitive infrastructure information in a public issue, pull request, commit or discussion.

Use GitHub private vulnerability reporting when it is available for this repository. Otherwise contact the repository owner through an established private channel and provide only the minimum information needed to locate and contain the problem.

A useful report includes:

- the affected path, project or component;
- the type and likely impact of the issue;
- safe reproduction steps;
- whether data or credentials may already have been exposed;
- a suggested containment step, if known.

Redact the actual secret. A fingerprint, key identifier, filename or short non-sensitive description is usually sufficient.

## Exposed-secret response

A secret that has appeared in an accessible file, message, log or repository must be treated as compromised even when its purpose is unknown.

1. Revoke, disable or rotate the secret at its issuing system.
2. Identify systems, accounts and logs that may have used it.
3. Remove accessible copies from current storage.
4. Search for duplicates in repositories, backups, Drive folders, exported archives and deployment systems.
5. Review access logs where available and proportionate.
6. Decide whether repository-history rewriting or backup cleanup is necessary; do not rewrite history casually.
7. Record the incident without reproducing the secret.
8. Replace the access path with a documented, least-privilege and recoverable mechanism.

Deleting the only known copy is not a substitute for revocation when the corresponding system may still trust the secret.

## Personal data

Unnecessary personal data in a public or broadly shared location should be reported privately. Include the path and data category, but do not repeat the personal information in the report.

Containment should balance prompt removal, legal obligations, historical preservation and the risk of spreading the information further.

## Supported scope

Security support focuses on:

- the current default branch;
- active projects under `projects/`;
- repository configuration and contribution workflows;
- secrets or personal data exposed by legacy areas.

Legacy prototypes may be unsupported as software, but reports about exposed credentials, unsafe defaults or personal data remain relevant.

## Safe testing

Do not access data that is not yours, degrade services, persist access, use social engineering or test against third-party systems without authorization. Prefer local, synthetic and non-sensitive test data.

## Public follow-up

After containment, a sanitized issue, advisory or decision record may document the root cause, impact, remediation and prevention steps. It must not include live credentials, unnecessary personal data or instructions that materially increase current risk.
