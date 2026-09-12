
## Assignment 1 – Basic Revert Practice

**Goal:** Perform a simple revert and observe the new commit.

1. Create 2–3 commits on any file (for example `index.html` or `notes.txt`).
2. Using `git log --oneline`, note the commit hash of the latest commit.
3. Revert the latest commit:
   ```bash
   git revert HEAD
   ```
   (or use the commit hash)
4. Run `git log --oneline` and observe the new revert commit.

**Submit:**
- Screenshot of `git log --oneline` before revert
- Screenshot of `git log --oneline` after revert
- Repository link

---

**Answer**

<img width="662" height="132" alt="Screenshot 2026-09-12 173904" src="https://github.com/user-attachments/assets/119c8545-9c68-4e26-8477-cd2eb5497b3f" />
<img width="621" height="226" alt="Screenshot 2026-09-12 173851" src="https://github.com/user-attachments/assets/033b97b4-e1ac-4ee2-ac65-733015b23583" />


- Repository link--https://github.com/Hari46-om/CG_practice

## Assignment 2 – Modify/Delete Conflict during Revert

**Goal:** Face and resolve a Modify/Delete conflict while reverting.

1. Create a commit that **adds a new file**.
2. Make one more commit after that.
3. Try to revert the commit that added the file.
4. A Modify/Delete conflict should appear.
5. Resolve it (either delete the file or keep it with required content).
6. Use:
   ```bash
   git add .
   git revert --continue
   ```

**Submit:**
- Screenshot of the conflict (VS Code or terminal)
- Screenshot after successful `git revert --continue`
- Repository link

---

**Answer**

<img width="762" height="522" alt="Screenshot 2026-09-12 182412" src="https://github.com/user-attachments/assets/be730c97-14fe-461c-850d-f981b802dff0" />
<img width="682" height="160" alt="Screenshot 2026-09-12 182708" src="https://github.com/user-attachments/assets/cba3d9c6-fe94-4898-bd0a-50879c0094b5" />


- Repository link--https://github.com/Hari46-om/CG_practice


## Assignment 3 – Revert Options + Conceptual Questions

**Goal:** Practice important flags and understand the concepts.

### Practical Part
1. Demonstrate any two of the following commands with a real commit:
   - `git revert --no-edit <commit_id>`
   - `git revert --no-commit <commit_id>`
   - `git revert --abort`
2. Take screenshots of the commands and their results.

### Theoretical Part (Write in Notebook)
Write short and correct answers for the following:

1. What does `git revert` do?
2. Why is `git revert` safer than `git reset` on a shared branch?
3. What is a Modify/Delete conflict? When can it occur during revert?
4. What is the difference between `git revert --abort` and `git revert --quit`?
5. Write one major difference each between:
   - `git restore`
   - `git reset`
   - `git revert`

**Submit:**
- Screenshots of the two practical commands you tried
- Clear photos of the written answers from your notebook
- Repository link

---
