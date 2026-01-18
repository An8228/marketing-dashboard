import { useEffect, useState } from "react";
import KpiCard from "../components/KpiCard";
import RecommendationCard from "../components/RecommendationCard";
import {
  fetchAnalyticsSummary,
  fetchRecommendations,
} from "../api/analytics";

/* ---------------- TYPES ---------------- */

type AnalyticsSummary = {
  total_campaigns: number;
  total_spend: number;
  total_revenue: number;
  roi: number;
};

type Recommendation = {
  id: string;
  title: string;
  description: string;
};

/* ---------------- COMPONENT ---------------- */

export default function Dashboard() {
  const [data, setData] = useState<AnalyticsSummary | null>(null);
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([
      fetchAnalyticsSummary(),
      fetchRecommendations(),
    ])
      .then(([summary, recs]) => {
        setData(summary);
        setRecommendations(recs);
      })
      .catch(() => setError("Failed to load dashboard data"))
      .finally(() => setLoading(false));
  }, []);

  /* ---------------- STATES ---------------- */

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

  if (error || !data) {
    return <p className="error">{error}</p>;
  }

  /* ---------------- UI ---------------- */

  return (
    <>
      {/* ===== KPIs ===== */}
      <h1>Key Metrics</h1>
      <div className="kpi-grid">
        <KpiCard title="Total Campaigns" value={data.total_campaigns} />
        <KpiCard
          title="Total Spend"
          value={`$${data.total_spend}`}
          subtitle="This Month"
        />
        <KpiCard
          title="Total Revenue"
          value={`$${data.total_revenue}`}
          subtitle="This Month"
        />
        <KpiCard
          title="ROI"
          value={`${data.roi}%`}
          subtitle="This Month"
        />
      </div>

      {/* ===== RECOMMENDATIONS ===== */}
      <h2>Recommendations</h2>
      <div className="recommendations-grid">
        {recommendations.map((rec) => (
          <RecommendationCard
            key={rec.id}
            title={rec.title}
            description={rec.description}
          />
        ))}
      </div>

      {/* ===== STEP 5: PERFORMANCE INSIGHTS ===== */}
      <h2>Performance Insights</h2>
      <div className="insights-placeholder">
        <p>
          Advanced charts, trend analysis, and AI-driven insights will appear
          here in the next phase.
        </p>
      </div>
    </>
  );
}
