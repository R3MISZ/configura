# 🧩 YAML BASICS — Examples & Explanations

YAML stands for **“YAML Ain’t Markup Language”**.  
It’s a **human-readable** text format for structured data, commonly used for configuration files such as Docker, CI/CD, GitHub Actions, and more.

---

## 🧠 1. Scalar Values (Basic Data Types)

YAML supports basic types like strings, integers, floats, booleans, and null.

```yaml
string: "Hello World"           # String (text)
integer: 42                     # Integer (whole number)
float: 3.14159                  # Floating-point number
boolean_true: true              # Boolean (true)
boolean_false: false            # Boolean (false)
null_value: null                # Null / None value
```

Strings can be quoted or not:

```yaml
simple_string: Hello
quoted_string: "Allowed with spaces"
```

Multiline text block (preserves line breaks):

```yaml
multiline_text: |
  This is a multiline text.
  Line breaks and indentation are preserved.
  Useful for documentation or long descriptions.
```

Folded text block (merges line breaks into one line):

```yaml
single_line_text: >
  This is a multiline text,
  but when parsed, it becomes a single line.
```

---

## 🍎 2. Lists (Arrays)

A list is a collection of values. Each item starts with a dash `-`.

```yaml
fruits:
  - Apple
  - Banana
  - Cherry
```

Inline version:

```yaml
numbers: [1, 2, 3, 4, 5]
```

---

## 👤 3. Dictionaries / Maps (Key-Value Pairs)

YAML uses **indentation** to represent structure — indentation defines hierarchy!

```yaml
person:
  name: "Kacper"
  age: 25
  hobbies:
    - Motorcycles
    - Learning
    - Psychology
  address:
    street: "Example Street 7"
    city: "Ingolstadt"
    zip: 85049
```

---

## 👥 4. Lists of Dictionaries

Very common for pipelines, users, or configurations.

```yaml
users:
  - name: "Alice"
    role: "Admin"
    active: true
  - name: "Bob"
    role: "User"
    active: false
  - name: "Charlie"
    role: "Moderator"
    active: true
```

---

## 🧾 5. Dictionary with Lists

Useful for role-based permissions or grouped settings.

```yaml
roles:
  Admin:
    - can_read
    - can_write
    - can_delete
  User:
    - can_read
  Moderator:
    - can_read
    - can_ban
```

---

## ⚙️ 6. Nested Structures (Combining Both)

You can nest dictionaries and lists as deeply as you like.

```yaml
config:
  database:
    host: localhost
    port: 5432
    credentials:
      user: "root"
      password: "1234"
  features:
    - name: "logging"
      enabled: true
    - name: "backup"
      enabled: false
```

---

## 💬 7. Comments

Everything starting with `#` is a **comment** and is ignored by the parser.

```yaml
# This is a comment
example: true   # Inline comments are also fine
```

---

## ♻️ 8. Aliases & References (Advanced)

You can **reuse** sections using **anchors (&)** and **aliases (*)**.

```yaml
default_settings: &defaults
  theme: "dark"
  language: "en"
  autosave: true

user_settings:
  <<: *defaults        # Merge all values from &defaults
  language: "de"       # Override 'language' from defaults
```

---

## 🧩 9. Mixed Example (All in One)

This combines all key YAML concepts:  
scalars, lists, maps, nested structures, and merging.

```yaml
example_mixed:
  name: "Project Configura"
  version: 1.0
  authors: ["R3MISZ", "AI Assistant"]
  tags:
    - clean code
    - modular
  settings:
    debug: true
    timeout: 10
    paths:
      input: "examples/data.json"
      output: "out/result.txt"
```

---

## ✅ Summary

| Concept | Description |
|----------|-------------|
| Scalars | Basic values like strings or numbers |
| Lists | Ordered sequences starting with `-` |
| Dictionaries | Key-value structures with indentation |
| Anchors & Aliases | Reuse or merge existing blocks |
| Comments | Lines starting with `#` are ignored |
| Indentation | Defines structure — **critical in YAML** |
