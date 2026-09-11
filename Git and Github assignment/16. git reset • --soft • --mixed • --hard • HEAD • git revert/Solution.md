## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Submit:**
- Screenshot of `git log --oneline` **before** reset
- Screenshot of `git log --oneline` and `git status` **after** reset
- Repository link

---
**Answer**

<img width="566" height="126" alt="Screenshot 2026-09-10 171451" src="https://github.com/user-attachments/assets/82b94e04-0406-488e-8b34-63361a1046f4" />
<img width="595" height="102" alt="Screenshot 2026-09-10 171621" src="https://github.com/user-attachments/assets/a1e617cf-be74-4895-a558-f68a4873eab5" />
<img width="687" height="285" alt="Screenshot 2026-09-10 171712" src="https://github.com/user-attachments/assets/ec7908f8-2eec-4ffd-8459-20426515ce2d" />

- Repository link--- https://github.com/Hari46-om/CG_practice

## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```

3. write the short answers in your own words in your notebook:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?

**Submit:**
- Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)
- Photos of written answers.
- Repository link

---

**Answer**


<img width="558" height="287" alt="Screenshot 2026-09-11 175029" src="https://github.com/user-attachments/assets/ec2cb1c1-c215-4e92-8f9c-b7f455a36cc3" />
<img width="726" height="331" alt="Screenshot 2026-09-11 175329" src="https://github.com/user-attachments/assets/37be67f2-f16c-438e-9670-6158c5da44cf" />
<img width="602" height="342" alt="Screenshot 2026-09-11 192327" src="https://github.com/user-attachments/assets/a52d7c2a-a193-495f-9360-949b382e7ac0" />
<img width="1051" height="1280" alt="image" src="https://github.com/user-attachments/assets/450a4329-b00f-4077-bf70-b6485347edd8" />

- Repository link--https://github.com/Hari46-om/CG_practice

## Assignment 3 – Practice git revert (Medium)

**Goal:** Safely undo a commit using `git revert` instead of reset.

1. Make sure you have at least 2–3 commits on `main`.
2. Choose the latest commit and revert it:
   ```bash
   git revert HEAD
   ```
   (Save the commit message that Git opens)
3. Run:
   ```bash
   git log --oneline
   ```
4. Observe that a **new commit** was created (the history was not deleted).
5. write the short answers in your own words in your notebook:
   - What does `git revert` do?
   - How is it different from `git reset`?
   - When is `git revert` safer than `git reset`?

**Submit:**
- Screenshot of `git log --oneline` showing the revert commit
- Photos of written answers.
- Repository link

---

**Answer**

<img width="601" height="227" alt="Screenshot 2026-09-11 222828" src="https://github.com/user-attachments/assets/6949013f-116e-4668-a5b9-d5674957672e" />
<img width="1152" height="1116" alt="image" src="https://github.com/user-attachments/assets/3706aa73-577c-40fd-bb78-33aa8d8196ef" />

- Repository link--https://github.com/Hari46-om/CG_practice

## Assignment 4 – Combined Practice + Safety Rules (Hard)

**Goal:** Combine reset and revert knowledge and demonstrate safe practices.

1. Create a small project flow:
   - Make 3 commits on a file called `project.txt`.
2. Use `git reset --soft HEAD~1` and then create a new improved commit.
3. Later, use `git revert` on one commit and show that history is preserved.
4. Write short answers in your notebook:
   - When should you use `git reset --soft`?
   - When should you use `git reset --hard`? (and why be careful)
   - When should you prefer `git revert`?
   - What do `HEAD`, `HEAD~1`, and `HEAD~2` mean?

**Submit:**
- Screenshot of final `git log --oneline`
- Photos of written answers.
- Repository link

---

## Submission Checklist

| # | Item | Required? |
|---|------|-----------|
| 1 | Assignment 1 – before/after reset screenshots | Yes |
| 2 | Assignment 2 – three reset mode screenshots + written answer photos | Yes |
| 3 | Assignment 3 – revert screenshot + written answer photos | Yes |
| 4 | Assignment 4 – final log + written answer photos | Yes |
| — | GitHub repository link | Yes |

**Important Notes:**
- Be very careful with `git reset --hard` — it can delete your work.
- Prefer `git revert` when commits are already pushed to GitHub.
- Always check `git log --oneline` and `git status` before and after these commands.
