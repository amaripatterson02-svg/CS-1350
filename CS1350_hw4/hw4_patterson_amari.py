import re
import time
from collections import Counter

# -------------------------
# Problem 1: Grouping & Capturing
# -------------------------
def problem1():
    """
    Extract information using regex groups.
    """
    # a) Extract ISO format dates (YYYY-MM-DD)
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    # Pattern for ISO format dates
    pattern_iso = r'\b(\d{4}-\d{2}-\d{2})\b'
    iso_dates = re.findall(pattern_iso, dates_text)

    # b) Parse email addresses and extract username and domain
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    # Named capturing groups for username and domain
    pattern_email = r'(?P<username>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Za-z]{2,})'
    email_parts = []
    for m in re.finditer(pattern_email, emails_text):
        email_parts.append({
            'username': m.group('username'),
            'domain': m.group('domain')
        })

    # c) Extract phone numbers with area codes
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    # Capture area code (group 1) and the rest (group 2)
    pattern_phone = r'\b\(?(\d{3})\)?[ -]?(\d{3}-\d{4})\b'
    # findall returns list of tuples (area, number)
    phone_numbers = re.findall(pattern_phone, phones_text)

    # d) Find repeated words in text (consecutive repeated words)
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    # Use backreference to find consecutive repeated words (case-insensitive)
    pattern_repeated = r'\b([A-Za-z]+)\s+\1\b'
    repeated_words = [w.lower() for w in re.findall(pattern_repeated, repeated_text, flags=re.IGNORECASE)]

    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }


# -------------------------
# Problem 2: Alternation Patterns
# -------------------------
def problem2():
    """
    Use alternation to create flexible patterns.
    """
    # a) Image filenames
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    pattern_images = r'\b[\w\-.]+\.(?:jpg|jpeg|png|gif)\b'
    image_files = re.findall(pattern_images, files_text, flags=re.IGNORECASE)

    # b) Match different date formats
    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    # Match ISO, US (MM/DD/YYYY), and textual month formats
    months = r'(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)'
    pattern_dates = rf'\b(?:\d{{4}}-\d{{2}}-\d{{2}}|\d{{2}}/\d{{2}}/\d{{4}}|{months}\s+\d{{1,2}},\s+\d{{4}})\b'
    all_dates = re.findall(pattern_dates, mixed_dates, flags=re.IGNORECASE)

    # c) Prices in different formats
    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    pattern_prices = r'\b(?:\$\d+(?:\.\d{1,2})?|USD\s*\d+(?:\.\d{1,2})?|\d+(?:\.\d{1,2})?\s*dollars|€\d+(?:\.\d{1,2})?|£\d+(?:\.\d{1,2})?)\b'
    prices = re.findall(pattern_prices, prices_text, flags=re.IGNORECASE)

    # d) Programming language mentions (full names and abbreviations)
    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    pattern_langs = r'\b(?:Python|Java(?:Script)?|JS|C\+\+|CPP)\b'
    languages = re.findall(pattern_langs, code_text, flags=re.IGNORECASE)

    # Normalize languages to consistent case (preserve found case)
    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }


# -------------------------
# Problem 3: findall() vs finditer()
# -------------------------
def problem3():
    """
    Practice with findall() and finditer() methods.
    """
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    # a) Extract all timestamps using findall()
    pattern_timestamp = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]'
    timestamps = re.findall(pattern_timestamp, log_text)

    # b) Use findall() with groups to extract log levels and messages
    pattern_log = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]\s+(\w+):\s+(.*)'
    log_entries = re.findall(pattern_log, log_text)

    # c) Use finditer() to get positions of all IP addresses
    pattern_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = []
    for m in re.finditer(pattern_ip, log_text):
        ip_addresses.append({'ip': m.group(0), 'start': m.start(), 'end': m.end()})

    # d) Highlight ERROR entries: surround ERROR with ** markers
    def highlight_errors(text):
        return re.sub(r'\bERROR\b', r'**ERROR**', text)

    highlighted_log = highlight_errors(log_text)

    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }


