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

This project demonstrates **real-world Git collaboration workflows** using a **Flask To-Do Application**.  
It includes branching, merging, rebasing, and conflict resolution — simulating how developers collaborate efficiently.

### 🎯 Topics Covered
- 🌿 Creating and managing Git branches  
- 💾 Committing code updates  
- 🔀 Merging feature branches  
- ⚔️ Resolving merge conflicts  
- 🔄 Rebasing workflow  
- ☁️ Pushing branches to GitHub  
- 🧹 Deleting merged branches  

---


---

## ⚙️ Git Workflow Demonstration (with Visuals)

### 🪜 Step 1 — Initialize Repository and Push to GitHub
> Initialize local Git repo, rename branch to `main`, add remote, and push.
![Initialize Git Repository and Push to GitHub](./images/Screenshot%202025-12-11%20000701.png)

---

### 🧩 Step 2 — Create `.gitignore` File
> Added `.gitignore` to ignore cache, database, and virtual environment files.
![Gitignore Setup](./images/Screenshot%202025-12-11%20000600.png)

---

### 🌿 Step 3 — Create `dev` Branch and Commit Flask Files
> Created a new branch `dev`, added files, and committed Flask setup.
![Dev Branch Created and Committed](./images/Screenshot%202025-12-11%20000822.png)

---

### 🌿 Step 4 — Merge `dev` into `main`
> Merged the development branch into the main production branch.
![Merge dev into main](./images/Screenshot%202025-12-11%20001101.png)

---

### 🌱 Step 5 — Create `apis` Branch and Add JSON File
> Created `apis` branch, added `todos.json`, committed, merged to `main`.
![APIs Branch Work](./images/Screenshot%202025-12-11%20001411.png)

---

### 🌳 Step 6 — Create `master_1` and `master_2` Branches
> Created `master_1` and `master_2` branches from `main` for parallel feature development.
![Create master_1 and master_2 Branches](./images/Screenshot%202025-12-11%20001528.png)

---

### 💻 Step 7 — Push `master_1` Branch to GitHub
> Added feature branch `master_1` to GitHub remote.
![Push master_1 to GitHub](./images/Screenshot%202025-12-11%20001727.png)

---

### 🧠 Step 8 — Modify `todo.html` in `master_1` (Added Form Fields)
> Added `Item ID`, `UUID`, and `Hash` input fields in HTML.
![Edit todo.html Form Fields](./images/Screenshot%202025-12-11%20002441.png)

---

### 🔄 Step 9 — Rebase `master_1` onto `main`
> Updated `master_1` branch with the latest commits from `main`.
![Rebase master_1 on main](./images/Screenshot%202025-12-11%20002516.png)

---

### 💾 Step 10 — Merge `master_1` Back into `main`
> Successfully merged enhanced form fields from `master_1` into `main`.
![Merge master_1 into main](./images/Screenshot%202025-12-11%20002100.png)

---

### 🔧 Step 11 — Edit `api/routes.py` in `master_2` (Backend Update)
> Updated Flask route `/submittodoitem` to insert data into MongoDB.
![API Route Updated](./images/Screenshot%202025-12-11%20002929.png)

---

### 🔁 Step 12 — Merge `master_2` into `main` and Push Changes
> Integrated backend updates with the latest main branch.
![Merge master_2 into main](./images/Screenshot%202025-12-11%20003133.png)

---

### ⚔️ Step 13 — Resolve Merge Conflicts (main vs master_1)
> Fixed conflicts during merging, committed resolution.
![Resolve Merge Conflicts](./images/merge_master1_branch_conflicsts_to_main_branch.png)

---

### 🌲 Step 14 — Merge Visualization and Cleanup
> Deleted local and remote `master_1` and `master_2` branches after merging.
![Git Graph and Cleanup](./images/master_1and2_merge_to_main_branch.png)

---

### 🧩 Step 15 — Final Branch Overview
> Complete Git graph of all branches and merges.
![Git Branch Overview](./images/1master_branch.png)

---

## 🧠 Git Commands Summary

| Action | Command |
|--------|----------|
| Create Branch | `git checkout -b branch-name` |
| Switch Branch | `git checkout branch-name` |
| Merge Branch | `git merge branch-name` |
| Rebase Branch | `git rebase branch-name` |
| Push Branch | `git push origin branch-name` |
| Delete Local Branch | `git branch -d branch-name` |
| Delete Remote Branch | `git push origin --delete branch-name` |
| Show Graph | `git log --oneline --graph --decorate --all` |

---

## 💡 Learning Outcomes

By completing this workflow, you’ll understand:
- ✅ Creating & switching branches  
- ✅ Merging feature branches  
- ✅ Rebasing cleanly  
- ✅ Handling merge conflicts  
- ✅ Using Git logs for visualization  
- ✅ Cleaning up branches safely  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| 🐍 Backend | Flask (Python) |
| 💾 Database | SQLite / JSON |
| 🧱 Frontend | HTML, CSS |
| ⚙️ Version Control | Git & GitHub |
| 💻 Environment | Ubuntu + VS Code |

---

## 📜 License

This project is open source under the **MIT License**.

---

<p align="center">
  ⭐ <b>If you found this project helpful, please star the repository!</b> ⭐  
  <br>
  <sub>Built with ❤️ by <a href="https://github.com/ankurchouhan">Ankur Chouhan</a> • 2025</sub>
</p>


