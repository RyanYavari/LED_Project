from sqlite_helpers import createTable, addUser, updateUser, displayAllUsers, top_users, resetAllUsers

def test_sqlite_helpers():
    print("\n=== Starting SQLite Helper Tests ===\n")
    
    # 1. Create/connect to database
    db_file = "test_database.db"
    print("Test 1: Creating database and table...")
    createTable(db_file)
    
    # 2. Add users
    
    addUser(db_file, "bob", 15, 45, easy_solved=7, medium_solved=5, hard_solved=7)
    addUser(db_file, "carol", 20, 60, easy_solved=10, medium_solved=7, hard_solved=3)
    addUser(db_file, "dave", 25, 75, easy_solved=12, medium_solved=10, hard_solved=3)
    addUser(db_file, "eve", 30, 90, easy_solved=15, medium_solved=12, hard_solved=3)
    addUser(db_file, "frank", 35, 105, easy_solved=17, medium_solved=15, hard_solved=3)
    addUser(db_file, "grace", 40, 120, easy_solved=20, medium_solved=17, hard_solved=3)
    addUser(db_file, "heidi", 45, 135, easy_solved=22, medium_solved=20, hard_solved=5)
    addUser(db_file, "ivan", 50, 150, easy_solved=25, medium_solved=22, hard_solved=3)
    addUser(db_file, "judy", 55, 165, easy_solved=27, medium_solved=25, hard_solved=3)
    
    # 3. Display initial state
    print("\nTest 3: Displaying initial user state...")
    displayAllUsers(db_file)
    
    # 4. Update a user
    print("\nTest 4: Updating Bob's stats...")
    updateUser(db_file, "bob", 25, 75, 12, 8, 5)
    print("\nAfter update:")
    displayAllUsers(db_file)
    
    # 5. Try updating non-existent user
    print("\nTest 5: Attempting to update non-existent user...")
    updateUser(db_file, "nonexistent", 0, 0, 0, 0, 0)
    
    # 6. Show top users
    print("\nTest 6: Displaying top users...")
    top_users(db_file)
    
    # 7. Reset all users
    print("\nTest 7: Testing reset all users...")
    resetAllUsers(db_file)
    print("\nAfter reset:")
    displayAllUsers(db_file)
    
    # 8. Test adding duplicate user
    print("\nTest 8: Testing duplicate user handling...")
    addUser(db_file, "alice", 5, 15, 3, 2, 0)
    
    print("\n=== SQLite Helper Tests Complete ===")

if __name__ == "__main__":
    test_sqlite_helpers()