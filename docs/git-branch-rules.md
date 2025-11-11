# 🚀 Git Branching Rules (Short & Simple)

## ✅ When is a new branch worth it?
- Changes take more than 30–60 minutes  
- More than 3 commits  
- Risk of breaking `main`  
- New feature / logical block  
- Large refactorings

Tiny 1‑line fixes can go directly on `main`.

---

## ✅ Which branches?

```
main                → stable, release-ready
dev (optional)      → integration branch for multiple features
feature/<name>      → new features
fix/<bug>           → minor bugfixes
hotfix/<critical>   → urgent fixes directly from main
docs/<topic>        → documentation changes
refactor/<topic>    → code restructuring
```

Rules:
- always lowercase  
- no spaces  
- short and clear names  

---

## ✅ Feature Branch Workflow

1. Create branch  
```bash
git checkout -b feature/<name> main
```

2. Work + commit small changes  
3. Rebase before pushing  
```bash
git fetch origin
git rebase origin/main
```

4. Push + open Pull Request  
```bash
git push -u origin feature/<name>
```

5. Squash merge into `main`  
6. Delete branch  

```bash
git branch -d feature/<name>
git push origin --delete feature/<name>
```

---

## ✅ Hotfix (urgent)

```bash
git checkout -b hotfix/<name> main
# fix + commit
git push -u origin hotfix/<name>
```

Merge → create tag:
```bash
git tag -a v0.1.1 -m "Hotfix"
git push --tags
```

---

## ✅ Commit Messages (short & clear)

```
<type>(scope): message
```

Types:
- feat  
- fix  
- refactor  
- docs  
- test  
- chore  

Examples:

```
type(scope): description

BRANCH:
feature/jsonl-support

COMMITS
feature(jsonl): add support for reading jsonl files
fix(jsonl): handle empty lines correctly
refactor(jsonl): split parser into smaller functions
```

---

## ✅ Pull Request Title & Description

### Title (short, start with a verb)
- Add output directory support  
- Fix crash on missing input  
- Refactor path handling  

### Description
```
### What
- What was done?

### Why
- Why was it needed?

### How
- How was it solved?
```

SHORT. CLEAN. STRAIGHT TO THE POINT.

---

# ✅ Info about the ZIP file (simple)

- The ZIP contains your **current project state**  
- Everything inside is **Work in Progress**  
- Push content **piece by piece** into feature branches  
- Merge only finished parts into `main`  
- Each push will look clean & professional  
- The ZIP is only your local **starting package** → **don’t dump it directly on main**

Recommended workflow:

```bash
unzip learn-configura.zip
cd learn-configura

# create your first branch
git checkout -b feature/initial-setup

# add files, commit, push
git push -u origin feature/initial-setup

# then PR → squash → main
```

This way it looks like you’re building the project **calmly, consistently, and professionally** — no messy history.

---

## ✅ TL;DR
- Create a branch whenever change is big enough  
- `main` holds only stable, finished work  
- squash merge → clean history  
- ZIP → base, but push step-by-step  
- PRs → What / Why / How