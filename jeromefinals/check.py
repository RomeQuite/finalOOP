import os

print("Checking project structure...")

# Check if manage.py exists
if not os.path.exists('manage.py'):
    print("ERROR: Not in project root! Run from folder with manage.py")
    exit()

print("✓ Found manage.py")

# Check template structure
template_path = 'myapp/templates/myapp/index.html'
if os.path.exists(template_path):
    print(f"✓ Found template: {template_path}")
else:
    print(f"✗ Missing: {template_path}")
    print("Creating template structure...")
    os.makedirs('myapp/templates/myapp', exist_ok=True)
    
    # Create simple index.html
    with open(template_path, 'w') as f:
        f.write('<h1>Jerome Portfolio - Template Found!</h1>')
    print(f"✓ Created: {template_path}")

# Check static folder
if os.path.exists('static/css'):
    print("✓ Found static/css folder")
else:
    print("✗ Missing static/css folder")
    os.makedirs('static/css', exist_ok=True)
    print("✓ Created static/css folder")

print("\n✅ Project structure is ready!")
print("Run: python manage.py runserver")