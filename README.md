# FastAPI Key-Value Server

## Overview

The FastAPI Key-Value Server is a simple web application that provides an HTTP API for accessing key-value pairs stored in an immutable data file. The server allows clients to query for values by providing keys and responds with the corresponding values from the dataset.

## Getting Started

To run the FastAPI Key-Value Server locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/adhithyasrinivasan/key-value-server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd key-value-server
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the server:

   ```bash
   python3 -m uvicorn app.main:app --host 0.0.0.0 --reload
   ```
5. We can also run the runner script to install the dependencies, run the unit tests and start the server:

   ```bash
   chmod 744 runner.sh
   ./runner.sh
   ```

The server should now be running locally on `http://localhost:8000`.

## API Structure

The FastAPI Key-Value Server exposes the following API endpoints:

### Get Value

- **Method**: `GET`
- **URL**: `/get_value/{uuid}`
- **Response**:
  - `200 OK`: Returns the value corresponding to the provided key.
  - `404 Not Found`: If the provided key does not exist in the dataset.
  - `422 Unprocessable Entity`: If the key parameter is missing or invalid.

#### Example

Request:

```http
GET /get_value/72cf48f7-d604-4423-b012-4e2329f5117b
```

Response:

```json
{
  "key": "72cf48f7-d604-4423-b012-4e2329f5117b",
  "value": "zsda pl focnygogk x cjuu cmwrolqrmu wgdwxr"
}
```

## Data File

The key-value pairs are stored in an immutable data file provided with the application. The file format is as follows:

```
72cf48f7-d604-4423-b012-4e2329f5117b zsda pl focnygogk x cjuu cmwrolqrmu wgdwxr
...
```

Each line contains a UUID key followed by a space and the corresponding value.

## Testing

To run tests for the FastAPI Key-Value Server, use the following command:

```bash
python -m pytest
```

## System operation in detail:
The FastAPI Key-Value Server is a web application that offers a user-friendly API for retrieving values associated with UUID keys from an immutable data file. Upon initialization, the server efficiently loads key-value pairs from the data file into memory, optimizing access speed. Clients interact with the server by providing a key, prompting the server to retrieve the corresponding value from the in-memory dataset. Utilizing asynchronous request handling, the server ensures swift response times and maintains high performance even under heavy loads.

Additionally, the system incorporates an LRU (Least Recently Used) cache mechanism to further optimize data retrieval. This cache stores recently accessed key-value pairs in memory, reducing the need to repeatedly access the underlying data file. As a result, common requests benefit from accelerated response times, enhancing overall system efficiency.

Furthermore, robust error handling mechanisms are in place to gracefully manage scenarios where the provided key is missing or invalid, ensuring reliability and resilience. Currently, the system demonstrates scalability by accommodating up to 1 crore lines of records. Looking ahead, future enhancements aim to bolster the system's scalability further, enabling it to efficiently handle even larger datasets with ease.

## System Performance and Scalability Analysis:
1. Scalability: The system is designed to handle a large volume of data, capable of processing up to 1 crore (10 million) lines of records within a single file. Despite the substantial dataset, the system maintains an average latency of approximately 120 to 130 milliseconds per request, encompassing validation, routing, and other processing steps within FastAPI.
2. Future Scalability: Currently, the system efficiently manages larger files with 1 crore lines of records. To further enhance scalability, future enhancements may involve implementing threading and other concurrency concepts. These optimizations aim to ensure that the system can seamlessly handle even larger loads and maintain optimal performance as the dataset continues to grow.

## Anticipated failure patterns for the FastAPI Key-Value Server may include:

1. Server Crashes: Due to hardware failures, software bugs, or resource exhaustion, the server may crash and become unavailable.
2. Network Failures: Network issues such as timeouts, packet loss, or DNS failures can disrupt communication between clients and the server.
3. Data Corruption: Errors during data processing or storage can lead to data corruption, resulting in incorrect responses or system failures.
4. Denial of Service (DoS) Attacks: Malicious users may attempt to overload the server with a high volume of requests, causing it to become unresponsive or crash.
5. Concurrency Issues: In cases of high concurrency, race conditions or deadlocks may occur, leading to unexpected behavior or server instability.
6. Dependency Failures: Failures or misconfigurations of external dependencies such as databases or caching systems can impact the server's functionality.
7. Security Vulnerabilities: Unauthorized access, injection attacks, or other security vulnerabilities may compromise the integrity and availability of the server.

## Future Scope:

1. Authentication and Authorization: Implementing authentication mechanisms such as JWT (JSON Web Tokens) or OAuth2 for secure access control to the API endpoints.
2. Parallel Processing and Concurrency: Introducing parallel processing techniques such as multi-threading or asynchronous programming to improve the efficiency of data processing, especially for large datasets.
3. Input Data Partitioning: Enhancing the system to support input data partitioning, allowing for distributed processing and scalability across multiple nodes or servers.
4. Caching Strategies: Implementing advanced caching strategies such as Redis or Memcached to improve response times and reduce the load on backend systems.
5. Monitoring and Logging: Integrating monitoring and logging tools to track system performance metrics, detect anomalies, and troubleshoot issues in real-time.
6. Rate Limiting and Throttling: Adding rate limiting and throttling mechanisms to prevent abuse and ensure fair usage of system resources.
7. Batch Processing Support: Adding support for batch processing to handle bulk data operations efficiently.
8. API Versioning: Introducing API versioning to support backward compatibility and facilitate future updates without breaking existing client implementations.
9. Fault Tolerance and Resilience: Enhancing the system's fault tolerance and resilience by implementing strategies such as circuit breakers and graceful degradation.
10. Documentation and API Documentation: Improving documentation for both developers and end-users, including comprehensive API documentation using tools like Swagger or OpenAPI.
11. File Lock / UnLock mechanism: Introducing a File Lock/Unlock mechanism enhances the robustness of the FastAPI Key-Value Server by ensuring data consistency and preventing concurrent access issues.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.