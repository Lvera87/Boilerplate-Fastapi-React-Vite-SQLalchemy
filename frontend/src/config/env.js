const API_VERSION = import.meta.env.VITE_API_VERSION ?? 'v1';
const API_BASE_PATH = import.meta.env.VITE_API_BASE_PATH ?? '/api';

export const API_BASE_URL = `${API_BASE_PATH}/${API_VERSION}`;
