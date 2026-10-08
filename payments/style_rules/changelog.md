---
name: changelog
description: |
  A skill for creating and improving changelog entries.
  It can write new changelogs from scratch or refine existing ones by organizing changes, improving clarity, following best practices, and ensuring consistency with semantic versioning.
---

# Changelog Skill

## Overview
This skill helps create and improve professional changelogs that clearly communicate release updates. It transforms raw commit messages, rough notes, or draft changelogs into well-structured, user-friendly documentation following semantic versioning and changelog best practices.

## Capabilities
- **Structure Organization**: Organize changes into standard categories (Added, Changed, Deprecated, Removed, Fixed, Security) following Keep a Changelog conventions.
- **User-Friendly Language**: Rewrite technical commit messages and jargon into clear descriptions focused on user impact.
- **Consistency**: Ensure consistent formatting, tone, action verbs, and style throughout all entries.
- **Semantic Versioning Alignment**: Verify changelog reflects semantic versioning principles (MAJOR.MINOR.PATCH). Breaking changes warrant MAJOR version bumps.
- **Breaking Change Clarity**: Clearly highlight breaking changes with migration guidance and upgrade paths.
- **Impact Communication**: Help users understand what changes affect them (performance, security, functionality, dependencies).
- **Grouping & Prioritization**: Group related changes logically. Prioritize important changes (security fixes, breaking changes) appropriately.
- **Markdown Formatting**: Output clean, well-formatted Markdown with proper heading hierarchy and consistent styling.
- **Version Dating**: Include version release dates in ISO format (YYYY-MM-DD) for clarity.

## Usage
Provide commit messages, release notes, PRDs, or existing changelog content. The skill will transform it into a professional changelog following best practices. You can specify target format, release date, and any special focus areas.

## Well-Written Examples

While the repositories don't contain traditional changelog files, they demonstrate excellent practices for documenting changes:

### Key Best Practices Found in Existing Documentation

1. **Security-Focused Communication** - `/developer-site-waas2/v2/guides/mpc-wallets/server-co-signer/`
   - ✅ Breaking changes clearly marked and explained
   - ✅ Migration guidance provided for each change
   - ✅ Security implications highlighted
   - ✅ Numbered, structured format for clarity

2. **Feature Explanation with Context** - `/payments-manual/payments/en/guides/`
   - ✅ Features introduced with "what" and "why"
   - ✅ Related operations/endpoints always linked
   - ✅ User benefits emphasized, not implementation details
   - ✅ Breaking changes explicitly documented in prerequisites sections

3. **Version-Specific Documentation** - `/developer-site-waas2/v2/guides/overview/changelog.mdx`
   - ✅ Version markers in documentation
   - ✅ Migration guides between versions
   - ✅ Deprecation notices with clear timelines
   - ✅ SDK version requirements documented

### Good Documentation Practices to Apply to Changelogs:

- **Use clear action verbs** - "Added", "Fixed", "Removed", "Improved" (see /v2 guides examples)
- **Link to related documentation** - Like guides do with cross-references
- **Organize by feature category** - Not by implementation (see Payments Manual guide organization)
- **Mark breaking changes clearly** - With explicit notices (see /v2 server-co-signer guides for security/breaking change patterns)
- **Provide migration paths** - Link to migration guides or alternative approaches
- **Include version numbers** - Always specify SDK or API version (SDK v1.30.0 format)

### Example Interactions

**Input**: A list of commit messages:
```
- Fixed wallet creation bug when user has no permissions
- Added batch export feature
- Improved API response times by 40%
- Removed deprecated OAuth flow
- Updated SDK dependencies
```
**Output**:
```markdown
## [1.2.0] - 2024-01-15

### Added
- Batch export feature for large transaction datasets

### Changed
- Improved API response times by 40% through database optimization

### Fixed
- Wallet creation now properly validates user permissions before creating wallet

### Removed
- Deprecated OAuth 1.0 flow (migrate to OAuth 2.0 by 2024-03-01)

### Security
- Updated SDK dependencies to address potential vulnerabilities
```

**Input**: "Our v2.0 is a complete rewrite with a new API structure"
**Output**:
```markdown
## [2.0.0] - 2024-01-20 - BREAKING CHANGES

This is a major release with significant breaking changes. **Please review the migration guide before upgrading.**

### Changed
- **BREAKING**: API endpoint structure changed from `/api/v1/wallets` to `/wallets/v2`
- **BREAKING**: Response format changed from XML to JSON
- **BREAKING**: Authentication method changed from Basic Auth to Bearer tokens (see [migration guide](/guides/auth-v2))
- Improved error messages with detailed troubleshooting information
- Enhanced webhook payloads with additional context

### Added
- New WebSocket API for real-time updates
- Batch operations support for improved performance
- Advanced filtering and sorting on list endpoints

### Removed
- XML response format (use JSON instead)
- Basic authentication (use Bearer tokens or OAuth 2.0)
```

