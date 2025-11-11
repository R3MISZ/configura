# 🧩 JSON BASICS — Examples & Explanations

**JSON** stands for **JavaScript Object Notation**.  
It’s a lightweight, text-based data format used for structured data — simple, universal, and language-independent.  
Commonly used for APIs, configurations, and data exchange.

---

## 🧠 1. Scalars (Basic Data Types)

JSON supports **string**, **number**, **boolean**, and **null** values.

```json
{
  "string": "Hello World",
  "number_integer": 42,
  "number_float": 3.14159,
  "number_scientific": 1.23e4,
  "boolean_true": true,
  "boolean_false": false,
  "null_value": null
}
```

💡 **Notes:**
- Strings must be wrapped in double quotes (`" "`).
- No comments allowed.
- Numbers can be integers, floats, or scientific notation.

---

## ✍️ 2. Strings & Escaping

JSON strings support Unicode, backslashes, and escape sequences.

```json
{
  "quote": "He said: \"JSON is strict.\"",
  "backslash": "C:\\Temp\\file.txt",
  "unicode": "Zażółć gęślą jaźń",
  "emoji": "🚀",
  "newline": "line1\nline2"
}
```

💡 **Notes:**
- Double quotes inside strings must be escaped (`\"`).
- Backslashes (`\\`) must also be escaped.
- Unicode and emoji are fully supported.
- Use `\n` for new lines.

---

## 🔢 3. Arrays

An array is an **ordered list** of values.  
It can contain numbers, strings, objects, and even other arrays.

```json
{
  "numbers": [1, 2, 3, 4, 5],
  "mixed": ["text", 123, true, null, {"k": "v"}, [10, 20]]
}
```

💡 **Notes:**
- Arrays use square brackets `[ ]`.
- Elements are comma-separated.
- JSON allows arrays to hold mixed data types (though avoid that in clean design).

---

## 🧍 4. Objects (Key-Value Pairs)

Objects store data as **key-value pairs**.  
Keys must be strings in double quotes.

```json
{
  "person": {
    "name": "R3MISZ",
    "age": 34,
    "skills": ["Python", "C#", "Clean Code"],
    "address": { "street": "Respo1", "city": "Github", "zip": "1101" }
  }
}
```

💡 **Notes:**
- Objects use curly braces `{ }`.
- Each key must be unique (later duplicates overwrite earlier ones).
- You can nest objects inside each other.

---

## 👥 5. Array of Objects

A common structure for representing lists of similar items.

```json
[
  { "name": "Alice", "role": "Admin", "active": true },
  { "name": "Bob", "role": "User", "active": false },
  { "name": "Charlie", "role": "Moderator", "active": true }
]
```

💡 **Use Case:** users, tasks, datasets, configurations, etc.

---

## 🧾 6. Object Containing Arrays

Useful for role permissions or grouped configurations.

```json
{
  "roles": {
    "Admin": ["can_read", "can_write", "can_delete"],
    "User": ["can_read"],
    "Moderator": ["can_read", "can_ban"]
  }
}
```

💡 **Notes:**
- Combines objects and arrays.
- Keys represent categories (Admin, User, Moderator).

---

## ⚙️ 7. Nested Configuration Example

Demonstrates deeply nested objects and arrays.

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "credentials": { "user": "root", "password": "1234" }
  },
  "features": [
    { "name": "logging", "enabled": true },
    { "name": "backup", "enabled": false }
  ]
}
```

💡 **Notes:**
- Useful for application configs.
- Structure must always be valid JSON (no trailing commas).

---

## 🗓️ 8. Dates and IDs

JSON doesn’t have a native `date` type — strings are used instead.

```json
{
  "iso8601_string": "2025-11-08T12:34:56Z",
  "uuid_like_string": "550e8400-e29b-41d4-a716-446655440000"
}
```

💡 **Notes:**
- ISO-8601 strings are the standard for dates.
- UUIDs are stored as plain strings.

---

## ⚠️ 9. Gotchas (Common Mistakes)

Some things that are valid in other languages **don’t work** in JSON.

```json
{
  "leading_trailing_commas_allowed": false,
  "comments_allowed": false,
  "duplicate_keys_example": { "key": "first", "key": "second" }
}
```

💡 **Warnings:**
- No trailing commas after the last element.
- No comments allowed (`#` or `//` will break parsing).
- Duplicate keys are allowed syntactically but only the last one counts.

---

## 🧩 10. Mixed Example (All in One)

A complete configuration combining most JSON structures.

```json
{
  "name": "Project mixed",
  "version": 1.0,
  "authors": ["R3MISZ", "AI Assistant"],
  "tags": ["clean code", "modular"],
  "settings": {
    "debug": true,
    "timeout_sec": 10,
    "paths": {
      "input": "examples/data.json",
      "output": "out/result.txt"
    }
  }
}
```

💡 **Notes:**
- Combine simple and nested structures for complex configurations.
- Always validate JSON with tools like `jsonlint` or `jq`.

---

## ✅ Summary

| Concept | Description |
|----------|-------------|
| Scalars | Simple data types: string, number, boolean, null |
| Arrays | Ordered lists `[ ]` |
| Objects | Key-value pairs `{ }` |
| Nesting | Combine objects and arrays for complex data |
| Escaping | Use `\\` for backslashes, `\"` for quotes |
| Comments | ❌ Not allowed in JSON |
| Encoding | Always UTF-8; supports emoji & Unicode |
| Validation | Use `jsonlint` or `jq` to verify correctness |
