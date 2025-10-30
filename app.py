from flask import Flask, render_template, request, redirect, url_for, flash
import json, os

app = Flask(__name__)
app.secret_key = "supersecretkey"

DATA_FILE = "data.json"

# === Fungsi bantu untuk load & save data ===
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# === Inisialisasi data dari file ===
transactions = load_data()

@app.route('/')
def index():
    total_balance = sum(t['amount'] for t in transactions)
    return render_template('index.html', transactions=transactions, total=total_balance)

@app.route('/add', methods=['POST'])
def add_transaction():
    try:
        desc = request.form['desc'].strip()
        amount = float(request.form['amount'])
        
        if desc == "":
            flash("Deskripsi tidak boleh kosong!", "warning")
        else:
            transactions.append({'desc': desc, 'amount': amount})
            save_data(transactions)
            flash("✅ Transaksi berhasil ditambahkan!", "success")
    except ValueError:
        flash("❌ Nominal harus berupa angka!", "danger")

    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_transaction(index):
    if 0 <= index < len(transactions):
        deleted = transactions.pop(index)
        save_data(transactions)
        flash(f"🗑️ Transaksi '{deleted['desc']}' berhasil dihapus.", "info")
    else:
        flash("Transaksi tidak ditemukan.", "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5050)
