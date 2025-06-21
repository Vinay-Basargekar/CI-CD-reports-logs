
# 🚀 CI/CD Pipeline for Docker Images with GitHub Actions

> **Reference**: [Automate Docker Image Builds & Push to Docker Hub Using GitHub Actions – DEV.to](https://dev.to/ken_mwaura1/automate-docker-image-builds-and-push-to-docker-hub-using-github-actions-32g5)

This project uses **GitHub Actions** to automatically build a Docker image and push it to **Docker Hub** whenever you push to the `main` branch. You can also configure it to push images to GitHub Packages or other branches as needed.

---

## ⚙️ How It Works

1. **Workflow File**: Defined at `.github/workflows/docker-build.yml`.
2. **Branch Triggers**: Automatically runs on push or PR to `main` or `dev` branches.
3. **Secrets**: Docker Hub credentials are securely stored as repository secrets:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`
4. **Automated Steps**:
   - ✅ Checkout code
   - 🛠️ Build Docker image
   - 🧪 (Optional) Test Docker image
   - 🔐 Log in to Docker Hub
   - 📤 Push image to Docker Hub

---

## 🔐 Setting Up Secrets

In your GitHub repository:

> Navigate to `Settings → Secrets and variables → Actions`

Add the following secrets:

- `DOCKER_USERNAME`: Your Docker Hub username  
- `DOCKER_PASSWORD`: Your Docker Hub password or access token  

---

## 📝 Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Vinay-Basargekar/docker-ci-cd-github-actions.git
cd docker-ci-cd-github-actions
```

2. Create and Push a Dev Branch
```bash
git checkout -b dev
git add .
git commit -m "Initial commit with workflow"
git push -u origin dev
```

3. Open a Pull Request
	•	Open a PR to merge `dev` into `main`.
	•	The workflow will run and push the Docker image to Docker Hub if successful.

4. Verify on Docker Hub
	•	Log in to Docker Hub and check for your new image under your account.

### 🐳 Example Workflow File

The main parts of `.github/workflows/docker-build.yml`:
```yaml
name: Build and Push Docker Image to Docker Hub

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: 🧾 Checkout Repository
        uses: actions/checkout@v3

      - name: 🐳 Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: 🔐 Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: 🔨 Build Docker Image and Log Output
        run: |
          mkdir -p shared-logs
          docker build -t vinay1304/flask-devops-app:latest . > shared-logs/build.log 2>&1

      - name: 📤 Upload Shared Directory as Artifact
        uses: actions/upload-artifact@v4
        with:
          name: docker-build-logs
          path: shared-logs/

```


Feel free to fork, modify, and use this setup for your own CI/CD pipeline!