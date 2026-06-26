import axios from 'axios';
import type { GeneratePayload, ImageRecord } from '../types/image';

const API_URL = 'http://127.0.0.1:8000';

export async function generateImage(payload: GeneratePayload): Promise<ImageRecord> {
  const response = await axios.post(`${API_URL}/api/generate`, payload);
  return response.data;
}

export async function getHistory(): Promise<ImageRecord[]> {
  const response = await axios.get(`${API_URL}/api/history`);
  return response.data;
}

export async function deleteHistoryItem(id: number): Promise<void> {
  await axios.delete(`${API_URL}/api/history/${id}`);
}
