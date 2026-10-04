# Credit Card Fraud Detection

Research and software workspace for fraud detection experiments and a dashboard/API prototype. The frontend uses Vue 3, TypeScript, and Vite; the backend uses FastAPI; model development lives in `data-science/`.

## Start the services

From this directory, run `docker compose up --build`. The dashboard is served at `http://localhost:8080`, the API docs at `http://localhost:8000/docs`, and the health endpoint at `http://localhost:8000/health`.

For local development, install frontend dependencies in `frontend/` with `npm install` and run `npm run dev`. Install backend dependencies with `pip install -r backend/requirements.txt`, then run `uvicorn app.main:app --reload` from `backend/`.

## Data handling

Do not commit payment-card data, credentials, `.env` files, or trained model binaries. Confirm dataset permissions and de-identification requirements before placing data in `data-science/data/`. Keep the example environment files free of secrets.

The API routes and dashboard components are starter scaffolding; connect them to approved data sources and a validated model before operational use.
