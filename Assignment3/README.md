# Linux User Management & File Permissions

## 🛠️ Tasks

### 1. User Account Creation
Created two separate user accounts to simulate a multi-user environment.
- **Command used:**`sudo useradd Jala1 Jala2`
- **Verification:** Verified user existence using `id Jala1` and by inspecting `/etc/passwd`.

### 2. File Ownership Transfer
Created a sensitive text file and transferred ownership to a specific user to ensure data accountability.
- **Command used:** `sudo chown Jala1:users textfile.txt`
- **Goal:** Ensuring that only the designated "owner" has primary control over the file.

### 3. Implementing Restricted Permissions (chmod 600)
Configured the file permissions so that **only the owner** can read and write to the file, while all other users (including the group) are completely blocked. 
4 = Read >>(r)
2 = Write >>(w)

- **Command used:** `sudo chmod 600 textfile.txt`
- **Permission string:** `-rw-------`


## 🔍 Verification Proof
To verify the security of the file, I performed a long listing:
```bash
ll 
