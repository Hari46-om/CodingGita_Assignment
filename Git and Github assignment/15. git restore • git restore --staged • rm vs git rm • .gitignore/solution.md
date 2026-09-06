## Assignment 1 – Practice `git restore` and `git restore --staged`

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
```bash
git restore profile.txt
```
Observe that it does **not** work (because the file is untracked).
4. Stage the file:
```bash
git add profile.txt
```
5. Unstage it using:
```bash
git restore --staged profile.txt
```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
```bash
git add profile.txt
git commit -m "Add profile.txt"
```

**Submit:**
- Screenshot of `git status` when the file was untracked
- Screenshot after using `git restore --staged`
- Repository link

---
**Answer**

<img width="772" height="312" alt="Screenshot 2026-09-06 180319" src="https://github.com/user-attachments/assets/a638e270-3158-4271-8a52-77818ea0642c" />




## Assignment 2 – `rm` vs `git rm`

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
```bash
rm profile.txt
```
3. Run `git status` and observe the output.
4. Recover the file using:
```bash
git restore profile.txt
```
5. Now delete it properly with Git:
```bash
git rm profile.txt
```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
```bash
git commit -m "Remove profile.txt using git rm"
```
8. Create a short file named `delete-difference.txt` and write in your own words:
- What is the difference between `rm` and `git rm`?
- When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

---

**Answer**

<img width="701" height="351" alt="Screenshot 2026-09-06 182427" src="https://github.com/user-attachments/assets/43c54146-877f-4a1a-80ed-4c354464df07" />
<img width="597" height="305" alt="Screenshot 2026-09-06 182411" src="https://github.com/user-attachments/assets/78b30e13-ad00-4b73-aad6-38af7da9ef33" />
<img width="787" height="456" alt="Screenshot 2026-09-06 182451" src="https://github.com/user-attachments/assets/5d7c6849-e371-42b5-ab00-99e0e832969e" />



## Assignment 3 – `.gitignore` + `git rm --cached`

**Goal:** Properly ignore sensitive files and practice stopping Git from tracking a file using `git rm --cached`.

1. Create a file named `config.env` with sample secret data:
```env
DB_PASSWORD=SuperSecretPass999
API_KEY=sk-test-abc123xyz789
```

2. **Intentionally** add and commit it (to practice the fix):
```bash
git add config.env
git commit -m "Accidentally commit config.env"
```

3. Create a folder named `vendor` and put any dummy file inside it.

4. Create a `.gitignore` file and add:
```gitignore
vendor/
config.env
```

5. Stop tracking `config.env` but **keep the file on your computer**:
```bash
git rm --cached config.env
```

6. Run `git status` and observe that `config.env` is staged for removal from Git (but the file still exists locally).

7. Commit the fix:
```bash
git add .gitignore
git commit -m "Stop tracking config.env and add .gitignore"
git push origin main
```

8. Confirm on GitHub that `config.env` is **no longer visible** in the repository, while the file still exists on your local machine.

9. Create a file named `why-gitignore.txt` and answer:
- Why should we ignore folders like `vendor` or `node_modules`?
- Why should we ignore files like `config.env` or `.env`?
- What does `git rm --cached` do?
- Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` after using `git rm --cached`
- Screenshot showing that `config.env` is ignored / removed from GitHub
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)

---

**Answer**

<img width="657" height="410" alt="Screenshot 2026-09-06 185916" src="https://github.com/user-attachments/assets/80cdd9e2-2282-493c-99fe-ee622505131d" />
<img width="921" height="442" alt="Screenshot 2026-09-06 190908" src="https://github.com/user-attachments/assets/de8e9eaf-b701-47ba-8424-085ac9713ee8" />
<img width="650" height="321" alt="Screenshot 2026-09-06 190619" src="https://github.com/user-attachments/assets/2f767155-a37f-4488-a398-baf34adf328d" />
<img width="1223" height="507" alt="Screenshot 2026-09-06 191234" src="https://github.com/user-attachments/assets/8d36df4c-3d34-4106-ba4c-4b61d32ea992" />

Repository link--https://github.com/Hari46-om/CG_practice/blob/main/.gitignore


## Bonus Assignment (Optional)

1. Modify a tracked file (create one if needed) and use `git restore <filename>` to discard the changes.
2. Stage a file and then unstage it using `git restore --staged`.
3. Take screenshots of both actions.

**Submit (optional):** Screenshots of both restore operations.

---

## Submission Checklist

| # | Item | Required? |
| --- | -------------------------------------------------------------- | ------------- |
| 1 | Assignment 1 – screenshots of restore practice | Yes |
| 2 | Assignment 2 – `rm` vs `git rm` screenshots + explanation file | Yes |
| 3 | Assignment 3 – `.gitignore` + `git rm --cached` practice + explanation file | Yes |
| 4 | Bonus restore practice assignment | No (optional) |
| — | GitHub repository link | Yes |

**Important:**
- Make sure `config.env` is **not** pushed to GitHub after Assignment 3.
- Your `.gitignore` file **should** be present in the repository.

---
