# Taxi Dispatch Service

This project simulates a taxi dispatch service that assigns the nearest available taxi to clients based on their pickup location. The system consists of a FastAPI service, a PostgreSQL database, and multiple taxi services running as containers. You can also simulate client orders to test the system's functionality.

## Getting Started

### Running the Containers

To build and run the containers for the database, dispatch service, and taxis, run the following commands:

```bash
docker compose build
docker compose up -d
docker compose logs -f
```

This will bring up the necessary services:

- `db`: PostgreSQL database
- `dispatch`: The FastAPI dispatch service
- `taxi_1`, `taxi_2`, etc.: Taxi service containers

If you need more taxis, you can add additional sections for taxis in `docker-compose.yml`.

### Simulating Client Requests

To simulate client orders, run the following Python script:

```bash
python client_order_simulation.py
```

This script will generate client requests at configurable intervals, simulating the taxi dispatch process. The configuration can be adjusted directly in the script.

#### Configuration

The simulation can be configured by modifying the following parameters in `client_order_simulation.py`:

- **`INTERVAL`**: Time between batches of client orders.
- **`ORDERS_PER_INTERVAL`**: Number of client orders generated per interval.
- **`GRID_SIZE`**: The size of the grid for generating pickup and dropoff locations.

## Areas for Improvement

While the project is functional, there are several areas where improvements could be made:

### 1. Time Constraints and Context Switching

This project took longer than anticipated due to constant context switching between other projects and private commitments. The result is some incomplete or suboptimal implementations, including:

- **Git History**: The commit history isn't as clean as I'd like. Frequent interruptions broke the development flow, leading to a less organized version control history.
  
### 2. SQLAlchemy Models and Relationships

The current implementation of SQLAlchemy models could use some refactoring. One missing feature is the relation between taxis and their locations. This would improve the structure and querying efficiency.

### 3. Testing Coverage

There should be more test cases to cover edge scenarios. Currently, the project has limited test coverage, and adding more unit tests would enhance the robustness of the system.

### 4. Dependency Injection

The current implementation of dependency injection can be improved. It currently supports two adapters `InMemoryAdapter` and `PostgresAdapter`, but it can be streamlined. You can switch between adapters in the `dispatch/app/routes/taxi.py` file:

```python
# Dependency to provide the adapter (can be replaced with other adapters like PostgresAdapter)
# def get_adapter() -> TaxiAdapter:
#     return InMemoryAdapter()

# Dependency to provide the PostgresAdapter
def get_adapter(db: Session = Depends(get_db)) -> TaxiAdapter:
    return PostgresAdapter(db)
```

This mechanism works with both `InMemoryAdapter` and `PostgresAdapter`, but there's room for improvement in how the dependency injection is handled, especially if you want to scale the project further.

## Conclusion

Despite the challenges, the project provides a functional taxi dispatch service with the ability to handle multiple clients and taxis. There are a few areas for improvement, especially in the dependency injection, model relationships, and testing, but the foundation is in place.

I got stuck a few times on various things – for example, mocking uuid.uuid4 for testing purposes. Theoretically, it was supposed to be easy, but it caused some problems.

The code structure could definitely be improved. Perhaps the chosen architecture and code separation aren't the best.

Besides that, thank you for the interesting task. I may not have completed all the points, but time didn't allow for more. Nevertheless, I had a lot of fun, and I'll probably come back to this to organize it in my head and try to write something like this in the 4 hours that Nina mentioned. :)