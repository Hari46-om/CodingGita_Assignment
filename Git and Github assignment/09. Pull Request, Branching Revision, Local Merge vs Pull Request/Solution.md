

### Assignment 1: Branching Commands & Naming###

**Objective:** Revise branching commands and naming conventions.

**Tasks:**
1. Write the modern and older command for the following:

| Action                         | Modern Command | Older Command |
|--------------------------------|----------------|---------------|
| Switch to a branch             |                |               |
| Create + Switch to new branch  |                |               |
| Merge a feature branch         |                |               |
| Delete a merged branch         |                |               |

2. Write 4 **good** branch names and 4 **bad** branch names.
3. What is the recommended naming convention for feature branches?

**Submission:** Written answers

**Answers:**

<img width="1599" height="870" alt="image" src="https://github.com/user-attachments/assets/aaadffb9-114f-4031-be10-bd40b5aa4098" />
<img width="1286" height="1600" alt="image" src="https://github.com/user-attachments/assets/1af38a02-d372-4cef-8420-04e094b839b9" />


---

### Assignment 2: Local Merge vs Pull Request

**Objective:** Understand the difference between the two methods.

**Tasks:**
1. Create a comparison table between **Local Merge** and **GitHub Pull Request** (at least 5 points).
2. When should you use Local Merge?
3. When should you use a Pull Request?
4. Why is Pull Request preferred in team/professional projects?

**Submission:** Written answers

**Answers:**
<img width="1402" height="1600" alt="image" src="https://github.com/user-attachments/assets/4a38eca0-2693-423c-a8a5-215a2599baae" />
<img width="1600" height="582" alt="image" src="https://github.com/user-attachments/assets/b765d8be-0aab-4678-a910-a493c68f98e9" />


---

### Assignment 3: Practical Local Merge

**Objective:** Practice the complete local merge workflow.

**Tasks:**
1. Make sure you are on `main`.
2. Create a branch named `feature/about-page`.
3. Create a file `about.txt` and add some content.
4. Stage and commit with a meaningful message.
5. Switch to `main` and merge the branch.
6. Delete the feature branch.
7. Verify with `git branch` and `git log --oneline`.

**Submission:**  
- Screenshot of `git branch` (final)  
- Screenshot of `git log --oneline`  
- Screenshot showing `about.txt` is present on main

**Answers:**
<img width="633" height="85" alt="Screenshot 2026-08-25 193942" src="https://github.com/user-attachments/assets/61d39850-2562-468c-8349-0f521bec7bf0" />
<img width="590" height="120" alt="Screenshot 2026-08-25 193950" src="https://github.com/user-attachments/assets/8b70c631-c14d-47f8-b151-9cdc96e990e1" />
<img width="1177" height="276" alt="Screenshot 2026-08-25 194550" src="https://github.com/user-attachments/assets/66af8067-64fc-4aa7-8f45-905553e8d473" />


---

### Assignment 4:  Create & Merge Pull Request

**Objective:** Perform the professional Pull Request workflow.

**Tasks:**
1. Create a new branch `feature/services-page`.
2. Add a file `services.txt` with any content.
3. Commit the changes.
4. Push the branch using:
   ```bash
   git push -u origin feature/services-page
   ```
5. Go to GitHub and create a Pull Request.
6. Merge the Pull Request.
7. Delete the branch on GitHub.
8. Update your local main:
   ```bash
   git switch main
   git pull origin main
   git branch -d feature/services-page
   ```

**Submission:**  
- Screenshot of the created Pull Request  
- Screenshot after merging the PR  
- Screenshot of final `git log --oneline` on main

**Answers:**
<img width="1253" height="286" alt="Screenshot 2026-08-25 195253" src="https://github.com/user-attachments/assets/6942e626-e592-4204-8d76-5d2da2fee728" />
<img width="848" height="746" alt="Screenshot 2026-08-25 195433" src="https://github.com/user-attachments/assets/9f6ed253-bc30-4d4c-b69e-b27c9f129337" />
<img width="527" height="185" alt="Screenshot 2026-08-25 195721" src="https://github.com/user-attachments/assets/97742920-2f21-4c7d-b99f-61032cbd515c" />



---

### Assignment 5: Complete Understanding + Reflection

**Objective:** Test deep understanding of Day 9 concepts.

**Tasks:**
1. Write the complete **Local Merge** workflow (step-by-step commands).
2. Write the complete **Pull Request** workflow (step-by-step).
3. Answer the following:
   - Why should we always run `git pull` on main before creating a new feature branch?
   - What happens if you merge a PR on GitHub but forget to run `git pull` locally?
   - Why should feature branches be deleted after merging?
4. Write 4 key takeaways from Day 9.

**Submission:** Written answers

**Answers:**

<img width="1599" height="1567" alt="image" src="https://github.com/user-attachments/assets/65cc6160-550e-4394-9c61-b9ee9f7f9a49" />
<img width="1152" height="1363" alt="image" src="https://github.com/user-attachments/assets/4edb6101-186a-4b98-a950-aa7087c18a4d" />
<img width="1563" height="1600" alt="image" src="https://github.com/user-attachments/assets/df00db45-1572-472e-9966-a7d9608848ea" />


---
