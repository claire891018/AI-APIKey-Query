

# **OpenAI API Key Query - Python Version**

This project is a Python reimplementation of the original [OpenAI-APIKey-Query](https://github.com/Ai-Yolo/OpenAI-APIKey-Query). It leverages **FastAPI** for the backend and **Streamlit** for the frontend, offering a more user-friendly interface.

## **Acknowledgements**

Special thanks to [Ai-Yolo](https://github.com/Ai-Yolo) for the inspiration and the original JavaScript implementation.

---

## **Project Structure**

```
openai-api-key-query-python/
│
├── backend/                   # Backend Service (FastAPI)
│   ├── routers/               # API Routers (with multi-language support)
│   │   └── openai.py          # OpenAI API query logic
│   ├── main.py                # FastAPI entry point
│   └── Dockerfile             # Backend Dockerfile
│
├── frontend/                  # Frontend Service (Streamlit)
│   ├── app.py                 # Main Streamlit application (with language switching)
│   └── Dockerfile             # Frontend Dockerfile
│
├── docker-compose.yml         # Docker Compose configuration
└── README.md                  # Documentation
```

---

## **Deployment Guide**

### **Prerequisites**

1. **Docker** and **Docker Compose** must be installed.

   - [Install Docker](https://docs.docker.com/get-docker/)
2. **Git** should be installed to clone the project:

   ```bash
   git clone https://github.com/your-repository.git
   cd openai-api-key-query-python
   ```

---

### **1. Deploy Using Docker Compose**

1. **Build and Run the Containers**:Execute the following command from the project root directory:

   ```bash
   docker-compose up --build -d
   ```

   **Explanation**:

   - `--build`: Rebuild the Docker images.
   - `-d`: Run the containers in detached mode (in the background).
2. **Verify that the Services are Running**:Use the following command to list the running containers:

   ```bash
   docker ps
   ```
3. **Access the Frontend Application**:Open your browser and navigate to:

   ```
   http://localhost:8501
   ```
4. **Test the Backend Service**:
   Access the FastAPI documentation and test API endpoints:

   ```
   http://localhost:8000/docs
   ```

---

### **2. Stop the Services**

To stop and remove the containers, run the following command:

```bash
docker-compose down
```

---

### **3. Troubleshooting**

- **Port Conflict**: If ports 8000 or 8501 are already in use, modify the port mappings in `docker-compose.yml`.
- **Backend Not Accessible**: Ensure that both the backend and frontend containers are running on the same Docker network.

---

## **Docker Compose Configuration**

`docker-compose.yml`:

```yaml
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    networks:
      - api_network

  frontend:
    build: ./frontend
    ports:
      - "8501:8501"
    networks:
      - api_network
    depends_on:
      - backend

networks:
  api_network:
    driver: bridge
```

---

## **Technical Support**

For issues or questions, please open an issue on [GitHub](https://github.com/your-repository). We will address your questions as soon as possible.

---

### **Acknowledgements**

Special thanks to [Ai-Yolo](https://github.com/Ai-Yolo) for the inspiration from the original JavaScript project.
