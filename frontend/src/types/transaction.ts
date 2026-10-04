export interface Transaction {
  id: string;
  amount: number;
  currency: string;
  timestamp: string;
  isFraud: boolean;
  riskScore: number;
}
