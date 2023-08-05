import json
from types import SimpleNamespace

class TimeRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Node:
    def __init__(self, ip, port, dns, mac):
        self.ip = ip
        self.port = port
        self.dns = dns
        self.mac = mac

class Flow:
    
    def __init__(self, obj):
        for field_name in self.get_all_fields():
            if field_name in obj.keys():
                setattr(self, field_name, obj.get(field_name))
            else:
                setattr(self, field_name, None)

    @staticmethod
    def get_class():
        return "flow"

    @staticmethod
    def get_all_fields():
        return [
            "_prn.id",
            "_prn.tx_id",
            "_chld.id",
            "_chld.type",
            "proto",
            "src.ip",
            "src.port",
            "src.mac",
            "src.dns",
            "src.geo.region",
            "src.geo.city",
            "src.geo.country",
            "src.geo.asn",
            "src.geo.org",
            "src.groups",
            "src.name",
            "src.host_id",
            "dst.ip",
            "dst.port",
            "dst.mac",
            "dst.dns",
            "dst.geo.region",
            "dst.geo.city",
            "dst.geo.country",
            "dst.geo.asn",
            "dst.geo.org",
            "dst.groups",
            "dst.name",
            "dst.host_id",
            "host.ip",
            "host.ip6",
            "host.port",
            "host.dns",
            "host.groups",
            "host.name",
            "bytes.total",
            "bytes.recv",
            "bytes.sent",
            "pkts.total",
            "pkts.recv",
            "pkts.sent",
            "state",
            "flags",
            "errors",
            "_reason",
            "_state",
            "tcp.flags",
            "tcp.flags_tc",
            "tcp.flags_ts",
            "tcp._state",
            "start",
            "end",
            "app_proto",
            "app_service",
            "pcaps",
            "tunnels.level",
            "tunnels.type",
            "tunnels.vlan_id",
            "tunnels.ip",
            "tunnels.ip6",
            "tunnels.endpoints.ip",
            "tunnels.endpoints.ip6",
            "tunnels.endpoints.port",
            "banner.client",
            "banner.server",
            "os.client",
            "os.server",
            "os_fp.client",
            "os_fp.server",
            "os_pt.client",
            "os_pt.server",
            "credentials.login",
            "credentials.password",
            "credentials.valid",
            "rpt.where",
            "rpt.id",
            "rpt.type",
            "rpt.cat",
            "rpt.color",
            "rpt.verdict",
            "rpt.rtime",
            "_ltime",
            "stag",
            "_ndx",
            "id",
            "_type",
            "_index",
            "_sort",
            "criticality",
            "false_positive",
            "has_files"]

    @staticmethod
    def get_basic_fields():
        return [
            "app_proto",
            "app_service",
            "banner.client",
            "banner.server",
            "bytes.recv",
            "bytes.sent",
            "bytes.total",
            "dst.dns",
            "dst.host_id",
            "dst.ip",
            "dst.mac",
            "dst.port",
            "end",
            "errors",
            "has_files",
            "id",
            "os.client",
            "os.server",
            "os_fp.client",
            "os_fp.server",
            "os_p0f.client",
            "os_p0f.server",
            "pkts.recv",
            "pkts.sent",
            "pkts.total",
            "src.dns",
            "src.host_id",
            "src.ip",
            "src.mac",
            "src.port",
            "start",
            "state",
            "tcp._state",
            "tcp.flags",
            "tcp.flags_tc",
            "tcp.flags_ts",
            "tcplen_stat.trunc",
            "tcplen_stat.value",
            "tunnels.endpoints.ip",
            "tunnels.endpoints.port",
            "tunnels.ip",
            "tunnels.level",
            "tunnels.type",
            "tunnels.vlan_id"]

    @classmethod
    def from_dict(cls, dictionary) -> 'Flow':
        return cls(dictionary)