## Quality Criteria

A high-quality changelog entry should have:

1. **Clear Category**: Entry belongs in exactly one logical category (Added, Changed, Fixed, etc.)
2. **Action Verb**: Starts with past tense verb (Added, Fixed, Changed, Improved, Removed, etc.)
3. **User Impact**: Describes what users need to know or do, not implementation details
   - ✅ "Added batch export for large datasets"
   - ❌ "Updated export function to handle arrays"
4. **Specificity**: Enough detail that users understand the change
   - ✅ "Fixed wallet creation failing when user lacks admin permissions"
   - ❌ "Fixed wallet bug"
5. **No Jargon**: Avoids overly technical terms or links to internal systems
6. **Completeness**: Important context included (affected features, workarounds, related links)
7. **Consistency**: Matches style of other entries (tense, verb form, detail level)
8. **Breaking Change Clarity**: Explicitly marked with "BREAKING:" prefix if upgrade path needed

## Guidelines

**All changelog entries must follow Cobo's standard terminology and language rules.**

Refer to the **Reference Materials** skill for:
- [General Writing Rules](../reference-materials/SKILL.md#general-writing-rules) (spelling, grammar, formatting)
- [Standard Terminology & Glossary](../reference-materials/SKILL.md#standard-terminology--glossary) (product names, payment terminology)
- [Word Choice Rules](../reference-materials/SKILL.md#word-choice-rules) (specific words and usage)
- [Quick Reference for transformations](../reference-materials/SKILL.md#quick-reference-common-transformations) (internal → user-facing language)

### Core Guidelines

- **User-Centric**: What do end-users and developers need to know? Focus on impact, not implementation.
- **Action Verbs**: Use past tense, clear verbs
  - ✅ Added, Changed, Improved, Fixed, Removed, Deprecated, Updated, Enhanced, Resolved
  - ❌ "Did", "Made", "Worked on", "Tweaked"
- **Clarity Over Completeness**: Be concise but specific. Each entry should stand alone and be understandable.
- **Breaking Changes**:
  - Always prefix with "BREAKING:" or include in a dedicated section
  - Include migration path or link to migration guide
  - Use version heading to make it obvious (e.g., "## [2.0.0] - MAJOR RELEASE")
- **No Technical Jargon**: Avoid: "Refactored authentication module" → Use: "Improved authentication response times"
- **Consistency Rules**:
  - Use past tense consistently (Fixed, not Fix)
  - Use parallel structure: "Added X, Changed Y, Removed Z" (not "Added X, Y is removed")
  - Apply consistent detail level across similar changes
  - Use American spelling, no contractions
- **Terminology**: Use standard Cobo terminology (see Reference Materials)
  - "Payment collection" (not "deposits")
  - "Payouts" (not "withdrawals")
  - "Compliance screening" (not "security check")
- **Grouped by Category**: Organize strictly by category type:
  - **Added**: New features, endpoints, fields
  - **Changed**: Modifications to existing functionality, improvements, enhancements
  - **Deprecated**: Features marked for future removal with timeline
  - **Removed**: Features or code that are gone (especially after deprecation period)
  - **Fixed**: Bug fixes
  - **Security**: Security improvements, vulnerability fixes, CVE patches
- **Chronological Within Category**: List changes newest to oldest within each category (optional if only one release)
- **Version Format**: Use semantic versioning: MAJOR.MINOR.PATCH[-prerelease][+build]
  - 1.0.0 (first release), 1.1.0 (feature), 1.0.1 (bug fix), 2.0.0 (breaking changes)
- **Date Format**: Always use ISO format: YYYY-MM-DD
- **Link References**: Include links where helpful
  - Link to migration guides for breaking changes
  - Link to related issue/PR numbers where helpful
  - Use descriptive link text
- **Deprecated Items**: When marking something as deprecated, include:
  - What is being deprecated
  - Why (if not obvious)
  - What to use instead
  - Timeline for removal (if known)
  - Link to migration guide

## Common Changelog Categories

- **Added**: New features, endpoints, parameters, integrations
- **Changed**: Improvements, enhancements, modifications to existing functionality
- **Deprecated**: Features marked for future removal with deprecation timeline
- **Removed**: Features, endpoints, or code that is no longer available
- **Fixed**: Bug fixes and corrections
- **Security**: Security vulnerabilities, patches, improvements

## 11. COBO-SPECIFIC PATTERNS

### Organizing by Feature Category (Not Implementation)

**CRITICAL:** Organize changelog by user-visible features, NOT by implementation details.

✅ **Feature Categories**:
- 收款 (Payment collection)
- 资金转出 (Payouts)
- Webhook 事件 (Webhook events)
- 资金管理 (Fund management)
- 支付链接 (Payment links)
- 合规筛查 (Compliance screening)
- SDK & Tools

❌ **Implementation Details (Remove)**:
- "App端/API端" (App vs API - combine into feature)
- "状态机调整" (State machine refactoring)
- "重构新接口" (Interface refactoring)
- "上线相关交付物" (Delivery artifacts)
- Internal refactoring or optimization details

### Example: Cobo Payments Changelog Format

```markdown
| 功能类别 | 变更说明 | 发布时间 |
|------|----------|----------|
| **资金管理** | (SDK v1.30.0) 全新资金转出 API 操作，转出流程更加高效... <br/>&nbsp;&nbsp;- [Create payout](/payments/en/api-references/payment/create-payout)<br/>&nbsp;&nbsp;- [List all payouts](/payments/en/api-references/payment/list-all-payouts) | 2026-01-23 |
| **Webhook 事件** | (SDK v1.30.0) 新增多个 Off-Ramp 对接相关的 [Webhook 事件](/payments/cn/guides/events/overview) | 2026-01-23 |
| **资金管理** | (SDK v1.30.0) 新增 Bulk Send API 操作，支持加密货币批量转账... | 2026-01-23 |
```

### Transformation Examples

**Original (Internal):**
```
- Payout-Crypto Withdraw支持Bridge
- App端/API端支持
- Off-ramp重构新接口及交互界面改造
- 状态机调整
- 支持批量获取payer收币地址
```

**Transformed (User-Facing):**
```
| **资金管理** | (SDK v1.30.0) 全新资金转出 API 操作，现已支持加密货币转账时自动跨链。将分布在不同链上的同一代币一次性转出至一个目标地址。<br/>涉及的 API 操作包括：<br/>&nbsp;&nbsp;- [Create payout](/payments/en/api-references/payment/create-payout)<br/>&nbsp;&nbsp;- [List all payouts](/payments/en/api-references/payment/list-all-payouts) | 2026-01-23 |
| **收款** | (SDK v1.30.0) [Create/Get top-up address](/payments/en/api-references/payment/createget-top-up-address) 操作新增支持批量获取充值地址 | 2026-01-23 |
```

### Key Transformation Principles

1. **Focus on User Benefits**
   - ❌ "重构新接口"
   - ✅ "转出流程更加高效，无需区分资金来源"

2. **Group by Feature, Not Implementation**
   - ❌ App vs API
   - ✅ Combine into one entry about the feature

3. **Include All Affected APIs**
   - List all new/changed operations with links
   - Mark deprecated operations explicitly

4. **Document Breaking Changes Clearly**
   - Use table with "BREAKING:" prefix
   - Include migration guidance
   - Link to migration guides when available

5. **Specify SDK Version**
   - Always include: `(SDK v1.30.0)`
   - Ask if missing: "Which SDK version?"

6. **Remove Internal Deliverables**
   - ❌ "用户引导手册" (user guide)
   - ❌ "developer hub"
   - ✅ Only include user-visible features

### Questions to Ask When Creating Changelogs

- [ ] What is the SDK version? (e.g., v1.30.0)
- [ ] What is the release date? (Format: YYYY-MM-DD)
- [ ] What is the main feature category?
- [ ] What are ALL affected API endpoints? (List with links)
- [ ] Are any features deprecated? (List all with migration path)
- [ ] Are there any breaking changes? (Mark clearly with BREAKING:)
- [ ] What is the user benefit/value proposition?
- [ ] Should this be organized differently (by feature vs category)?

### Handling Missing Information

Don't guess - ask specifically:

```
❓ Which SDK version is required?
- [ ] SDK v1.30.0
- [ ] SDK v1.31.0
- [ ] Multiple versions
- [ ] Not applicable
- [ ] Other: ___________
```

Use placeholders in output when information is unclear:

```markdown
| **资金管理** | (SDK v[VERSION]) [需要确认：功能描述] |  |
```
