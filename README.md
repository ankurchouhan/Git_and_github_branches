<!-- HEADER -->
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git Logo" width="80"/>
</p>

<h1 align="center">🧠 Git & GitHub Branches — Flask To-Do Application</h1>

<p align="center">
  <b>Learn Git branching, merging, rebasing, and conflict resolution using a Flask-based To-Do web app.</b>
</p>

<p align="center">
  👤 Author: <a href="https://github.com/ankurchouhan"><b>Ankur Chouhan</b></a>  
  <br>
  🗂 Repository: <a href="https://github.com/ankurchouhan/Git_and_github_branches">Git_and_github_branches</a>
</p>

---

## 🚀 Project Overview

This project demonstrates **Git workflow mastery** using a **Flask To-Do Application**.  
It shows real-world collaboration techniques — how developers use **branches, merges, rebasing, and conflict resolution** effectively.

### 🎯 Covers:
- 🌿 Creating and managing Git branches  
- 🔀 Merging multiple branches  
- ⚔️ Resolving merge conflicts  
- 🔄 Rebasing for clean commit history  
- ☁️ Pushing changes to GitHub  
- 🧹 Deleting branches locally and remotely  

---

## ⚙️ Git Workflow Demonstration (with Screenshots)

### 🪜 Step 1 — Push Existing Flask Project to New GitHub Repo (main)
![Initial Repository Setup & Push to main](./images/Screenshot%202025-12-11%20000701.png)

---

### 🌿 Step 2 — Create `dev` Branch and Commit Flask Project Files
![Create dev branch and first dev commit](./images/Screenshot%202025-12-11%20000822.png)

---

### 🌿 Step 3 — Merge `dev` into `main` and Prepare for API Work
> Merge `dev` → `main`, then create a new branch for API work.

![Merge dev into main and prepare next branch](./images/Screenshot%202025-12-11%20001101.png)

---

### 🌿 Step 4 — Create `apis`, Commit JSON Data, Merge Back into `main` & Create `master_1` / `master_2`
> Work in `apis` branch, then merge it into `main`. After that, create `master_1` and `master_2` branches for separate features.

![Work with apis branch and create master_1, master_2](./images/Screenshot%202025-12-11%20001411.png)

---

### ☁️ Step 5 — List All Branches and Push `master_1` to GitHub
![Push master_1 branch to GitHub](./images/Screenshot%202025-12-11%20001528.png)

---

### 📝 Step 6 — Edit To-Do Form in `master_1` (HTML Changes)
> Update `templates/todo.html` in `master_1` to add more fields to the To-Do form.

![Editing To-Do HTML form in master_1](./images/Screenshot%202025-12-11%20001727.png)

---

### 🔄 Step 7 — Rebase `master_1` on Top of Latest `main`
> Bring `master_1` up to date with `main` using `git rebase main`.

![Rebasing master_1 onto main](./images/Screenshot%202025-12-11%20002441.png)

---

### 🔀 Step 8 — Commit Enhanced Form in `master_1` and Merge into `main`
> Commit updated form in `master_1`, push it, then merge into `main` and push again.

![Commit enhanced form and merge master_1 into main](./images/Screenshot%202025-12-11%20002516.png)

---

### 💻 Step 9 — Update Backend Route in `master_2` (API Logic)
> Edit `api/routes.py` in `master_2` to enhance the backend `/submittodoitem` route.

![Editing backend routes in master_2](./images/Screenshot%202025-12-11%20002929.png)

---

### 🔀 Step 10 — Merge `master_2` into `main` and Push Final Changes
> Push `master_2`, then merge it into `main` and push to GitHub.

![Merge master_2 into main and push final changes](./images/Screenshot%202025-12-11%20003131.png)

---

## 🔍 Extra Visuals — Git Branch Graphs

### 🌳 Git Graph — Branch Overview
![Git Graph: Branch Overview](./images/1master_branch.png)

### 🌳 Git Graph — `master_1` and `master_2` Merged into `main`
![Git Graph: master_1 and master_2 merge](./images/master_1and2_merge_to_main_branch.png)

### ⚔️ Git Graph — Merge Conflicts While Merging `master_1`
![Git Graph: merge conflict example](./images/merge_master1_branch_conflicsts_to_main_branch.png)

---

## 🧠 Git Commands Summary

| Action | Command |
|--------|----------|
| Create Branch | `git checkout -b branch-name` |
| Switch Branch | `git checkout branch-name` |
| Merge Branch | `git merge branch-name` |
| Rebase Branch | `git rebase branch-name` |
| Delete Local Branch | `git branch -d branch-name` |
| Delete Remote Branch | `git push origin --delete branch-name` |
| View Branches | `git branch -a` |

---

## 🌳 Branch Naming Convention

| Type | Prefix | Example |
|------|--------|---------|
| Main Branch | `main` | `main` |
| Feature Branch | `feature/` | `feature/add-task` |
| Fix Branch | `fix/` | `fix/typo-bug` |
| Docs Branch | `docs/` | `docs/update-readme` |
| Experimental | `exp/` | `exp/test-api` |

---

## 💡 Learning Outcomes

By following this project, you’ll learn:
- ✅ Branch creation & management  
- ✅ Merge conflict resolution  
- ✅ Rebasing workflow  
- ✅ Clean commit practices  
- ✅ Collaborative GitHub flow  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| 🐍 Backend | Flask (Python) |
| 💾 Database | SQLite |
| 💅 Frontend | HTML, CSS |
| ⚙️ Version Control | Git & GitHub |
| 🧩 Editor | VS Code |

---

## 📜 License

This project is open source under the **MIT License**.

---

<p align="center">
  ⭐ <b>If you found this project helpful, please star the repository!</b> ⭐  
  <br>
  <sub>Built with ❤️ by <a href="https://github.com/ankurchouhan">Ankur Chouhan</a> • 2025</sub>
</p>
