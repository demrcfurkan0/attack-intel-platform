import { render, screen } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest'; // veya jest
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ActiveThreatsCard } from './ActiveThreatsCard';


const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: false,
    },
  },
});

const wrapper = ({ children }: { children: React.ReactNode }) => (
  <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
);

vi.mock('@/services/statisticsService', () => ({
  getDetectionMetrics: () => Promise.resolve({ data: { detected_attacks: 42, benign_traffic: 158 } }),
}));


describe('ActiveThreatsCard Component', () => {

  it('should render the correct title', () => {
    render(<ActiveThreatsCard />, { wrapper });

    const titleElement = screen.getByText(/detected attacks/i);
    
    expect(titleElement).toBeInTheDocument();
  });

  it('should display the count from the mocked API call', async () => {
    render(<ActiveThreatsCard />, { wrapper });

    const countElement = await screen.findByText('42');
    
    expect(countElement).toBeInTheDocument();
  });

});