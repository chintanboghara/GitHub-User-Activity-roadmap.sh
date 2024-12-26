[![Python CI](https://github.com/chintanboghara/GitHub-User-Activity-roadmap.sh/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/chintanboghara/GitHub-User-Activity-roadmap.sh/actions/workflows/ci.yml)

This project is a simple command-line tool to fetch and display a GitHub user's recent activity. It uses GitHub's public API to fetch events and outputs them in a human-readable format on the terminal.

## Features

- Fetch recent GitHub activity of any user.
- Display activities like commits, issues opened, and stars received.
- Easy to use command-line interface.

## Prerequisites

To run this project, you need:

- Python 3.x
- `pip` (Python's package installer)

## Installation

### Step 1 Install Dependencies

Install the required dependencies using `pip3`:

```bash
sudo apt update
sudo apt install python3-pip
sudo pip3 install requests
```

### Step 2: Run the Script

Run the script by passing a GitHub username as an argument:

```bash
python3 github_activity.py <username>
```

For example, to fetch activity for the user `chintanboghara`:

```bash
python3 github_activity.py chintanboghara
```

### Output Example

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

- The script fetches a list of events using the GitHub API endpoint: `https://api.github.com/users/<username>/events`.
- It parses the events and displays them in a user-friendly format.
- The script currently handles **PushEvent**, **IssuesEvent**, and **WatchEvent** (starred events). You can extend it to support more event types.
