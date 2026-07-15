---
name: pr-body
description: Write the body text for a pull/merge request. Use when asked to write a PR body or create a PR.
---

This skill produces the body text for a pull/merge request. It does not specify where the output goes — produce the body text and let the caller decide what to do with it.

## Choosing a template

1. Always look for the repository's own custom PR/MR template first. This is a service-agnostic step: a repo may define a template regardless of which host it uses.
2. Known hard-coded locations to check:
   - **GitHub**: `.github/PULL_REQUEST_TEMPLATE.md`, root `PULL_REQUEST_TEMPLATE.md`, `docs/PULL_REQUEST_TEMPLATE.md` (file names are case-insensitive), and the `.github/PULL_REQUEST_TEMPLATE/` directory, which may hold multiple named templates.
   - **GitLab**: `.gitlab/merge_request_templates/*.md` (may hold multiple named templates).
3. If a custom template is found, use it. Otherwise, use the standard template below.

## Standard template

All sections are optional. Render a section's heading only if there is content for it.

- **Context**: a short summary of why the changes were made. Include issue tracking ticket IDs (e.g. Jira) if available.
  - Only use context already provided during the session, including information already read earlier in the session.
  - Do NOT read, fetch, or infer anything new when writing the context. For example, if a ticket number is available but its contents were not already read, just put the ticket number in — do not go read the ticket.
- **Primary changes**: a bullet point list.
- **Other changes**: a bullet point list.

What counts as a primary versus other change depends on the PR.

## Trailer

Always append the trailer specified in the system instructions at the end of the body, whether a custom or the standard template was used.
