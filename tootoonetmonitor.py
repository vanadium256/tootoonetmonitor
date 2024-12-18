import psutil

def get_network_connections():
    # Получаем все сетевые соединения
    connections = psutil.net_connections(kind='inet')
    return connections

def get_process_info(pid):
    try:
        process = psutil.Process(pid)
        return process.name(), process.exe()
    except psutil.NoSuchProcess:
        return None, None

def main():
    connections = get_network_connections()
    print(f"{'PID':<10} {'Process Name':<25} {'Local Address':<25} {'Remote Address':<25}")

    for conn in connections:
        pid = conn.pid
        process_name, process_path = get_process_info(pid) if pid else (None, None)
        local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
        remote_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

        # Проверяем, если process_name или pid равен None
        if process_name is None:
            process_name = "N/A"
            pid = "N/A"

        print(f"{pid:<10} {process_name:<25} {local_address:<25} {remote_address:<25}")

if __name__ == "__main__":
    main()

