def average_salary(row):
    return (row['Min Salary'] + row['Max Salary']) / 2

def clean_html(text):
    import re
    return re.sub('<[^<]+?>', '', text)

def normalize_title(title):
    return title.strip().title()

def classify_role(title):
    title = title.lower()
    if "data" in title:
        return "Data"
    elif "engineer" in title:
        return "Engineering"
    elif "analyst" in title:
        return "Analyst"
    elif "developer" in title:
        return "Development"
    else:
        return "Other"
