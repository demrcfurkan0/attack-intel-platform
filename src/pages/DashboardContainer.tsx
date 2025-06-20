import { useState, useEffect } from 'react';
import IndexPage from './Index'; 
import { getAttackTrends, getDetectionMetrics } from '@/services/statisticsService';

const DashboardContainer = () => {
  const [dashboardData, setDashboardData] = useState({
    detected_attacks: 0,
    benign_traffic: 0,
    total_simulations: 0,
  });
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchAllData = async () => {
      setIsLoading(true);
      try {
        const [metricsRes, trendsRes] = await Promise.all([
          getDetectionMetrics(),
          getAttackTrends(),
        ]);

        const totalSims = Object.values(trendsRes.data).reduce(
          (acc, hour) => acc + (hour.ddos || 0) + (hour.brute_force || 0) + (hour.sql_injection || 0),
          0
        );

        setDashboardData({
          detected_attacks: metricsRes.data.detected_attacks,
          benign_traffic: metricsRes.data.benign_traffic,
          total_simulations: totalSims,
        });

      } catch (error) {
        console.error("Failed to fetch dashboard container data:", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchAllData();
    const intervalId = setInterval(fetchAllData, 30000);
    return () => clearInterval(intervalId);
  }, []);

  return <IndexPage data={dashboardData} isLoading={isLoading} />;
};

export default DashboardContainer;