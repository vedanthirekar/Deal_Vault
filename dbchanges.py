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
    cur.execute("ALTER TABLE deals ALTER COLUMN promo_code TYPE VARCHAR(100);")
    conn.commit()

    print("Column changed successfully.")

except Exception as e:
    print("Error:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
