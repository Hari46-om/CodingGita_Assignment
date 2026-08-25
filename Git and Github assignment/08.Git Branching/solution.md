### Assignment 1: Understanding Concepts

**Objective:** Check basic understanding of branching.

**Tasks:**
1. What is a **branch** in Git? Explain in your own words.
2. Why should we **not** work directly on the `main` branch?
3. Explain the road analogy of branching (main road vs side road).
4. What is the difference between `git branch` and `git switch`?

**Submission:** Written answers in your notebook.

**Answers:**

<img width="1152" height="1307" alt="image" src="https://github.com/user-attachments/assets/6b491ee2-b576-412b-b376-0a863e1cab31" />
<img width="1600" height="1283" alt="image" src="https://github.com/user-attachments/assets/69a8ca91-9d2a-4336-93b5-a5836aaab5b2" />


---

### Assignment 2: Commands Identification

**Objective:** Identify the correct commands.

**Tasks:**
1. Write the command for the following actions:

| Action                              | Command |
|-------------------------------------|---------|
| List all branches                   |         |
| Create a new branch named `feature-home` |    |
| Switch to `feature-home`            |         |
| Create + Switch in one command      |         |
| Merge `feature-home` into main      |         |
| Delete `feature-home` after merge   |         |

2. Write both the **modern** and **older** command for:
   - Switching to a branch
   - Creating + switching to a new branch

**Submission:** Filled table + answers

**Answers:**

<img width="1600" height="832" alt="image" src="https://github.com/user-attachments/assets/dcc3e3d7-57e6-4bfe-8e43-d2f0e0916e51" />
<img width="1599" height="584" alt="image" src="https://github.com/user-attachments/assets/9f6294e6-2387-4473-8e57-392de09d0440" />



---

### Assignment 3: Practical Branching Workflow

**Objective:** Perform the complete branching cycle.

**Tasks:**
1. Make sure you are on the `main` branch.
2. Create a new branch named `feature-contact`.
3. Create a file `contact.txt` and write your name + any message.
4. Stage and commit the file with a meaningful message.
5. Switch back to `main`.
6. Merge `feature-contact` into `main`.
7. Delete the `feature-contact` branch.
8. Verify using:
   - `git branch`
   - `git log --oneline`

**Submission:**  
- Screenshot of `git branch` (before and after)  
- Screenshot of `git log --oneline`  
- Screenshot showing `contact.txt` is present on `main`

**Answers:**

<img width="727" height="75" alt="Screenshot 2026-08-25 181719" src="https://github.com/user-attachments/assets/6071d49f-1580-4cc0-9e8b-058ed6c6b1b6" />
<img width="846" height="111" alt="Screenshot 2026-08-25 181740" src="https://github.com/user-attachments/assets/3f9986bc-4deb-4bd1-9798-a32976da399d" />
<img width="722" height="115" alt="Screenshot 2026-08-25 181753" src="https://github.com/user-attachments/assets/59c6458d-7674-421c-b8a7-2f76e43f700a" />
<img width="700" height="307" alt="Screenshot 2026-08-25 181942" src="https://github.com/user-attachments/assets/3b01eb9f-c697-471f-b323-4e98624d6144" />



---

### Assignment 4: Conceptual + Error Handling

**Objective:** Understand rules and common mistakes.

**Tasks:**
1. What will happen if you try to delete a branch that is not yet merged?  
   Write the error and how to fix it.
2. Why should you always **commit** before switching branches?
3. Fill in the correct flow:

```
______ → Work → ______ → ______ → Switch to main → ______ → Delete branch
```

4. Explain the difference between:
   - `git branch -d branch-name`
   - `git branch -D branch-name`

**Submission:** Written answers

**Answers:**

<img width="1599" height="1384" alt="image" src="https://github.com/user-attachments/assets/ab48e8f9-897e-40d1-addb-a2a9865c397d" />
<img width="1303" height="1600" alt="image" src="https://github.com/user-attachments/assets/3659b187-bee3-42ef-9e78-bf3688659ef2" />



---

### Assignment 5: Complete Real Scenario

**Objective:** Apply branching in a realistic situation.

**Scenario:**  
You are working on a website project. Currently you are on the `main` branch. You need to add two new pages: **About** and **Services**.

**Tasks:**
1. Create a branch `feature-about`, add a file `about.txt`, commit it, merge it into `main`, and delete the branch.
2. Create another branch `feature-services`, add a file `services.txt`, commit it, merge it into `main`, and delete the branch.
3. After completing both, show:
   - Final list of branches (`git branch`)
   - Final commit history (`git log --oneline`)
4. Answer:
   - Why did we create two separate branches instead of doing both features on one branch?
   - What is the advantage of merging only after the feature is complete?

**Submission:**  
- Screenshots of both merges  
- Final `git branch` and `git log --oneline`  
- Written answers for the two questions

- **Answers:**
- <img width="803" height="82" alt="Screenshot 2026-08-25 183040" src="https://github.com/user-attachments/assets/f23f5b75-5e46-4630-94b1-4484c7ce44dc" />
<img width="753" height="165" alt="Screenshot 2026-08-25 183029" src="https://github.com/user-attachments/assets/bd120fce-2869-4607-aabe-16ae8feecbc6" />

