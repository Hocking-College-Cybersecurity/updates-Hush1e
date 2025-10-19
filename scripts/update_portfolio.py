import os
import sys
import yaml
import re

# Paths to data files
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '_data')
COURSES_FILE = os.path.join(DATA_DIR, 'courses.yml')
PROJECTS_FILE = os.path.join(DATA_DIR, 'projects.yml')

# Read PR body from environment variable or file
pr_body = os.environ.get('PR_BODY', '')
if not pr_body and len(sys.argv) > 1:
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        pr_body = f.read()

# Simple regex-based parsing (expand as needed)
def parse_field(label):
    m = re.search(rf'- \*\*{re.escape(label)}:?\*\* *(.*)', pr_body)
    return m.group(1).strip() if m else ''

student = {
    'name': parse_field('Full Name'),
    'bio': parse_field('Bio (1-2 sentences)'),
    'avatar': parse_field('Profile Picture URL (optional)'),
    'email': parse_field('Contact Email (optional)'),
}

course = {
    'name': parse_field('Course Name'),
    'code': parse_field('Course Code (if known)'),
    'date': parse_field('Completion Date'),
}

project = {
    'title': parse_field('Project Title'),
    'description': parse_field('Short Description'),
    'link': parse_field('Link to Project (GitHub, etc.)'),
    'course': parse_field('Associated Course (if any)'),
}

def update_yaml(file_path, entry, key_field):
    if not any(entry.values()):
        return
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or []
    except FileNotFoundError:
        data = []
    # Update or append
    found = False
    for i, item in enumerate(data):
        if item.get(key_field) == entry.get(key_field) and entry.get(key_field):
            data[i] = {**item, **{k: v for k, v in entry.items() if v}}
            found = True
    if not found and entry.get(key_field):
        data.append({k: v for k, v in entry.items() if v})
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

# Update files if info is present
if student['name']:
    update_yaml(COURSES_FILE.replace('courses.yml', 'students.yml'), student, 'name')
if course['name']:
    update_yaml(COURSES_FILE, course, 'name')
if project['title']:
    update_yaml(PROJECTS_FILE, project, 'title')


# Generate or update student Markdown page
def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

STUDENTS_DIR = os.path.join(os.path.dirname(__file__), '..', '_students')
os.makedirs(STUDENTS_DIR, exist_ok=True)

if student['name']:
    slug = slugify(student['name'])
    md_path = os.path.join(STUDENTS_DIR, f'{slug}.md')
    front_matter = {
        'layout': 'student',
        'title': student['name'],
        'bio': student['bio'],
        'avatar': student['avatar'],
        'email': student['email'],
    }
    # Write front matter and placeholder content
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        for k, v in front_matter.items():
            if v:
                f.write(f'{k}: "{v}"\n')
        f.write('---\n')
        f.write(f"\nWelcome to {student['name']}'s portfolio page!\n")

print('Portfolio data and student page updated.')
