import { render, screen } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest'; // veya jest
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ActiveThreatsCard } from './ActiveThreatsCard';

// React Query'nin useQuery hook'u bir QueryClientProvider içinde çalışmalıdır.
// Testler için bir sarmalayıcı (wrapper) oluşturalım.
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // Testlerin hızlı çalışması için yeniden denemeleri kapat
      retry: false,
    },
  },
});

const wrapper = ({ children }: { children: React.ReactNode }) => (
  <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
);

// useQuery'den gelen sahte bir yanıt oluşturarak API çağrısını mock'layalım.
// Bu, testimizin API'ye bağımlı olmasını engeller.
vi.mock('@/services/statisticsService', () => ({
  getDetectionMetrics: () => Promise.resolve({ data: { detected_attacks: 42, benign_traffic: 158 } }),
}));


describe('ActiveThreatsCard Component', () => {

  it('should render the correct title', () => {
    // Component'i sarmalayıcı ile render et
    render(<ActiveThreatsCard />, { wrapper });

    // "Detected Attacks" metninin ekranda olup olmadığını kontrol et
    // `getByText` büyük/küçük harf duyarsızdır.
    const titleElement = screen.getByText(/detected attacks/i);
    
    // Elementin belgede (DOM'da) var olduğunu doğrula
    expect(titleElement).toBeInTheDocument();
  });

  it('should display the count from the mocked API call', async () => {
    render(<ActiveThreatsCard />, { wrapper });

    // API'den dönen sahte veri olan "42" sayısını bul
    // `findByText` asenkron işlemler için kullanılır ve bir Promise döndürür.
    const countElement = await screen.findByText('42');
    
    // Sayının belgede var olduğunu doğrula
    expect(countElement).toBeInTheDocument();
  });

});