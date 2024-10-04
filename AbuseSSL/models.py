
from datetime import datetime

class IP:
    def __init__(self, ip_address, collected_at=None, source=" abuse.ch SSLBL", related_iocs=None,
                 related_urls=None, related_domains=None, whois_info=None, geo_info=None,
                 ssl_certificate_info=None, reputation_score=None, threat_type=None,
                 malware_samples=None, port=None, tags=None):
        self.ip_address = ip_address
        self.collected_at = collected_at 
        self.source = source
        self.port= port
        self.related_iocs = related_iocs or []
        self.related_urls = related_urls or []
        self.related_domains = related_domains or []
        self.whois_info = whois_info or {}
        self.geo_info = geo_info or {}
        self.ssl_certificate_info = ssl_certificate_info or []
        self.reputation_score = reputation_score
        self.threat_type = threat_type
        self.malware_samples = malware_samples or []
        self.tags = tags or []
        self.last_modified = datetime.utcnow().isoformat()