# -------------------------
# Problem 4: re.sub() transformations
# -------------------------
def problem4():
    """
    Practice text transformation using re.sub().
    """
    # a) Standardize phone numbers to (XXX) XXX-XXXX
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """

    def standardize_phones(text):
        # Pattern matches (555) 123-4567, 555.123.4567, 555 345 6789, 5554567890, etc.
        pattern = re.compile(r'\b\(?(\d{3})\)?[.\s-]?(\d{3})[.\s-]?(\d{4})\b')
        def repl(m):
            g1, g2, g3 = m.group(1), m.group(2), m.group(3)
            return f'({g1}) {g2}-{g3}'
        return pattern.sub(repl, text)

    cleaned_phones = standardize_phones(messy_phones)

    # b) Redact sensitive information: SSN and Credit Card
    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    def redact_sensitive(text):
        # Redact SSN
        text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', text)
        # Redact credit card numbers (spaces or dashes optional)
        text = re.sub(r'\b(?:\d{4}[- ]?){3}\d{4}\b', 'XXXX-XXXX-XXXX-XXXX', text)
        return text

    redacted_text = redact_sensitive(sensitive_text)

    # c) Convert markdown links to HTML
    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    def markdown_to_html(text):
        # Replace [text](url) with <a href="url">text</a>
        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', text)

    html_text = markdown_to_html(markdown_text)

    # d) Simple template system: replace {key} with values[key]
    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {
        'name': 'John Smith',
        'order_id': '12345',
        'product': 'Python Book',
        'tracking': 'TRK789XYZ'
    }
    def fill_template(template_str, values_dict):
        def repl(m):
            key = m.group(1)
            return values_dict.get(key, m.group(0))  # leave placeholder if key not found
        return re.sub(r'\{(\w+)\}', repl, template_str)

    filled_template = fill_template(template, values)

    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }


# -------------------------
# Problem 5: Pattern Compilation & Optimization
# -------------------------
def problem5():
    """
    Use compiled patterns for efficiency and clarity.
    """
    class PatternLibrary:
        """
        Library of compiled regex patterns for common use cases.
        """
        # a) Email validation pattern (case insensitive)
        EMAIL = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', flags=re.IGNORECASE)

        # b) URL pattern (with optional protocol)
        URL = re.compile(r'^(?:https?://)?(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/.*)?$', flags=re.IGNORECASE)

        # c) US ZIP code (5 digits or 5+4 format)
        ZIP_CODE = re.compile(r'^\d{5}(?:-\d{4})?$')

        # d) Strong password (verbose pattern with comments)
        PASSWORD = re.compile(r'''
            ^               # start of string
            (?=.{8,}$)      # at least 8 characters
            (?=.*[A-Z])     # at least one uppercase letter
            (?=.*[a-z])     # at least one lowercase letter
            (?=.*\d)        # at least one digit
            (?=.*[^A-Za-z0-9]) # at least one special character
            .+              # one or more of any characters
            $               # end of string
        ''', flags=re.VERBOSE)

        # e) Credit card number (with spaces or dashes optional)
        CREDIT_CARD = re.compile(r'^(?:\d{4}[- ]?){3}\d{4}$')

    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
    }

    validation_results = {
        'emails': [bool(PatternLibrary.EMAIL.fullmatch(e)) for e in test_data['emails']],
        'urls': [bool(PatternLibrary.URL.fullmatch(u)) for u in test_data['urls']],
        'zips': [bool(PatternLibrary.ZIP_CODE.fullmatch(z)) for z in test_data['zips']],
        'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
        'cards': [bool(PatternLibrary.CREDIT_CARD.fullmatch(c.replace(' ', '').replace('-', '') if '-' in c or ' ' in c else c)) for c in test_data['cards']]
    }

    # Note: For credit card validation above, we used a simple tactic:
    # - For the supplied test inputs, check after removing separators; but the pattern actually allows separators.
    # We'll run a more straightforward check using the compiled pattern too:
    validation_results['cards'] = [bool(PatternLibrary.CREDIT_CARD.fullmatch(c)) for c in test_data['cards']]

    return validation_results


# -------------------------
# Problem 6: Real-World Log Analyzer
# -------------------------
def problem6():
    """
    Create a log file analyzer using regex.
    """
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200
    5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401
    234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200

    1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200
    15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
    # Comprehensive pattern: allow the size to be on same line or next line (whitespace)
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+HTTP/[0-9.]+"\s+(?P<status>\d{3})\s*(?P<size>\d+)?',
        flags=re.MULTILINE
    )

    parsed_logs = []
    for m in log_pattern.finditer(log_data):
        size_str = m.group('size')
        size = int(size_str) if size_str and size_str.isdigit() else 0
        status = int(m.group('status'))
        parsed_logs.append({
            'ip': m.group('ip'),
            'timestamp': m.group('timestamp'),
            'method': m.group('method'),
            'path': m.group('path'),
            'status': status,
            'size': size
        })

    # Analysis
    total_requests = len(parsed_logs)
    unique_ips = sorted({entry['ip'] for entry in parsed_logs})
    error_count = sum(1 for entry in parsed_logs if 400 <= entry['status'] < 600)
    total_bytes = sum(entry['size'] for entry in parsed_logs)
    path_counts = Counter(entry['path'] for entry in parsed_logs)
    most_requested_path = path_counts.most_common(1)[0][0] if path_counts else ''
    methods_used = sorted({entry['method'] for entry in parsed_logs})

    analysis = {
        'total_requests': total_requests,
        'unique_ips': unique_ips,
        'error_count': error_count,
        'total_bytes': total_bytes,
        'most_requested_path': most_requested_path,
        'methods_used': methods_used
    }

    return {
        'parsed_logs': parsed_logs,
        'analysis': analysis
    }


# -------------------------
# Run everything step-by-step and print results
# -------------------------
if __name__ == "__main__":
    print("=== Problem 1 ===")
    p1 = problem1()
    print("ISO Dates:", p1['iso_dates'])
    print("Email parts:", p1['email_parts'])
    print("Phone numbers:", p1['phone_numbers'])
    print("Repeated words:", p1['repeated_words'])
    print()

    print("=== Problem 2 ===")
    p2 = problem2()
    print("Image files:", p2['image_files'])
    print("All dates found:", p2['all_dates'])
    print("Prices found:", p2['prices'])
    print("Languages found:", p2['languages'])
    print()

    print("=== Problem 3 ===")
    p3 = problem3()
    print("Timestamps:", p3['timestamps'])
    print("Log entries (level,message):", p3['log_entries'])
    print("IP addresses with positions:", p3['ip_addresses'])
    print("Highlighted log (ERROR -> **ERROR**):")
    print(p3['highlighted_log'])
    print()

    print("=== Problem 4 ===")
    p4 = problem4()
    print("Cleaned phones:\n", p4['cleaned_phones'])
    print("Redacted sensitive text:\n", p4['redacted_text'])
    print("Markdown -> HTML:\n", p4['html_text'])
    print("Filled template:\n", p4['filled_template'])
    print()

    print("=== Problem 5 ===")
    p5 = problem5()
    print("Validation results:")
    for k, v in p5.items():
        print(f"  {k}: {v}")
    print()

    print("=== Problem 6 ===")
    p6 = problem6()
    print("Parsed logs:")
    for entry in p6['parsed_logs']:
        print(" ", entry)
    print("Analysis:")
    for k, v in p6['analysis'].items():
        print(" ", k, ":", v)
    print()