# GitHub User Activity CLI

[![Python CI](https://github.com/chintanboghara/GitHub-User-Activity-roadmap.sh/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chintanboghara/GitHub-User-Activity-roadmap.sh/actions/workflows/ci.yml)

This project is a simple command-line tool that fetches and displays a GitHub user's recent activity using GitHub's public API. The tool outputs events such as commits, issues opened, and stars received in a human-readable format directly on the terminal.

## Features

- **Fetch User Activity:** Retrieve recent GitHub events for any specified user.
- **Display Events:** Show activities including commits, issues, and starred events.
- **Simple CLI Interface:** Easy-to-use command-line operations.

## Installation

### 1. Install Dependencies

Update your package lists and install Python pip. Then install the required Python packages:

```bash
sudo apt update
sudo apt install python3-pip
sudo pip3 install requests
```

### 2. Running the Script

Execute the script by passing a GitHub username as an argument:

```bash
python3 github_activity.py <username>
```

For example, to fetch activity for the user `chintanboghara`:

```bash
python3 github_activity.py chintanboghara
```

## Example Output

When you run the script, you can expect output similar to the following:

```bash
chintanboghara@HEYBEAST:~/Projects$ python3 github_activity.py chintanboghara
Pushed 2 commit(s) to chintanboghara/Landing-Page-S3-Auto-Deploy-gh-Actions
Pushed 1 commit(s) to chintanboghara/Two-Tier-DockerBridge-Flask-MySQL
Pushed 1 commit(s) to chintanboghara/Two-Tier-DockerBridge-Flask-MySQL
Pushed 1 commit(s) to chintanboghara/IaC-Terraform
Pushed 1 commit(s) to chintanboghara/IaC-Terraform
Pushed 1 commit(s) to chintanboghara/IaC-Terraform
Pushed 2 commit(s) to chintanboghara/IaC-Terraform
Pushed 1 commit(s) to chintanboghara/AWS-EC2-Instance-Creation-with-Vault-Secrets-Integration
Pushed 1 commit(s) to chintanboghara/AWS-EC2-Instance-Creation-with-Vault-Secrets-Integration
Pushed 1 commit(s) to chintanboghara/HashiCorp-Vault-Integration-DevMoDeEnV
Pushed 1 commit(s) to chintanboghara/HashiCorp-Vault-Integration-DevMoDeEnV
Pushed 1 commit(s) to chintanboghara/HashiCorp-Vault
Pushed 1 commit(s) to chintanboghara/HashiCorp-Vault-Installation-on-AWS-EC2
Pushed 1 commit(s) to chintanboghara/Two-Tier-DockerBridge-Flask-MySQL
Pushed 1 commit(s) to chintanboghara/Two-Tier-DockerBridge-Flask-MySQL
Pushed 1 commit(s) to chintanboghara/Two-Tier-DockerBridge-Flask-MySQL
Pushed 1 commit(s) to chintanboghara/Two-Tier-DockerBridge-Flask-MySQL
```

## How It Works

- **Data Fetching:** The script uses GitHub's API endpoint  
  `https://api.github.com/users/<username>/events`  
  to fetch a list of recent events for the specified user.
- **Event Parsing:** It processes the JSON response and extracts relevant details.
- **Supported Event Types:**  
  Currently, the script handles:
  - **PushEvent:** Displays commit information.
  - **IssuesEvent:** Shows newly opened issues.
  - **WatchEvent:** Indicates when a repository is starred.
