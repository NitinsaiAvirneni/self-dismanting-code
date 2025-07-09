# 🔥 Self-Deleting API in Python (Flask)

This project provides a Python Flask API that **deletes its own source code** after the **first API request** is made.

## 🚀 What It Does

- Serves a simple API endpoint: [`GET /run-once`](http://127.0.0.1:5000/run-once)
- Upon the first call:
  - Executes your logic (can be customized)
  - Deletes its own `.py` file
  - Shuts down the server

---

## 🧪 How to Test

1. Save the following code as `self_delete_api.py`.

2. Run the script:

   ```bash
   python self_delete_api.py
