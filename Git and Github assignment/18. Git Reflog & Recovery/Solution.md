***

## 📋 Part 1: Recovery After `git reset --hard` (5 Points)

### Task
1. Create a new repository called `reflog-practice-part1`
2. Create 3 commits:
   - **C0:** `README.md` with project title
   - **C1:** `index.html` with `<h1>Welcome</h1>`
   - **C2:** `style.css` with basic styling
3. Accidentally delete C1 and C2 using `git reset --hard <C0-commit-hash>`
4. Use `git reflog` to find the lost C2 commit
5. Recover C2 (and C1) using detached HEAD + branch + merge
6. Verify all commits are restored

### Deliverables
```
✅ Screenshot of: git log --oneline BEFORE reset
✅ Screenshot of: git log --oneline AFTER reset (showing lost commits)
✅ Screenshot of: git reflog output (highlighting the commit you recovered)
✅ Screenshot of: git log --oneline AFTER recovery (showing all commits restored)
✅ Push final repository to GitHub
```

### Expected Output
```bash
# Initial state
C0 ────── C1 ────── C2 (main)

# After reset --hard
C0 (main)    [C1 & C2 lost from log]

# After recovery
C0 ────── C1 ────── C2 (main)  ← All restored!
```

***

**Answer**

<img width="755" height="115" alt="Screenshot 2026-09-15 195348" src="https://github.com/user-attachments/assets/1b86c8fe-8a31-408e-997f-0c992196e36c" />
<img width="865" height="76" alt="Screenshot 2026-09-15 195412" src="https://github.com/user-attachments/assets/983326d9-dd5f-4ea0-af6d-f5460553e8f5" />
<img width="1135" height="231" alt="Screenshot 2026-09-15 195758" src="https://github.com/user-attachments/assets/569cfecc-a3d4-46b8-9257-4d1fc78fd672" />
<img width="760" height="122" alt="Screenshot 2026-09-15 195835" src="https://github.com/user-attachments/assets/de66a2bc-1615-4fa2-b37b-c47f30fbb8ba" />

-Repository link --http://github.com/Hari46-om/CG_practice/tree/main/reflog-practice-part1

## 📋 Part 2: Reworking Old Commit (5 Points)

### Task
1. Create a new repository called `reflog-practice-part2`
2. Create 3 commits:
   - **C0:** `README.md` with just title
   - **C1:** `app.js` with basic function
   - **C2:** `utils.js` with helper functions
3. Realize you need to add description to README (C0) without losing C1 and C2
4. Create a branch at C0: `git switch -c rework/readme-update <C0-hash>`
5. Update README.md with description, commit
6. Merge the branch back to main
7. Verify C0, C1, and C2 are all preserved

### Deliverables
```
✅ Screenshot of: git log --oneline BEFORE creating branch
✅ Screenshot of: git branch output (showing both branches)
✅ Screenshot of: git log --oneline --graph (showing merge)
✅ Screenshot of: Final README.md content
✅ Push final repository to GitHub
```

### Expected Output
```bash
# Before rework
C0 ────── C1 ────── C2 (main)

# After rework + merge
      C3 (README update) ─┐
                          │
C0 ────── C1 ────── C2 ─── Merge (main)

All commits preserved!
```

***
---
**Answer**

<img width="780" height="127" alt="Screenshot 2026-09-18 203032" src="https://github.com/user-attachments/assets/6522e907-b6a2-48e3-80f2-3acb8c750e0e" />
<img width="906" height="368" alt="Screenshot 2026-09-18 203223" src="https://github.com/user-attachments/assets/cde6ddcb-2c17-49f2-96ab-586443ee8ec5" />
<img width="820" height="201" alt="Screenshot 2026-09-18 203613" src="https://github.com/user-attachments/assets/c9486e70-62c7-46f1-b8df-02a650a6af25" />
<img width="720" height="112" alt="Screenshot 2026-09-18 203701" src="https://github.com/user-attachments/assets/bf4fe7d5-7988-429a-af3f-c3fb2268a22f" />

