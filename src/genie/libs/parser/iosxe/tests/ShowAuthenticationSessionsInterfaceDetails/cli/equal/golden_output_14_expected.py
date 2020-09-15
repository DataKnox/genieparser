expected_output = {
    "interfaces": {
        "GigabitEthernet1/0/6": {
            "mac_address": {
                "0024.9bff.077a": {
                    "ipv6_address": "Unknown",
                    "iif_id": "0x1FB8CAD0",
                    "ipv4_address": "Unknown",
                    "user_name": "User1",
                    "status": "Authorized",
                    "domain": "DATA",
                    "oper_host_mode": "multi-auth",
                    "oper_control_dir": "both",
                    "session_timeout": {"type": "N/A"},
                    "common_session_id": "0A788905000029BE6BFF02FE",
                    "acct_session_id": "0x00004bca",
                    "handle": "0x010009d6",
                    "current_policy": "Test_DOT1X-DEFAULT_V1",
                    "method_status": {
                        "dot1x": {"method": "dot1x", "state": "Authc Success"},
                        "mab": {"method": "mab", "state": "Stopped"},
                    },
                    "server_policies": {
                        1: {
                            "security_policy": "None",
                            "security_status": "Link Unsecured",
                            "name": "ACS ACL",
                            "policies": "xACSACLx-IP-Test_ACL_PERMIT_ALL-565bad69",
                        }
                    },
                }
            }
        }
    }
}
