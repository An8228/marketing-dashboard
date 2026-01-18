import { useEffect, useState } from "react";
import KpiCard from "../components/KpiCard";
import { fetchAnalyticsSummary } from "../api/analytics";

import RecommendationCard from "../components/RecommendationCard";
import { fetchRecommendations } from "../api/analytics";


type AnalyticsSummary = {
  total_campaigns: number;
  total_spend: number;
  total_revenue: number;
  roi: number;
};



export default function Dashboard() {
  const [data, setData] = useState<AnalyticsSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [recommendations, setRecommendations] = useState<
  { title: string; reason: string }[]
>([]);


  useEffect(() => {
  fetchAnalyticsSummary()
    .then(setData)
    .catch(() => setError("Failed to load analytics"))
    .finally(() => setLoading(false));

  fetchRecommendations()
    .then(setRecommendations)
    .catch(() => {});
}, []);

  if (loading) {
  return (
    <>
      <h1>Key Metrics</h1>
      <div className="kpi-grid">
        {[1, 2, 3, 4].map((i) => (
          <div key={i} className="kpi-card skeleton" />
        ))}
      </div>
    </>
  );
}

  if (error) return <p>{error}</p>;
  if (!data) return null;

  return (
    <>
      <h1>Key Metrics</h1>

      <div className="kpi-grid">
        <KpiCard title="Total Campaigns" value={data.total_campaigns} />
        <KpiCard title="Total Spend" value={`$${data.total_spend}`} subtitle="This Month" />
        <KpiCard title="Total Revenue" value={`$${data.total_revenue}`} subtitle="This Month" />
        <KpiCard title="ROI" value={`${data.roi}%`} subtitle="This Month" />
      </div>
    </>
    

  );

}

