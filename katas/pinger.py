import subprocess
import time

# Note
# The unittest for this kata *must mock* the ping to avoid actual network calls.



#

def ping_host(hostname: str, count: int = 5):
    """
    Pings a host and returns connection statistics.
    
    Args:
        hostname: Host to ping (e.g., 'google.com')
        count: Number of ping attempts
        
    Returns:
        Dictionary with:
        - 'host': hostname
        - 'avg_response_time_ms': average response time in milliseconds
        - 'success': True if any packets received
    """
    # TODO: Use subprocess.run() to execute ping command
    # Linux/Mac: ping -c {count} {hostname}
    # Parse output to extract the average latency in milliseconds
    string = subprocess.run(["ping","-c",str(count),hostname], capture_output=True, text=True)
    ping_result = string.__dict__["stdout"] 
    avg_time = float(ping_result.split("=")[-1].split("/")[1])
    print("Average time:", avg_time, "ms")  

    return {
        'host': hostname,
        'avg_response_time_ms': avg_time,  # Placeholder value
        'success': True if string.returncode == 0 else False             # Placeholder value
    }




if __name__ == '__main__':
    # Test the functions
    ping_result = ping_host("8.8.8.8", 3)
    print(f"Ping result: {ping_result}")
