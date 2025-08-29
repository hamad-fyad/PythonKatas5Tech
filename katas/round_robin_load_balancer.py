class IP:
    """
    Represents an IPv4 address. s
    """

    def __init__(self, address: str):
        """
        Initializes an IP address.

        Args:
            address: The IP address as a string.

        Raises:
            ValueError: If the address is invalid.
        """
        address = address.strip()
        if not self._is_valid_ip(address):
            raise ValueError(f"Invalid IP address: {address}")
        self.address = address

    def _is_valid_ip(self, address: str) -> bool:
        """
        Validates an IPv4 address.

        Args:
            address: The address string to validate.

        Returns:
            True if valid, False otherwise.
        """
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        return True
        

    def __str__(self):
        return self.address

    def __eq__(self, other):
        return isinstance(other, IP) and self.address == other.address

    def __hash__(self):
        raise NotImplementedError("hashCode logic not implemented.")


class RoundRobinLoadBalancer:
    """
    Implements a round-robin load balancer.

    A load balancer distributes requests to a pool of EC2 instances.
    This implementation routes requests in a circular (a.k.a. round-robin) manner.
    """

    def __init__(self):
        """
        Initializes the load balancer with an empty pool of servers.
        """
        self.servers = []
        self.server_index = 0 

    def add_server(self, server: IP):
        """
        Adds a server instance to the load balancer.

        Args:
            server: An IP instance representing the server to add.
        """
        self.servers.append(server)

    def remove_server(self, server: IP):
        """
        Removes a server instance from the load balancer.

        Args:
            server: An IP instance representing the server to remove.
        """
        self.servers.remove(server)

    def route_request(self) -> IP | None:
        """
        Routes a request to the next server in round-robin order.

        Returns:
            The IP instance of the server handling the request, or None if no servers are available.
        """
    
        servers_length = len(self.servers)
        if servers_length == 0 : 
            return None
        server = self.servers[self.server_index]
        self.server_index = (self.server_index + 1) % servers_length
        return server
        



if __name__ == '__main__':
    lb = RoundRobinLoadBalancer()

    lb.add_server(IP("192.168.0.1"))
    lb.add_server(IP("192.168.0.2"))
    lb.add_server(IP("192.168.0.3"))

    print("Routing to:", lb.route_request())  # Should route to 192.168.0.1 server
    print("Routing to:", lb.route_request())  # Should route to 192.168.0.2 server
    print("Routing to:", lb.route_request())  # Should route to 192.168.0.3 server
    print("Routing to:", lb.route_request())  # Should route to 192.168.0.1 server again

    lb.remove_server(IP("192.168.0.2")) # Remove second server

    print("Routing to:", lb.route_request()) # Should route to 192.168.0.3 server
    print("Routing to:", lb.route_request()) # Should route to 192.168.0.1 server again
