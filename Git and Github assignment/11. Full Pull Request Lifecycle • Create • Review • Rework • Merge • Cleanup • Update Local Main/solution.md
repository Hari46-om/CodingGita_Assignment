### Assignment 1 – Complete PR Lifecycle with `feature/contact-form` (Mandatory)

**Goal:** Practice the full cycle: branch → file → commit → push → PR → merge → cleanup.

1. Update main:  
   `git checkout main && git pull origin main`
2. Create branch:  
   `git checkout -b feature/contact-form`
3. Create file `contact.html` with a simple heading and a short paragraph about a contact form.
4. Stage, commit and push:  
   ```bash
   git add contact.html
   git commit -m "Add contact form page"
   git push -u origin feature/contact-form
   ```
5. On GitHub: Open a Pull Request (base = `main`, compare = `feature/contact-form`). Write a clear title and description.
6. Merge the Pull Request using **“Create a merge commit”**.
7. Delete the remote branch (GitHub “Delete branch” button or `git push origin --delete feature/contact-form`).
8. Update local main using the two-command method:  
   ```bash
   git checkout main
   git fetch origin main
   git merge origin/main
   ```
9. Delete local branch:  
   `git branch -d feature/contact-form`
10. Take screenshots of:  
    (a) the merged PR  
    (b) terminal after fetch + merge  
    (c) `git branch` showing the branch is gone

**Submit:** Merged PR link + the 3 screenshots listed above.

**Answer**


Merged PR link  --  https://github.com/Hari46-om/CG_Assignments-/pull/1

screenshots --

<img width="992" height="250" alt="Screenshot 2026-09-04 173913" src="https://github.com/user-attachments/assets/bd962257-6620-4380-88c7-5a2a8a0ada3b" />
<img width="672" height="398" alt="Screenshot 2026-09-04 174231" src="https://github.com/user-attachments/assets/8f3c7b23-a224-4112-a81a-3b3b589ff994" />
<img width="592" height="102" alt="Screenshot 2026-09-04 174435" src="https://github.com/user-attachments/assets/0b314768-4e27-4ac6-a9bd-4de628625843" />


---

### Assignment 2 – `feature/about-page` with Review & Rework (Mandatory)

**Goal:** Practice receiving a review comment, reworking the **same** branch, and updating the PR.

1. Create branch:  
   `git checkout -b feature/about-page`
2. Create `about.html` with only a basic heading (intentionally incomplete).
3. Commit and push:  
   ```bash
   git add .
   git commit -m "Add about page skeleton"
   git push -u origin feature/about-page
   ```
4. Open a Pull Request on GitHub.
5. **Simulate review:** Add a comment on the PR yourself (or ask a classmate/mentor) requesting:  
   *“Please add a short paragraph about the purpose of the about page and a simple team section placeholder.”*
6. Rework on the **same branch**:  
   ```bash
   git checkout feature/about-page
   # edit about.html as requested
   git add .
   git commit -m "Address review: add description and team section"
   git push origin feature/about-page
   ```
7. Confirm the PR on GitHub now shows the new commit.
8. Merge the PR, delete remote branch, update local main (`git fetch` + `git merge` or `git pull`), delete local branch.
9. Screenshot:  
   (a) PR conversation showing the review comment + your new commit  
   (b) merged PR

**Submit:** PR link showing review comment + rework commit, plus merged PR screenshot.

Merged PR link  --  https://github.com/Hari46-om/CG_Assignments-/pull/4/commits

screenshots --


<img width="847" height="201" alt="Screenshot 2026-09-05 192625" src="https://github.com/user-attachments/assets/e700d117-7602-48ba-9b0a-c1ad8d95f57a" />

<img width="1142" height="140" alt="Screenshot 2026-09-05 190934" src="https://github.com/user-attachments/assets/9cb0011a-9cd6-4cfe-91f3-ada8ec909243" />

<img width="746" height="95" alt="image" src="https://github.com/user-attachments/assets/0a1da70e-2b26-48b7-8053-0b2028db4f48" />


---

### Assignment 3 – `feature/navbar` Independent Full Cycle (Mandatory)

**Goal:** Independently complete one more full PR lifecycle.

1. Create `feature/navbar` branch from updated main.
2. Create `navbar.html` with a heading and 3–4 lines describing what a navigation bar contains (Home, About, Contact, etc.).
3. Commit, push, open PR with a clear title and description.
4. Merge the PR on GitHub.
5. Delete remote branch.
6. Update local main using:  
   ```bash
   git fetch origin main
   git merge origin/main
   ```
7. Delete local branch with `git branch -d feature/navbar`.
8. Run `git log --oneline -10` and take a screenshot showing the merge commits from the features you completed.

**Submit:** Merged PR link + screenshot of `git log --oneline`.

Merged PR link  --  https://github.com/Hari46-om/CG_Assignments-/pull/5

screenshots --

<img width="973" height="222" alt="Screenshot 2026-09-05 200435" src="https://github.com/user-attachments/assets/af27d9af-2b39-4496-a97d-b91277a81938" />

<img width="668" height="275" alt="Screenshot 2026-09-05 200946" src="https://github.com/user-attachments/assets/141499bf-218d-486e-8f5f-fde34a257164" />



---

### Assignment 4 – Short Reflection (Mandatory)

Write answer **in your own words** in your notebook:

- Why do we push new commits to the **same** feature branch after a review instead of creating a new PR?
- What is the difference between deleting a remote branch and deleting a local branch?
- Why must we run `git fetch` + `git merge` (or `git pull`) after merging a PR on GitHub?
- Write the full sequence of commands you used to update local main and delete the local feature branch.

**Submit:** Photos of the hand written answers of the above questions.

**Answer:**


<img width="1599" height="1470" alt="image" src="https://github.com/user-attachments/assets/aa1e35f3-9f37-4e64-a9e2-164aa4ec8954" />
<img width="1570" height="1600" alt="image" src="https://github.com/user-attachments/assets/1fc7dbc9-9015-4bc4-b394-9cb9cff3e9de" />


---

### Bonus – Peer Review Simulation (Optional)

Pair with a classmate (or use two clones):

1. Person A creates a feature branch (example: `feature/footer`) and opens a PR.
2. Person B leaves a meaningful review comment requesting a small improvement.
3. Person A reworks, pushes, and asks for re-review.
4. Person B approves; Person A merges and completes cleanup.
5. Both update their local main and confirm the file is present.

**Submit (optional):** PR link showing the review conversation + photo short note on what you learned.

---

### Deadline : 27th August, 2026.
