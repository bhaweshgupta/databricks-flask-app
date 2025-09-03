# Deploying Flask Todo App to Databricks

This guide walks you through deploying your Flask todo application to Databricks using Databricks Apps.

## Prerequisites

1. **Databricks Workspace**: You need access to a Databricks workspace
2. **Databricks CLI**: Install and configure the Databricks CLI
3. **Databricks Apps**: Ensure your workspace has Databricks Apps enabled

## Step 1: Install Databricks CLI

```bash
pip install databricks-cli
```

## Step 2: Configure Databricks CLI

1. Get your Databricks workspace URL and personal access token
2. Configure the CLI:

```bash
databricks configure --token
```

Enter your workspace URL (e.g., `https://your-workspace.cloud.databricks.com`) and access token when prompted.

## Step 3: Verify Connection

Test your connection:

```bash
databricks workspace list /
```

## Step 4: Deploy Your App

### Option A: Using the deployment script (Recommended)

```bash
python deploy_to_databricks.py
```

### Option B: Manual deployment

1. **Upload your app files to Databricks workspace:**

```bash
databricks workspace upload-dir . /Workspace/Users/your-email/flask-todo-app --overwrite
```

2. **Deploy using Databricks Apps:**

```bash
databricks apps deploy --source-dir . --app-name flask-todo-app
```

## Step 5: Access Your App

After successful deployment:

1. Go to your Databricks workspace
2. Navigate to "Apps" in the sidebar
3. Find your "flask-todo-app"
4. Click on the app URL to access your todo application

## Configuration Files Explained

### `databricks_app.py`
- Modified version of your Flask app optimized for Databricks
- Uses `/tmp/todo.db` for SQLite database (Databricks-compatible path)
- Configured for production environment

### `databricks-app.yml`
- Databricks Apps configuration file
- Defines resource requirements, health checks, and networking
- Specifies the entry point for your Flask application

### `requirements-databricks.txt`
- Python dependencies for Databricks deployment
- Includes `gunicorn` for production WSGI server

## Troubleshooting

### Common Issues:

1. **"databricks command not found"**
   - Install Databricks CLI: `pip install databricks-cli`

2. **Authentication errors**
   - Reconfigure CLI: `databricks configure --token`
   - Verify your access token is valid

3. **App deployment fails**
   - Check that Databricks Apps is enabled in your workspace
   - Verify you have the necessary permissions

4. **Database issues**
   - The app uses SQLite with `/tmp/todo.db` path
   - Data will be ephemeral (lost on app restart)
   - For persistent data, consider using Databricks SQL or external database

### Logs and Monitoring

View app logs in Databricks:
```bash
databricks apps logs flask-todo-app
```

## Production Considerations

1. **Database**: Replace SQLite with a persistent database (Databricks SQL, PostgreSQL, etc.)
2. **Security**: Update the SECRET_KEY in `databricks-app.yml`
3. **Scaling**: Adjust CPU/memory resources in the YAML file
4. **Monitoring**: Set up proper logging and monitoring

## Alternative Deployment Methods

### Method 1: Notebook-based Deployment

Create a Databricks notebook and run your Flask app:

```python
# In a Databricks notebook cell
%pip install Flask Flask-SQLAlchemy

# Copy your app code and run
# Note: This method is less suitable for production
```

### Method 2: MLflow Model Serving (API only)

If you only need API endpoints (no web UI):

```python
import mlflow
from mlflow.pyfunc import PythonModel

class TodoAPI(PythonModel):
    def predict(self, context, model_input):
        # Implement your API logic here
        pass

# Register and serve the model
```

## Next Steps

1. Test your deployed application
2. Set up monitoring and logging
3. Configure a persistent database if needed
4. Set up CI/CD pipeline for automated deployments
5. Configure custom domain (if available in your Databricks workspace)

## Support

- [Databricks Apps Documentation](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html)
- [Databricks CLI Reference](https://docs.databricks.com/en/dev-tools/cli/index.html)