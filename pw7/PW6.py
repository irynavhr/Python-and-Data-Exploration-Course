# DEVELOPED BY IRYNA HRYTSENKO

import sqlite3

# create db
conn = sqlite3.connect('emails.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Domain;
DROP TABLE IF EXISTS Email;
DROP TABLE IF EXISTS Weekday;
DROP TABLE IF EXISTS Message;

CREATE TABLE Domain (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Email (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT UNIQUE,
    domain_id INTEGER,
    FOREIGN KEY (domain_id) REFERENCES Domain(id)
);

CREATE TABLE Weekday (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_id INTEGER,
    weekday_id INTEGER,
    spam_confidence REAL,
    FOREIGN KEY (email_id) REFERENCES Email(id),
    FOREIGN KEY (weekday_id) REFERENCES Weekday(id)
);
''')

# procces throuugh file AND fill db
with open("mbox-short.txt") as fh:
    email = None
    weekday = None
    spam_conf = None

    for line in fh:
        line = line.strip()
# ....................EXTRACT DATA................................................................
        # get email and day
        if line.startswith("From "):
            parts = line.split()
            if len(parts) >= 2:
                email = parts[1]
                weekday = parts[2]

        # spam confidence
        elif line.startswith("X-DSPAM-Confidence:"):
            try:
                spam_conf = float(line.split()[1].strip())
                # spam_conf = float(line.split(":")[1].strip())
            except:
                continue

            # domain
            domain = email.split('@')[1]
# ....................SAVE DATA......................................................
            # insert into Domain
            cur.execute('INSERT OR IGNORE INTO Domain (name) VALUES (?)', (domain,))
            cur.execute('SELECT id FROM Domain WHERE name = ?', (domain,))
            domain_id = cur.fetchone()[0]

            # insert into Email
            cur.execute('INSERT OR IGNORE INTO Email (address, domain_id) VALUES (?, ?)', (email, domain_id))
            cur.execute('SELECT id FROM Email WHERE address = ?', (email,))
            email_id = cur.fetchone()[0]

            # insert into Weekday
            cur.execute('INSERT OR IGNORE INTO Weekday (name) VALUES (?)', (weekday,))
            cur.execute('SELECT id FROM Weekday WHERE name = ?', (weekday,))
            weekday_id = cur.fetchone()[0]

            # insert into Message
            cur.execute('INSERT INTO Message (email_id, weekday_id, spam_confidence) VALUES (?, ?, ?)',
                        (email_id, weekday_id, spam_conf))

            # for next record
            email = None
            weekday = None
            spam_conf = None

conn.commit()

# printing...............
print("\nUnique Domains:")
cur.execute('SELECT name FROM Domain ORDER BY name')
domains = cur.fetchall()

for domain in domains:
    print(f"- {domain[0]}")

# ..................................................................
user_domain = input("\nEnter a domain from the list above: ")

query = '''
SELECT Weekday.name, Domain.name, Email.address, Message.spam_confidence
FROM Message
JOIN Email ON Message.email_id = Email.id
JOIN Domain ON Email.domain_id = Domain.id
JOIN Weekday ON Message.weekday_id = Weekday.id
WHERE Domain.name = ? AND (Weekday.name = "Fri" OR Weekday.name = "Sat")
ORDER BY Weekday.name
'''

print("\nResults (Only Friday & Saturday Emails):")
print(f"{'Day':<10} {'Domain':<25} {'Email':<30} {'Spam Confidence'}")
print("-" * 80)

for row in cur.execute(query, (user_domain,)):
    print(f"{row[0]:<10} {row[1]:<25} {row[2]:<30} {row[3]:.4f}")


conn.close()