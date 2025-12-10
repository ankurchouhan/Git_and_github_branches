<!-- HEADER -->
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git Logo" width="80"/>
</p>

<h1 align="center">🧠 Git & GitHub Branches — Flask To-Do Application</h1>

<p align="center">
  <b>Master Git branching, merging, rebasing, and conflict resolution using a Flask-based To-Do web app.</b>
</p>

<p align="center">
  👤 Author: <a href="https://github.com/ankurchouhan"><b>Ankur Chouhan</b></a>  
  <br>
  🗂 Repository: <a href="https://github.com/ankurchouhan/Git_and_github_branches">Git_and_github_branches</a>
</p>

---

## 🚀 Project Overview

This project demonstrates **real-world Git collaboration workflows** using a **Flask To-Do Application**.  
It simulates a professional development setup with **multiple branches**, **merges**, **rebasing**, and **conflict resolution**.

### 🎯 You’ll Learn:
- 🌿 Creating and managing Git branches  
- 🧩 Merging and rebasing branches  
- ⚔️ Resolving merge conflicts  
- ☁️ Pushing code to GitHub  
- 🧹 Cleaning up merged branches  
- 💡 Understanding Git Graphs  

---

## ⚙️ Git Workflow Demonstration (Step-by-Step with Screenshots)

### 🪜 Step 1 — Initialize Repository and Push to GitHub  
> Setup local Git repo, rename branch to `main`, add remote, and push.

![Step 1 — Initialize Git Repository](./images/Screenshot%202025-12-11%20000701.png)

---

### 🧩 Step 2 — Create `.gitignore` File  
> Added `.gitignore` to ignore unwanted files like cache, db, and virtual environment.

![Step 2 — .gitignore Setup](./images/Screenshot%202025-12-11%20000822.png)

---

### 🌿 Step 3 — Create `dev` Branch and Add Flask Files  
> Created `dev` branch, committed Flask project files.

![Step 3 — Create Dev Branch and Commit Files](./images/Screenshot%202025-12-11%20001101.png)

---

### 🌿 Step 4 — Merge `dev` into `main` and Create `apis` Branch  
> Merged `dev` into `main`, then created `apis` for backend JSON updates.

![Step 4 — Merge dev to main and create apis](./images/Screenshot%202025-12-11%20001411.png)

---

### 🌱 Step 5 — Add and Commit JSON File in `apis`  
> Added `data/todos.json` and merged the branch back to `main`.

![Step 5 — Add todos.json in apis branch](./images/Screenshot%202025-12-11%20001528.png)

---

### 🌳 Step 6 — Create `master_1` and `master_2` Feature Branches  
> Created new branches `master_1` and `master_2` for different tasks.

![Step 6 — Create master_1 and master_2 Branches](./images/Screenshot%202025-12-11%20001727.png)

---

### 💻 Step 7 — Modify HTML To-Do Form in `master_1`  
> Enhanced `todo.html` by adding fields: `Item ID`, `UUID`, and `Hash`.

![Step 7 — Edit todo.html in master_1](./images/Screenshot%202025-12-11%20002441.png)

---

### 🔄 Step 8 — Rebase `master_1` onto `main`  
> Updated `master_1` with latest commits from `main` before merging.

![Step 8 — Rebase master_1 with main](./images/Screenshot%202025-12-11%20002516.png)

---

### 🔀 Step 9 — Merge `master_1` Back into `main`  
> Merged updated HTML features from `master_1` into `main`.

![Step 9 — Merge master_1 into main](./images/Screenshot%202025-12-11%20002625.png)

---

### ⚙️ Step 10 — Update Backend in `master_2`  
> Modified Flask route `/submittodoitem` in `api/routes.py` for MongoDB integration.

![Step 10 — Update Backend Route in master_2](./images/Screenshot%202025-12-11%20002940.png)

---

### 🔁 Step 11 — Merge `master_2` into `main`  
> Merged backend updates into the main branch.

![Step 11 — Merge master_2 into main](./images/Screenshot%202025-12-11%20003133.png)

---

### ⚔️ Step 12 — Resolve Merge Conflicts  
> Resolved conflicts while merging multiple branches.

![Step 12 — Resolve Merge Conflicts](./images/merge_master1_branch_conflicsts_to_main_branch.png)

---

### 🌲 Step 13 — View Combined Git Graph  
> Visualized merged branches `master_1` and `master_2` on Git graph.

![Step 13 — Git Graph After Merge](./images/master_1and2_merge_to_main_branch.png)

---

### 🧩 Step 14 — Final Branch Overview  
> The final branch graph after all merges and cleanups.

![Step 14 — Final Branch Overview](./images/1master_branch.png)

---

## 🧠 Git Commands Summary

| Action | Command |
|--------|----------|
| Initialize Repo | `git init` |
| Create Branch | `git checkout -b branch-name` |
| Switch Branch | `git checkout branch-name` |
| Merge Branch | `git merge branch-name` |
| Rebase Branch | `git rebase branch-name` |
| View Branches | `git branch -a` |
| Push to GitHub | `git push origin branch-name` |
| Delete Local Branch | `git branch -d branch-name` |
| Delete Remote Branch | `git push origin --delete branch-name` |
| Visualize Commits | `git log --oneline --graph --decorate --all` |

---

## 🌳 Branch Naming Convention

| Type | Prefix | Example |
|------|---------|----------|
| Main Branch | `main` | `main` |
| Development Branch | `dev` | `dev` |
| API Branch | `apis` | `apis` |
| Feature Branch | `master_1` | `master_1` |
| Secondary Feature | `master_2` | `master_2` |

---

## 💡 Learning Outcomes

By completing this project, you’ll master:
- ✅ Branch creation & version isolation  
- ✅ Rebasing for a clean commit history  
- ✅ Handling and resolving merge conflicts  
- ✅ Managing multiple branches effectively  
- ✅ Cleaning up old branches  
- ✅ Visualizing Git structure  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| 🐍 Backend | Flask (Python) |
| 💾 Database | JSON / SQLite |
| 💅 Frontend | HTML, CSS |
| ⚙️ Version Control | Git & GitHub |
| 💻 Environment | Ubuntu + VS Code |

---

## 🏁 Final Output

### ✅ Flask To-Do App and Final Git Structure
![Final Flask App Git View](./images/Screenshot%202025-12-11%20001727.png)

---

## 📜 License

This project is open source under the **MIT License**.

---

<p align="center">
  ⭐ <b>If you found this project helpful, please star the repository!</b> ⭐  
  <br>
  <sub>Built with ❤️ by <a href="https://github.com/ankurchouhan">Ankur Chouhan</a> • 2025</sub>
</p>
