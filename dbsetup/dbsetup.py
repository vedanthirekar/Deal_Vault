from app import db, create_app

app = create_app()

with app.app_context():
    connection = db.engine.raw_connection()
    cursor = connection.cursor()
    
    with open("dbcreatequeries.sql", "r") as f:
        sql = f.read()
        for statement in sql.strip().split(";"):
            if statement.strip():
                try:
                    cursor.execute(statement + ";")
                except Exception as e:
                    print(f"⚠️ Failed on: {statement[:100]}...\n  → {e}")
    
    connection.commit()
    cursor.close()
    connection.close()

print("Database setup complete.")
