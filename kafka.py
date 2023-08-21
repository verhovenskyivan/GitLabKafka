import gitlab
import yaml

# GitLab configuration
gitlab_url = "https://gitlab.com"  # Replace with your GitLab URL
gitlab_token = "YOUR_GITLAB_TOKEN"
project_id = "YOUR_PROJECT_ID"
branch_name = "YOUR_BRANCH_NAME"
file_path = "path/to/your/file.yaml"  # Replace with the path to your YAML file in the repository

# Load the GitLab project
gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_token)
project = gl.projects.get(project_id)

# Get the file from the repository
file = project.files.get(file_path=file_path, ref=branch_name)

# Load the YAML content
yaml_content = yaml.safe_load(file.decode())

# Make changes to the YAML content (for example, add or modify key-value pairs)
yaml_content["new_key"] = "new_value"

# Convert the modified content back to YAML
modified_yaml = yaml.dump(yaml_content, default_flow_style=False)

# Commit and push the changes back to the repository
project.commits.create({
    "branch": branch_name,
    "commit_message": "Update YAML file",
    "actions": [
        {
            "action": "update",
            "file_path": file_path,
            "content": modified_yaml,
        }
    ]
})

print("YAML file updated successfully.")
