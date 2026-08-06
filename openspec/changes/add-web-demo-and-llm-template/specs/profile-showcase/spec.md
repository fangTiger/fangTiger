## ADDED Requirements

### Requirement: 展示新增前端与模板入口
Profile README SHALL present the frontend website, `web_demo` project, and large model template as discoverable showcase entries alongside the existing AI x Web3 project identity.

#### Scenario: README contains new showcase entries
- **WHEN** a visitor opens the profile README
- **THEN** the README includes visible text for the frontend website, `web_demo`, and the large model template

#### Scenario: README contains stable entry links
- **WHEN** the README is rendered
- **THEN** the frontend website, `web_demo`, and large model template entries expose stable links or anchors that a visitor can follow

### Requirement: 展示资产保持静态可访问
Profile README SHALL use local SVG assets for new visual cards, and each new asset MUST be accessible, described, and free of scripts, foreign objects, or remote resources.

#### Scenario: New showcase cards use local SVG assets
- **WHEN** tests inspect README asset references
- **THEN** the `web_demo` and large model template card references resolve to local files under `assets/`

#### Scenario: New SVG assets remain safe for GitHub rendering
- **WHEN** tests parse the new SVG card assets
- **THEN** each asset has a `viewBox`, `title`, and `desc`, and contains no `script`, `foreignObject`, or remote `href` or `src` reference
