from katas.round_robin_load_balancer import RoundRobinLoadBalancer,IP
import unittest

class TestRoundRobinLoadBalancer(unittest.TestCase):
    def setUp(self):
        self.lb = RoundRobinLoadBalancer()
        self.server1 = IP("112.32.43.11")
        self.server2 = IP("112.32.43.12")
        self.server3 = IP("112.32.43.13")
        self.server4 = IP("112.32.43.14")
        self.lb.add_server(self.server1)
        self.lb.add_server(self.server2) 
        self.lb.add_server(self.server3)   
        self.lb.add_server(self.server4)

    def test_round_robin_order(self):
        # First request should go to server1
        self.assertEqual(self.lb.route_request(), self.server1)
        # Next to server2
        self.assertEqual(self.lb.route_request(), self.server2)
        # Next to server3
        self.assertEqual(self.lb.route_request(), self.server3)
        # Next to server4
        self.assertEqual(self.lb.route_request(), self.server4)
        # Should wrap around back to server1
        self.assertEqual(self.lb.route_request(), self.server1)

    def test_remove_server(self):

        self.lb.remove_server(self.server1)

        self.assertNotEqual(self.lb.route_request(),self.server1)

        self.assertEqual(self.lb.route_request(), self.server3)

        self.assertEqual(self.lb.route_request(), self.server4)

        self.assertEqual(self.lb.route_request(), self.server2)

    def test_add_server(self):
        server5 = IP("112.32.43.15")
        self.lb.add_server(server5)
        for _ in range(4):
            self.lb.route_request()
        self.assertEqual(self.lb.route_request(),server5)

if __name__ == '__main__':
    unittest.main()
