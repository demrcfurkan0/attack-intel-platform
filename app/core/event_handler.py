import os, json, joblib, traceback
from app.database.database import db_manager
from app.core.config import Config
from app.core import state 
from .security import get_password_hash
from dotenv import load_dotenv

load_dotenv()

async def create_initial_admin_user():

    print("First Admin User Check")
    db_conn = db_manager.get_db()
    if db_conn is None:
        print("Database connection failed")
        return
    
    # Create admin only if the 'users' collection is empty.
    if db_conn.users.count_documents({}) == 0:
        print("No user found, creating default admin user")
        
        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123") 
        
        admin_user = {
            "username": admin_username,
            "email": admin_email,
            "password": get_password_hash(admin_password),  # Hash the password for security.
            "role": "Administrator",
            "status": "active"
        }
        
        try:
            db_conn.users.insert_one(admin_user)
            print(f"Default admin user '{admin_username}' created successfully.")
            print(f"Password: {admin_password} (Please change it after first login)")
        except Exception as e:
            print(f"Error creating default admin user: {e}")
    else:
        print("User already exists, skipping admin user creation.")


async def startup_event():
    print("Starting the application...")
    db_manager.connect()
    
    await create_initial_admin_user()
    print("Loading AI Model, Scaler and Feature Columns...")
    try:
        
    # Note: Model loading logic is in main.py's startup event.
    # This is a placeholder print statement.
    
        print("AI Model, Scaler and Feature Columns loaded successfully.")
    except Exception as e:
        print(f"Error loading AI Model, Scaler and Feature Columns: {e}")

    print("Application startup completed.")

async def shutdown_event():
    print("Shutting down the application...")
    db_manager.close()
    print("Application shutdown completed.")