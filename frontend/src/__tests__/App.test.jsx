import { render, screen } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

import App from '@/App.jsx';

function renderApp() {
  const queryClient = new QueryClient();
  render(
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>,
  );
}

describe('App', () => {
  it('renderiza el título principal', () => {
    renderApp();
    expect(screen.getByRole('heading', { name: /fastapi \+ react boilerplate/i })).toBeInTheDocument();
  });
});
