class DatabasePoolError(Exception):
    pass

class DatabasePool:
    _instance = None  # Singleton instance
    _max_connections = 5  # Max connections allowed

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabasePool, cls).__new__(cls)
            cls._instance._initialize_pool()
        return cls._instance
    
    def _initialize_pool(self):
        self._connections = []  # List to track active connections
    
    def get_connection(self):
        if len(self._connections) >= self._max_connections:
            raise DatabasePoolError("Connection pool exhausted. No available connections.")
        connection = f"Connection-{len(self._connections) + 1}"
        self._connections.append(connection)
        return connection
    
    def release_connection(self, connection):
        if connection in self._connections:
            self._connections.remove(connection)
        else:
            raise DatabasePoolError("Invalid connection release attempt.")

# Test Input
pool1 = DatabasePool()
pool2 = DatabasePool()
print(pool1 is pool2)  # Must be True (Singleton check)

conn1 = pool1.get_connection()
print(conn1)  # Should return a connection name

conn2 = pool1.get_connection()
print(conn2)

pool1.release_connection(conn1)
pool1.release_connection(conn2)

# Exhausting the pool
for _ in range(5):
    print(pool1.get_connection())

# This should raise an exception
print(pool1.get_connection())
