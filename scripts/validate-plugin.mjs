#!/usr/bin/env node
// Validates this repo as a single root-level Devin plugin.
// Run: node scripts/validate-plugin.mjs

import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];
const kebab = /^[a-z0-9]+(-[a-z0-9]+)*$/;
const fail = (msg) => errors.push(msg);
const rel = (p) => p.slice(root.length + 1);

function frontmatter(path) {
  const m = readFileSync(path, "utf8").match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!m) return null;
  const fields = {};
  for (const line of m[1].split(/\r?\n/)) {
    const idx = line.indexOf(":");
    if (idx > 0) fields[line.slice(0, idx).trim()] = line.slice(idx + 1).trim();
  }
  return fields;
}

function checkFrontmatter(md, expectedName) {
  const fm = frontmatter(md);
  if (!fm) return fail(`${rel(md)}: missing YAML frontmatter`);
  if (!fm.name) fail(`${rel(md)}: frontmatter missing "name"`);
  if (!fm.description) fail(`${rel(md)}: frontmatter missing "description"`);
  if (fm.name && fm.name !== expectedName)
    fail(`${rel(md)}: frontmatter name "${fm.name}" should match "${expectedName}"`);
}

// Manifest
const manifestPath = join(root, ".devin-plugin", "plugin.json");
if (!existsSync(manifestPath)) fail("missing .devin-plugin/plugin.json");
else {
  let manifest = null;
  try {
    manifest = JSON.parse(readFileSync(manifestPath, "utf8"));
  } catch (e) {
    fail(`.devin-plugin/plugin.json: invalid JSON (${e.message})`);
  }
  if (manifest) {
    if (!manifest.name) fail("manifest missing \"name\"");
    else if (!kebab.test(manifest.name)) fail(`manifest name "${manifest.name}" must be kebab-case`);
    if (manifest.version && !/^\d+\.\d+\.\d+([-+].*)?$/.test(manifest.version))
      fail(`manifest version "${manifest.version}" is not semver`);
    for (const list of ["requiredPlugins", "optionalPlugins", "forbiddenPlugins"])
      if (manifest[list] !== undefined && !Array.isArray(manifest[list]))
        fail(`manifest "${list}" must be an array`);
  }
}

// Skills: skills/<name>/SKILL.md
const skillsDir = join(root, "skills");
const skillFiles = [];
if (!existsSync(skillsDir)) fail("missing skills/ directory");
else {
  for (const entry of readdirSync(skillsDir)) {
    const dir = join(skillsDir, entry);
    if (!statSync(dir).isDirectory()) continue;
    const md = join(dir, "SKILL.md");
    if (!existsSync(md)) {
      fail(`skills/${entry}: missing SKILL.md`);
      continue;
    }
    skillFiles.push(md);
    checkFrontmatter(md, entry);
  }
  if (skillFiles.length === 0) fail("no skills found under skills/");
}

// Agents: agents/<name>.md or agents/<name>/AGENT.md
const agentsDir = join(root, "agents");
if (existsSync(agentsDir)) {
  for (const entry of readdirSync(agentsDir)) {
    const p = join(agentsDir, entry);
    if (statSync(p).isDirectory()) {
      const md = join(p, "AGENT.md");
      if (!existsSync(md)) fail(`agents/${entry}: missing AGENT.md`);
      else checkFrontmatter(md, entry);
    } else if (entry.endsWith(".md")) {
      checkFrontmatter(p, entry.slice(0, -3));
    }
  }
}

// Every concrete {ai-eng-os}/... reference must point at a real file or folder.
const refPattern = /\{ai-eng-os\}\/([A-Za-z0-9_./*\[\]-]+)/g;
const docs = [
  ...skillFiles,
  join(root, "AGENTS.md"),
  join(root, "CLAUDE.md"),
  join(root, "README.md"),
].filter(existsSync);
for (const file of docs) {
  const text = readFileSync(file, "utf8");
  for (const m of text.matchAll(refPattern)) {
    const target = m[1].replace(/[.,;:)]+$/, "");
    if (/[*\[\]]/.test(target)) continue; // glob or placeholder
    if (!existsSync(join(root, target))) fail(`${rel(file)}: {ai-eng-os}/${target} does not exist`);
  }
}

if (errors.length) {
  console.error(`Plugin validation failed with ${errors.length} error(s):`);
  for (const e of errors) console.error(`  - ${e}`);
  process.exit(1);
}
console.log(`Plugin validation passed: ${skillFiles.length} skills.`);
