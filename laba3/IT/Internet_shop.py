from IT.Server import Server
from IT.Website import Website
class Internet_shop:
    def __init__(self, website, mobile_app):
        self.website = website
        self.servers = []

    def add_server(self, server):
        if hasattr(server, 'get_info'):
            self.servers.append(server)
            print(f"Сервер {server.ip_address} добавлен в платформу")

    def get_platform_info(self):
        info = " САЙТ:\n"
        info += self.website.get_info() + "\n\n"
        info += f"СЕРВЕРОВ: {len(self.servers)}\n"
        for i, server in enumerate(self.servers, 1):
            info += f"{i}. {server.get_info()}\n"
        return info

    def is_platform_online(self):
        if not self.website.is_online():
            return False
        if not self.servers:
            return False
        return any(server.is_running() for server in self.servers)