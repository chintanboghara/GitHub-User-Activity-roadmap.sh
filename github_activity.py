import argparse
import requests
import json

# Function to fetch user activity
def fetch_github_activity(username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Error fetching data for {username}: {response.status_code}")
        return []
    
    # Parse the JSON response
    activities = response.json()
    return activities

# Function to display the user activity
def display_activity(activities):
    if not activities:
        print("No activity found.")
        return
    
    for activity in activities:
        # Process the event type
        event_type = activity['type']
        repo_name = activity['repo']['name']
        
        if event_type == 'PushEvent':
            commits = activity['payload']['commits']
            print(f"Pushed {len(commits)} commit(s) to {repo_name}")
        elif event_type == 'IssuesEvent' and activity['payload']['action'] == 'opened':
            print(f"Opened a new issue in {repo_name}")
        elif event_type == 'WatchEvent' and activity['payload']['action'] == 'star':
            print(f"Starred {repo_name}")
        # Add more event types as needed
        
# Main function to handle the command-line interface
def main():
    parser = argparse.ArgumentParser(description="Fetch and display GitHub user activity.")
    parser.add_argument('username', type=str, help="GitHub username")
    args = parser.parse_args()
    
    # Fetch the activity
    activities = fetch_github_activity(args.username)
    
    # Display the activity
    display_activity(activities)

if __name__ == '__main__':
    main()