-repository--https://github.com/Hari46-om/CG_practice/tree/main/reflog-practice-part2




## 📋 Part 3: Reflog Exploration 

### Task
1. In either repository, run `git reflog`
2. Document at least 5 different HEAD movements
3. For each movement, explain what command caused it

### Deliverables
```
✅ Screenshot of: git reflog output
✅ Written explanation (in README or written answer in notebook) for 5 HEAD movements:
   - HEAD@{0}: What happened?
   - HEAD@{1}: What happened?
   - HEAD@{2}: What happened?
   - HEAD@{3}: What happened?
   - HEAD@{4}: What happened?
```

### Example Format
```markdown
## Reflog Analysis

- **HEAD@{0}**: `git log` - Just viewing history (no movement)
- **HEAD@{1}**: `git checkout main` - Switched to main branch
- **HEAD@{2}**: `git merge rework/readme` - Merged rework branch
- **HEAD@{3}**: `git commit -m "Updated README"` - Made a commit
- **HEAD@{4}**: `git switch -c rework/readme abc1234` - Created branch at C0
```

***

**Answer**

<img width="1141" height="181" alt="Screenshot 2026-09-20 102523" src="https://github.com/user-attachments/assets/5cd971d8-a23b-4e3c-8c70-45bbe20792a5" />

```markdown
## Reflog Analysis

- **HEAD@{0}**: `git checkout main` - Switched from the `stu/feature` branch to the `main` branch.
- **HEAD@{1}**: `git rebase origin/main` - The rebase finished and Git returned to the `stu/feature` branch.
- **HEAD@{2}**: `git rebase origin/main` - The rebase started by checking out `origin/main` as the base for the rebase.
- **HEAD@{3}**: `git checkout stu/feature` - Switched from the `main` branch to the `stu/feature` branch.
- **HEAD@{4}**: `git checkout main` - Ran checkout to move from `main` to `main`; since already on `main`, there was no actual branch change.
```

***

## 📋 Part 4: Challenge - Multiple Recoveries (BONUS ASSIGNMENT)

### Task
1. Create a repository with 5 commits (C0 to C4)
2. Reset to C2 (losing C3 and C4)
3. Recover C4 using reflog
4. Make 2 more commits (C5, C6)
5. Reset to C3 (losing C4, C5, C6)
6. Recover all lost commits using reflog
7. Document your process

### Deliverables
```
✅ Screenshot of: git reflog showing multiple recoveries
✅ Screenshot of: Final git log --oneline --graph
✅ Brief write-up: What challenges did you face? How did you solve them?
```

**Answer**

<img width="897" height="722" alt="Screenshot 2026-09-20 153437" src="https://github.com/user-attachments/assets/b5b15729-2ec3-42f1-8e9c-317fd9aa6afb" />
<img width="692" height="197" alt="Screenshot 2026-09-20 153550" src="https://github.com/user-attachments/assets/2b9f7027-8530-44d5-b2e2-fac0d3a8aa6b" />

```
Challenges Faced

The main challenge was understanding what happens to commits after using git reset --hard. After resetting to C2, commits C3 and C4 were no longer visible in the normal Git history.

How I Solved Them

I used git reflog to find the previous positions of HEAD. The reflog showed the commit hashes of the commits that were no longer visible in the normal branch history. I used those commit hashes to recover the lost commits.

Later, after creating C5 and C6, I again reset the branch to C3. I used git reflog again to locate C4, C5, and C6 and recovered them.
```

***

## 📤 Submission Guidelines

- Push all repositories to your GitHub account
- Use your **CodingGita_Assignment** repository for all practical work and submission.
- Complete the assignments in order.
- For theoretical questions → write a short and correct answer in your notebook.
- Take clear photos of the written answers.
- Take screenshots of terminal / GitHub where asked.
- Push your practical work to the repository and submit the repository link along with the required photos and screenshots.

***
