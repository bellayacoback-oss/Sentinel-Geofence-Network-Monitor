import os
import shutil

# 1. Define where we want our 'Clean' portfolio
portfolio_dir = "/sdcard/Documents/Sentinel_Portfolio"

if not os.path.exists(portfolio_dir):
    os.makedirs(portfolio_dir)
    print(f"[+] Created: {portfolio_dir}")

# 2. Search current directory for our hard work
files = os.listdir('.')
for f in files:
    if f.endswith('.py') or f.endswith('.txt'):
        shutil.copy(f, portfolio_dir)
        print(f"[->] Copied {f} to Portfolio folder")

print("\n--- CLEANUP COMPLETE ---")
print(f"Go to your 'Files' app -> Documents -> Sentinel_Portfolio to see your work!")
