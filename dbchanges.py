import psycopg2

# Fill in your actual password here
password = "etxMmAhtXmPwmbiZRoSmOeAASCMfylKt"

try:
    conn = psycopg2.connect(
        host="yamabiko.proxy.rlwy.net",
        port=58338,
        dbname="railway",
        user="postgres",
        password=password
    )

    cur = conn.cursor()

    # Modify this as needed
    cur.execute("ALTER TABLE deals RENAME COLUMN deal_amount TO promo_code;")
    conn.commit()

    print("Column renamed successfully.")

except Exception as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
