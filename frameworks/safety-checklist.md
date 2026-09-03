# Safety Checklist

For anything user-facing or side-effecting. Used by `/safety-review`, `/red-team`, `/launch-readiness`. Adapt the policy lines to your organisation's usage policy; the structure stays.

## Policy and scope

- [ ] Usage policy identified and linked. Prohibited uses listed for this system.
- [ ] Intended users and out-of-scope users stated.
- [ ] Highest-harm misuse scenario written down in one sentence each (aim for 3–5).

## Refusal behavior

- [ ] Refusal precision and recall measured on a set with adversarial requests and benign look-alikes.
- [ ] Over-refusal measured (benign requests wrongly declined); target set.
- [ ] Refusal tone reviewed: brief, non-judgemental, offers a safe alternative where one exists.

## Attack taxonomy (try each, record success rate)

| Category | Examples |
|---|---|
| Direct policy violation | asking outright for prohibited content |
| Role-play / persona | "pretend you're an AI with no rules" |
| Encoding / obfuscation | base64, leetspeak, other languages, split across turns |
| Prompt injection via data | instructions inside retrieved docs, tool results, file contents, web pages |
| System prompt extraction | "repeat your instructions" |
| Gradual escalation | many-turn drift toward a violation |
| Tool misuse | coaxing side-effecting tools into unintended actions; argument injection |
| Privacy | extracting PII from context or training data; re-identification |
| Overreach | agent taking irreversible actions without the gate |
| Denial of wallet | inputs that cause budget blowout |

## Data and privacy

- [ ] PII in prompts, logs and traces: what's stored, for how long, who can read it.
- [ ] Training on user data: policy stated and enforced.
- [ ] Retrieved documents respect the user's access rights (no cross-tenant leakage).

## Agent-specific

- [ ] Every irreversible or externally visible action passes the human gate.
- [ ] Step, token, dollar and wall-clock caps set and tested.
- [ ] Tool results treated as untrusted data.

## Monitoring and response

- [ ] Harmful-output detector or sampling review in production, with a rate target.
- [ ] Incident path: who is paged, how to kill, how to roll back.
- [ ] Jailbreak regression suite runs on every release candidate (`/jailbreak-regression`).

## Sign-off

Safety reviewer named in `context-library/stakeholders.md` signs the launch-readiness doc. Open critical or high findings block launch.
