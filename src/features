# src/features/extract_features.py
import re
import urllib.parse
import socket
import ssl
import whois
from datetime import datetime

def has_ip(url):
    """Return 1 if URL uses an IP address instead of domain name."""
    try:
        hostname = urllib.parse.urlparse(url).netloc
        # strip port
        hostname = hostname.split(':')[0]
        # IPv4 regex
        if re.match(r'^\d+\.\d+\.\d+\.\d+$', hostname):
            return 1
        # IPv6 heuristic
        if ':' in hostname and any(c in hostname for c in "abcdef0123456789"):
            return 1
    except Exception:
        return 0
    return 0

def count_subdomains(url):
    try:
        hostname = urllib.parse.urlparse(url).netloc
        hostname = hostname.split(':')[0]
        return hostname.count('.')  # simple heuristic
    except Exception:
        return 0

def has_https(url):
    try:
        return 1 if urllib.parse.urlparse(url).scheme == 'https' else 0
    except Exception:
        return 0

def count_special_chars(url):
    return sum(url.count(ch) for ch in ['@', '-', '_', '?', '=', '&', '%', '$'])

def url_length(url):
    return len(url)

def has_at_symbol(url):
    return 1 if '@' in url else 0

def count_digits(url):
    return sum(c.isdigit() for c in url)

def contains_suspicious_words(url):
    suspicious = ['login', 'signin', 'bank', 'secure', 'update', 'verify', 'account']
    url_low = url.lower()
    return int(any(word in url_low for word in suspicious))

def domain_age_days(domain):
    """Return age in days of domain. If cannot fetch, return -1."""
    try:
        w = whois.whois(domain)
        creation = w.creation_date
        if isinstance(creation, list):
            creation = creation[0]
        if not creation:
            return -1
        if isinstance(creation, str):
            creation = datetime.strptime(creation.split(' ')[0], '%Y-%m-%d')
        delta = datetime.now() - creation
        return max(delta.days, 0)
    except Exception:
        return -1

def extract_domain(url):
    try:
        host = urllib.parse.urlparse(url).netloc
        return host.split(':')[0].lower()
    except Exception:
        return ''

def extract_features(url):
    """
    Return a dict of features for a single URL.
    Keep features simple & fast for real-time use.
    """
    feats = {}
    feats['url_length'] = url_length(url)
    feats['count_digits'] = count_digits(url)
    feats['count_subdomains'] = count_subdomains(url)
    feats['has_ip'] = has_ip(url)
    feats['has_https'] = has_https(url)
    feats['count_special_chars'] = count_special_chars(url)
    feats['has_at'] = has_at_symbol(url)
    feats['suspicious_words'] = contains_suspicious_words(url)
    domain = extract_domain(url)
    feats['domain_age_days'] = domain_age_days(domain) if domain else -1
    # simple token features
    feats['count_slash'] = url.count('/')
    feats['count_dot'] = url.count('.')
    return feats

# Example quick test
if __name__ == "__main__":
    test_url = "http://192.168.0.1/login.php?user=abc"
    print(extract_features(test_url))
