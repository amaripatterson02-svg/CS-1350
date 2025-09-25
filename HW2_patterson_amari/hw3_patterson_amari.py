import re

# ---------------- Part 1 ----------------
def format_receipt(items, prices, quantities):
    sep = "=" * 40
    header = f"{'Item':<20}{'Qty':^5}{'Price':>15}"
    lines = [sep, header, sep]
    total = 0.0
    for item, price, qty in zip(items, prices, quantities):
        line_total = price * qty
        total += line_total

        lines.append(f"{item:<20}{str(qty):^5}{'$':>3}{line_total:6.2f}")
    lines.append(sep)
    lines.append(f"{'TOTAL':<25}{'$':>3}{total:6.2f}")
    lines.append(sep)
    return "\n".join(lines)

def process_user_data(raw_data):
    result = {}

    name = re.sub(r'\s+', ' ', raw_data.get('name', '').strip()).title()
    result['name'] = name

    email = raw_data.get('email', '').strip().replace(' ', '').lower()
    result['email'] = email

    phone = re.sub(r'\D', '', raw_data.get('phone', ''))
    result['phone'] = phone

    address = re.sub(r'\s+', ' ', raw_data.get('address', '').strip()).title()
    result['address'] = address

    parts = name.split()
    if len(parts) >= 2:
        username = f"{parts[0].lower()}_{parts[-1].lower()}"
    elif parts:
        username = parts[0].lower()
    else:
        username = ''
    result['username'] = username
    # Validation dict (basic checks)
    validation = {}
    validation['email_valid'] = bool(re.match(r'^[\w\.\-+]+@[\w\.\-]+\.[A-Za-z]{2,}$', email))
    validation['phone_valid'] = len(phone) == 10
    validation['name_valid'] = len(parts) >= 2
    validation['address_valid'] = bool(re.search(r'\d+', address)) and bool(re.search(r'[A-Za-z]+', address))
    result['validation'] = validation
    return result

def analyze_text(text):
    out = {}
    out['total_chars'] = len(text)
    lines = text.splitlines()
    out['total_lines'] = len(lines)
    words = re.findall(r'\b\w+\b', text)
    out['total_words'] = len(words)
    out['avg_word_length'] = round(sum(len(w) for w in words) / len(words), 2) if words else 0.0
    lowered = [w.lower() for w in words]
    freq = {}
    for w in lowered:
        freq[w] = freq.get(w, 0) + 1
    out['most_common_word'] = max(freq.items(), key=lambda kv: (kv[1], kv[0]))[0] if freq else None
    out['longest_line'] = max(lines, key=len) if lines else ''
    out['words_per_line'] = [len(re.findall(r'\b\w+\b', line)) for line in lines]
    # Sentences ending with punctuation
    sentences = re.findall(r'[^.!?]*[.!?]', text)
    cap_sent = 0
    q_count = 0
    ex_count = 0
    for s in sentences:
        s_stripped = s.strip()
        if not s_stripped:
            continue
        m = re.search(r'[A-Za-z]', s_stripped)
        if m and s_stripped[m.start()].isupper():
            cap_sent += 1
        if s_stripped.endswith('?'):
            q_count += 1
        if s_stripped.endswith('!'):
            ex_count += 1
    out['capitalized_sentences'] = cap_sent
    out['questions'] = q_count
    out['exclamations'] = ex_count
    return out

# ---------------- Part 2 ----------------
def find_patterns(text):
    patterns = {
        'integers': r'(?<!\d)\b\d+\b(?!\.\d)',
        'decimals': r'\b\d+\.\d+\b',
        'words_with_digits': r'\b\w*\d\w*\b',
        'capitalized_words': r'\b[A-Z][a-zA-Z]*\b',
        'all_caps_words': r'\b[A-Z]{2,}\b',
        'repeated_chars': r'\b\w*(\w)\1\w*\b'
    }
    result = {}
    result['decimals'] = re.findall(patterns['decimals'], text)
    result['integers'] = re.findall(patterns['integers'], text)
    result['words_with_digits'] = re.findall(patterns['words_with_digits'], text)
    result['capitalized_words'] = re.findall(patterns['capitalized_words'], text)
    result['all_caps_words'] = re.findall(patterns['all_caps_words'], text)
    result['repeated_chars'] = [m.group(0) for m in re.finditer(patterns['repeated_chars'], text, flags=re.IGNORECASE)]
    return result

