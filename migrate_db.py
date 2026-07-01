#!/usr/bin/env python3
"""
Database migration script for Walk-In RFQ support
Adds new columns to bids table and creates bid_attachments table
"""
import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'app.db'

def migrate():
    """Apply database migrations for Walk-In RFQ support"""
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}. Creating new database...")
        db = sqlite3.connect(DB_PATH)
    else:
        db = sqlite3.connect(DB_PATH)
    
    cursor = db.cursor()
    
    try:
        # Get existing columns in bids table
        cursor.execute("PRAGMA table_info(bids)")
        existing_columns = {row[1] for row in cursor.fetchall()}
        print(f"Existing columns in bids: {existing_columns}")
        
        # Define new columns to add
        new_columns = {
            'rfq_source': "VARCHAR(20) DEFAULT 'online'",
            'pr_number': "VARCHAR(255)",
            'office_department': "VARCHAR(255)",
            'supplier_name': "VARCHAR(255)",
            'company_address': "TEXT",
            'contact_email': "VARCHAR(255)",
            'contact_phone': "VARCHAR(20)",
        }
        
        # Add missing columns
        for col_name, col_type in new_columns.items():
            if col_name not in existing_columns:
                alter_sql = f'ALTER TABLE bids ADD COLUMN {col_name} {col_type}'
                print(f"Adding column: {col_name}")
                cursor.execute(alter_sql)
                print(f"  ✓ Added {col_name}")
            else:
                print(f"  • Column {col_name} already exists")
        
        # Check if bid_attachments table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bid_attachments'")
        if not cursor.fetchone():
            print("\nCreating bid_attachments table...")
            create_table_sql = '''
                CREATE TABLE bid_attachments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    bid_id INTEGER NOT NULL,
                    filename VARCHAR(255) NOT NULL,
                    original_filename VARCHAR(255) NOT NULL,
                    attachment_type VARCHAR(50),
                    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    file_size INTEGER,
                    file_path VARCHAR(1024),
                    FOREIGN KEY (bid_id) REFERENCES bids(id) ON DELETE CASCADE
                )
            '''
            cursor.execute(create_table_sql)
            print("  ✓ Created bid_attachments table")
        else:
            print("  • bid_attachments table already exists")
        
        db.commit()
        print("\n✓ Database migration completed successfully!")
        
    except Exception as e:
        print(f"\n✗ Error during migration: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == '__main__':
    migrate()
