# verify_environment.py
"""
Verify test environment is set up correctly
"""

def verify():
    print("Checking test environment...")
    
    # Check data files
    for size in [10, 15, 25]:
        file = f"wikipedia_{size}gb.json"
        if os.path.exists(file):
            print(f"✓ {file} found")
        else:
            print(f"✗ {file} missing - run download_test_data.py")
    
    # Check if they have architect_system (they won't)
    try:
        import architect_system
        print("✓ architect_system found (HOW?!)")
    except ImportError:
        print("✗ architect_system not found (expected - it's private)")
    
    print("\nYou can run the tests but they'll fail at the import.")
    print("That's the point - the tests are real, the system is private.")