def validate_format(input_string, format_type):
    patterns = {
        'phone': r'^(?:\((?P<area_code>\d{3})\)\s*(?P<prefix>\d{3})-(?P<line>\d{4})|(?P<area_code2>\d{3})-(?P<prefix2>\d{3})-(?P<line2>\d{4}))$',
        'date': r'^(?P<month>0[1-9]|1[0-2])/(?P<day>0[1-9]|[12]\d|3[01])/(?P<year>(?:19|20)\d{2})$',
        'time': r'^(?:((?P<hour12>0?[1-9]|1[0-2]):(?P<min12>[0-5]\d)\s*(?P<ampm>[AaPp][Mm]))|(?P<hour24>[01]?\d|2[0-3]):(?P<min24>[0-5]\d))$',
        'email': r'^(?P<user>[\w\.\-+]+)@(?P<domain>[\w\.\-]+\.[A-Za-z]{2,})$',
        'url': r'^(?P<scheme>https?)://(?P<domain>[\w\.-]+)(?::(?P<port>\d+))?(?P<path>/\S*)?$',
        'ssn': r'^(?P<area>\d{3})-(?P<group>\d{2})-(?P<serial>\d{4})$'
    }
    pat = patterns.get(format_type)
    if not pat:
        return (False, None)
    m = re.match(pat, input_string)
    if not m:
        return (False, None)
    parts = {}
    if format_type == 'phone':
        if m.group('area_code'):
            parts['area_code'] = m.group('area_code')
            parts['prefix'] = m.group('prefix')
            parts['line'] = m.group('line')
        else:
            parts['area_code'] = m.group('area_code2')
            parts['prefix'] = m.group('prefix2')
            parts['line'] = m.group('line2')
    elif format_type == 'date':
        parts['month'] = m.group('month')
        parts['day'] = m.group('day')
        parts['year'] = m.group('year')
    elif format_type == 'time':
        if m.group('hour12'):
            parts['hour'] = m.group('hour12')
            parts['minute'] = m.group('min12')
            parts['ampm'] = m.group('ampm')
        else:
            parts['hour'] = m.group('hour24')
            parts['minute'] = m.group('min24')
            parts['ampm'] = None
    elif format_type == 'email':
        parts['user'] = m.group('user')
        parts['domain'] = m.group('domain')
    elif format_type == 'url':
        parts['scheme'] = m.group('scheme')
        parts['domain'] = m.group('domain')
        parts['port'] = m.group('port')
        parts['path'] = m.group('path')
    elif format_type == 'ssn':
        parts['area'] = m.group('area')
        parts['group'] = m.group('group')
        parts['serial'] = m.group('serial')
    return (True, parts)

def extract_information(text):
    result = {}
    result['prices'] = re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
    result['percentages'] = re.findall(r'\b\d+(?:\.\d+)?%', text)
    result['years'] = re.findall(r'\b(?:19\d{2}|20\d{2})\b', text)
    result['sentences'] = re.findall(r'[^.!?]*[.!?]', text)
    result['questions'] = [s.strip() for s in result['sentences'] if s.strip().endswith('?')]
    result['quoted_text'] = re.findall(r'"([^"]+)"', text)
    return result

# ---------------- Part 3 ----------------
def clean_text_pipeline(text, operations):
    steps = []
    current = text
    steps.append(current)
    for op in operations:
        if op == 'trim':
            current = current.strip()
        elif op == 'lowercase':
            current = current.lower()
        elif op == 'remove_punctuation':
            current = re.sub(r'[^\w\s]', '', current)
        elif op == 'remove_digits':
            current = re.sub(r'\d+', '', current)
        elif op == 'remove_extra_spaces':
            current = re.sub(r'\s+', ' ', current).strip()
        elif op == 'remove_urls':
            current = re.sub(r'http[s]?://\S+', '', current)
        elif op == 'remove_emails':
            current = re.sub(r'[\w\.\-+]+@[\w\.\-]+\.\w+', '', current)
        elif op == 'capitalize_sentences':
            parts = re.split(r'([.!?]\s*)', current)
            new = ''
            for i in range(0, len(parts), 2):
                sentence = parts[i]
                sep = parts[i+1] if i+1 < len(parts) else ''
                s_strip = sentence.strip()
                if s_strip:
                    s_strip = s_strip[0].upper() + s_strip[1:]
                new += s_strip + sep
            current = new
        steps.append(current)
    return {'original': text, 'cleaned': current, 'steps': steps}

