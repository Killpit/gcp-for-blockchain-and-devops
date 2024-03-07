# Cloud Source Repositories

Cloud Source Repositories are Google Cloud's Git-based repository solution hosted on its platform. The repositories allow you to develop and deploy your applications or services with version control and collaboration.

### How to create a cloud source repository?

- Open a Google Cloud account if you didn't have one and install gcloud CLI
- Make sure you have the latest git version and if you don't have it, update to the latest version
- Initialize gcloud CLI with `gcloud init`
- Create your repository with `gcloud source repos create demo-repo`
- Clone the repository with `gcloud source repos clone demo-repo`
- Create app.yaml and main.py file in demo-repo
- Go to `demo-repo` with `cd demo-repo` and write `git add .`
- After adding the files, use `git commit -m "message"`
- Then push the files with `git push origin master`