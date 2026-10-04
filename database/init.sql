CREATE TABLE IF NOT EXISTS transactions (
    id TEXT PRIMARY KEY,
    amount NUMERIC(18, 2) NOT NULL CHECK (amount >= 0),
    currency CHAR(3) NOT NULL,
    occurred_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS predictions (
    id BIGSERIAL PRIMARY KEY,
    transaction_id TEXT NOT NULL REFERENCES transactions(id),
    risk_score NUMERIC(6, 5) NOT NULL CHECK (risk_score >= 0 AND risk_score <= 1),
    is_fraud BOOLEAN NOT NULL,
    model_version TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
