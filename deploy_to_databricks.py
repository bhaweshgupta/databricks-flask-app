#!/usr/bin/env python3
"""
Deployment script for Flask Todo App to Databricks
"""
import os
import subprocess
import sys

def check_databricks_cli():
    """Check if Databricks CLI is installed and configured"""
    try:
        result = subprocess.run(['databricks', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Databricks CLI found: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    
    print("❌ Databricks CLI not found. Please install it:")
    print("pip install databricks-cli")
    print("Then configure it with: databricks configure --token")
    return False

def check_workspace_connection():
    """Check if we can connect to Databricks workspace"""
    try:
        result = subprocess.run(['databricks', 'workspace', 'list', '/'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Connected to Databricks workspace")
            return True
        else:
            print("❌ Cannot connect to Databricks workspace")
            print("Please run: databricks configure --token")
            return False
    except Exception as e:
        print(f"❌ Error checking workspace connection: {e}")
        return False

def deploy_app():
    """Deploy the Flask app to Databricks"""
    print("🚀 Starting deployment to Databricks...")
    
    # Check prerequisites
    if not check_databricks_cli():
        return False
    
    if not check_workspace_connection():
        return False
    
    try:
        # Create app bundle
        print("📦 Creating app bundle...")
        
        # Deploy using Databricks Apps CLI
        cmd = [
            'databricks', 'apps', 'deploy',
            '--source-dir', '.',
            '--app-name', 'flask-todo-app'
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ App deployed successfully!")
            print(result.stdout)
            return True
        else:
            print("❌ Deployment failed:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")
        return False

if __name__ == "__main__":
    success = deploy_app()
    sys.exit(0 if success else 1)