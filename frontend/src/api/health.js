import client from './client.js';

export async function fetchHealthStatus() {
  const response = await client.get('/health/');
  return response.data;
}