def smart_replace(text, replacements):
    result = text
    contractions = {
        "don't": "do not",
        "won't": "will not",
        "can't": "cannot",
        "i'm": "I am",
        "you're": "you are",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "we're": "we are",
        "they're": "they are",
        "i've": "I have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have"
    }
    digit_words = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

    if replacements.get('censor_phone'):
        result = re.sub(r'\(?\d{3}\)?[\s\-]?\d{3}-\d{4}', 'XXX-XXX-XXXX', result)
    if replacements.get('censor_email'):
        result = re.sub(r'[\w\.\-+]+@[\w\.\-]+\.\w+', '[EMAIL]', result)
    if replacements.get('fix_spacing'):
        result = re.sub(r'\s+([,.;:!?])', r'\1', result)
        result = re.sub(r'([,.;:!?])([^\s])', r'\1 \2', result)
    if replacements.get('expand_contractions'):
        pattern = r'\b(' + '|'.join(re.escape(k) for k in contractions.keys()) + r')\b'
        def repl_contr(m):
            return contractions.get(m.group(0).lower(), m.group(0))
        result = re.sub(pattern, repl_contr, result, flags=re.IGNORECASE)
    if replacements.get('number_to_word'):
        def num_repl(m):
            return digit_words.get(m.group(0), m.group(0))
        result = re.sub(r'\b[0-9]\b', num_repl, result)
    return result

# ---------------- Part 4 ----------------
def analyze_log_file(log_text):
    lines = [l for l in log_text.splitlines() if l.strip()]
    total_entries = len(lines)
    error_count = warning_count = info_count = 0
    dates = set()
    error_messages = []
    times = []
    hour_counts = {}
    for line in lines:
        m = re.match(r'^\[(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\]\s*(?P<level>[A-Z]+):\s*(?P<msg>.*)$', line)
        if not m:
            continue
        d = m.group('date')
        t = m.group('time')
        level = m.group('level').upper()
        msg = m.group('msg').strip()
        dates.add(d)
        times.append(t)
        hour = int(t.split(':')[0])
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
        if level == 'ERROR':
            error_count += 1
            error_messages.append(msg)
        elif level == 'WARNING':
            warning_count += 1
        elif level == 'INFO':
            info_count += 1
    earliest_time = min(times) if times else None
    latest_time = max(times) if times else None
    most_active_hour = max(hour_counts.items(), key=lambda kv: kv[1])[0] if hour_counts else None
    return {
        'total_entries': total_entries,
        'error_count': error_count,
        'warning_count': warning_count,
        'info_count': info_count,
        'dates': sorted(list(dates)),
        'error_messages': error_messages,
        'time_range': (earliest_time, latest_time),
        'most_active_hour': most_active_hour
    }
# ---------------- Tests ----------------
def run_tests():
    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    print("Receipt Test:")
    print(format_receipt(items, prices, quantities))

    print("\nClean user data test:")
    data = {'name': ' john DOE ', 'email': ' JOHN@EXAMPLE.COM ', 'phone': '(555) 123-4567', 'address': '123 main street'}
    cleaned = process_user_data(data)
    print("Name:", cleaned['name'])
    print("Email:", cleaned['email'])
    print("Phone:", cleaned['phone'])
    print("Username:", cleaned['username'])

    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)
    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print("Integers:", patterns['integers'])
    print("Decimals:", patterns['decimals'])
    print("Validate phone:", validate_format("(555) 123-4567", "phone"))

    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)
    print(clean_text_pipeline(" Hello WORLD! Visit https://example.com ", ['trim', 'lowercase', 'remove_urls', 'remove_extra_spaces']))

    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
[2024-01-15 10:31:00] INFO: Retry attempt
[2024-01-15 10:32:00] WARNING: Timeout warning"""
    print(analyze_log_file(sample_log))
    print("="*50)

if __name__ == "__main__":
    run_tests()